"""
デジタルチラシ新規営業支援ツール
──────────────────────────────────
都道府県を選択すると、その地域に「10店舗以上 かつ 総店舗数の40%以上」を
持つ契約企業を一覧表示します。
"""

import time
import streamlit as st
import pandas as pd

from companies import COMPANIES, PREFECTURES
from scraper import fetch_company_data, load_cache, clear_cache
from init_seed import init_seed

# ── ページ設定 ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="都道府県別デジタルチラシ導入企業",
    page_icon="🛒",
    layout="wide",
)

# ── パスワード認証 ────────────────────────────────────────────────────────────
PASSWORD = st.secrets["password"]

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("🔒 ログイン")
    pw = st.text_input("パスワードを入力してください", type="password")
    if st.button("ログイン"):
        if pw == PASSWORD:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("パスワードが違います")
    st.stop()

st.title("🛒 都道府県別デジタルチラシ導入企業")
st.caption("都道府県を選択すると、その地域に集中している契約企業を表示します。")

# ── サイドバー ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("🔍 検索条件")

    selected_pref = st.selectbox(
        "都道府県を選択",
        PREFECTURES,
        index=PREFECTURES.index("東京都"),
    )

    st.divider()
    st.header("⚙️ フィルター設定")
    min_stores = st.number_input(
        "最低店舗数（その地域）", min_value=1, max_value=100, value=10, step=1
    )
    min_ratio = st.slider(
        "最低割合（総店舗数に対する地域比率）",
        min_value=0, max_value=100, value=0, step=5,
        format="%d%%",
    )

    st.divider()
    st.header("🔄 データ管理")

    col1, col2 = st.columns(2)
    with col1:
        fetch_all = st.button("全社データ取得", use_container_width=True)
    with col2:
        refresh = st.button("キャッシュ更新", use_container_width=True, type="secondary")

    st.caption(
        "「全社データ取得」: 未取得の企業のみ収集（数分かかります）\n"
        "「キャッシュ更新」: 全企業を再収集"
    )

    st.divider()
    st.header("🏢 業態フィルター")
    show_sm = st.checkbox("SM（スーパー）", value=True)
    show_dgs = st.checkbox("DGS（ドラッグストア）", value=True)

# ── データ取得ロジック ────────────────────────────────────────────────────────

@st.cache_data(show_spinner=False)
def get_all_cached() -> dict:
    result = {}
    for c in COMPANIES:
        cached = load_cache(c["name"])
        if cached:
            result[c["name"]] = cached
    return result


def run_fetch(companies_to_fetch: list, force: bool = False):
    progress = st.progress(0, text="データ取得を開始します...")
    status_text = st.empty()
    total = len(companies_to_fetch)

    for i, c in enumerate(companies_to_fetch):
        status_text.text(f"取得中: {c['short']}（{i+1}/{total}）")
        fetch_company_data(c["name"], c["short"], force=force)
        progress.progress((i + 1) / total, text=f"取得中... {i+1}/{total}件")
        time.sleep(0.3)

    progress.empty()
    status_text.empty()
    st.cache_data.clear()
    st.success(f"✅ {total}社のデータ取得が完了しました。")
    st.rerun()


# 初回起動時にシードデータを投入
if "seed_initialized" not in st.session_state:
    init_seed(overwrite=False)
    st.session_state["seed_initialized"] = True

if fetch_all:
    targets = [c for c in COMPANIES if not load_cache(c["name"])]
    if targets:
        run_fetch(targets, force=False)
    else:
        st.sidebar.success("全社のデータ取得済みです。")

if refresh:
    run_fetch(COMPANIES, force=True)

# ── メイン表示 ────────────────────────────────────────────────────────────────

# キャッシュ済みデータを収集
cached_data = {c["name"]: load_cache(c["name"]) for c in COMPANIES}
fetched_count = sum(1 for v in cached_data.values() if v is not None and v.get("by_prefecture"))
total_count = len(COMPANIES)

# 進捗バー
progress_pct = fetched_count / total_count if total_count else 0
st.progress(progress_pct, text=f"店舗データ取得済み: {fetched_count} / {total_count} 社")

if fetched_count == 0:
    st.info("👈 サイドバーの「全社データ取得」ボタンを押してください。（初回のみ数分かかります）")
    st.stop()

# ── 絞り込みとテーブル生成 ────────────────────────────────────────────────────
rows = []

for c in COMPANIES:
    # 業態フィルター
    if c["type"] == "SM" and not show_sm:
        continue
    if c["type"] == "DGS" and not show_dgs:
        continue

    data = cached_data.get(c["name"])
    if not data or data["status"] == "not_found":
        continue

    total = data.get("total", 0)
    pref_count = data.get("by_prefecture", {}).get(selected_pref, 0)

    if total == 0:
        continue

    ratio = pref_count / total if total > 0 else 0

    # 条件チェック
    if pref_count >= min_stores and ratio >= min_ratio / 100:
        rows.append({
            "企業名": c["name"],
            "ブランド名": c["short"],
            "業態": c["type"],
            f"{selected_pref}の店舗数": pref_count,
            "総店舗数（全国）": total,
            "地域比率": f"{ratio*100:.1f}%",
            "_ratio": ratio,
            "_pref_count": pref_count,
        })

# ── 結果表示 ──────────────────────────────────────────────────────────────────
st.subheader(f"📍 {selected_pref} の検索結果")

if not rows:
    st.warning(
        f"条件を満たす企業が見つかりませんでした。\n\n"
        f"条件: {selected_pref}内に **{min_stores}店舗以上** かつ **総店舗数の{min_ratio}%以上**\n\n"
        f"・データ未取得の企業がある場合は「全社データ取得」を実行してください。\n"
        f"・条件を緩和して再検索することもできます。"
    )
else:
    df = pd.DataFrame(rows).sort_values("_pref_count", ascending=False)

    # 件数サマリー
    sm_cnt = sum(1 for r in rows if r["業態"] == "SM")
    dgs_cnt = sum(1 for r in rows if r["業態"] == "DGS")
    c1, c2, c3 = st.columns(3)
    c1.metric("ヒット企業数", f"{len(rows)} 社")
    c2.metric("うち SM", f"{sm_cnt} 社")
    c3.metric("うち DGS", f"{dgs_cnt} 社")

    # 表示用 DataFrame
    display_cols = [
        "企業名", "業態",
        f"{selected_pref}の店舗数", "総店舗数（全国）", "地域比率",
    ]
    st.dataframe(
        df[display_cols].reset_index(drop=True),
        use_container_width=True,
        hide_index=True,
        column_config={
            "業態": st.column_config.TextColumn(width="small"),
            f"{selected_pref}の店舗数": st.column_config.NumberColumn(width="medium"),
            "総店舗数（全国）": st.column_config.NumberColumn(width="medium"),
            "地域比率": st.column_config.TextColumn(width="small"),
        },
    )

    # CSVダウンロード
    csv = df[display_cols].to_csv(index=False, encoding="utf-8-sig")
    st.download_button(
        "📥 CSVダウンロード",
        data=csv,
        file_name=f"営業リスト_{selected_pref}.csv",
        mime="text/csv",
    )

# ── データ未取得企業の一覧 ────────────────────────────────────────────────────
with st.expander("⚠️ データ未取得・取得失敗の企業"):
    not_found = [
        c["name"] for c in COMPANIES
        if not cached_data.get(c["name"])
        or cached_data[c["name"]]["status"] == "not_found"
    ]
    if not_found:
        st.write(f"{len(not_found)} 社のデータが未取得または取得失敗です:")
        st.write("\n".join(f"- {n}" for n in not_found))
    else:
        st.write("すべての企業のデータを取得済みです。")

