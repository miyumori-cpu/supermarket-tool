"""
各企業の都道府県別店舗数をWebから収集するモジュール。

戦略（優先順）:
1. ajsm_urls.py のURLマッピングから直接アクセス → 「都道府県名(N)」形式パース
2. マッピングがない場合は DuckDuckGo 検索で ajsm.jp ページを探す
3. ajsm.jp に見つからなければ一般検索でスニペットからデータ抽出
4. 結果はキャッシュ保存
"""

from __future__ import annotations

import json
import os
import re
import time
import hashlib
from urllib.parse import quote, unquote

import requests
from bs4 import BeautifulSoup

from companies import PREFECTURES, PREF_SHORT
from ajsm_urls import get_ajsm_url

CACHE_DIR = os.path.join(os.path.dirname(__file__), "cache")

# ajsm.jp へのアクセス用セッション（Cookieを保持）
_AJSM_SESSION = None
_LAST_REQUEST_TIME = 0.0
_MIN_INTERVAL = 2.5  # 秒

BASE_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ja,en-US;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
}

# 都道府県マッチング用
_PREF_PATTERNS = [
    ("北海道", "北海道"),
    ("青森", "青森県"), ("岩手", "岩手県"), ("宮城", "宮城県"), ("秋田", "秋田県"),
    ("山形", "山形県"), ("福島", "福島県"), ("茨城", "茨城県"), ("栃木", "栃木県"),
    ("群馬", "群馬県"), ("埼玉", "埼玉県"), ("千葉", "千葉県"),
    ("東京", "東京都"), ("神奈川", "神奈川県"), ("新潟", "新潟県"), ("富山", "富山県"),
    ("石川", "石川県"), ("福井", "福井県"), ("山梨", "山梨県"), ("長野", "長野県"),
    ("岐阜", "岐阜県"), ("静岡", "静岡県"), ("愛知", "愛知県"), ("三重", "三重県"),
    ("滋賀", "滋賀県"), ("京都", "京都府"), ("大阪", "大阪府"), ("兵庫", "兵庫県"),
    ("奈良", "奈良県"), ("和歌山", "和歌山県"), ("鳥取", "鳥取県"), ("島根", "島根県"),
    ("岡山", "岡山県"), ("広島", "広島県"), ("山口", "山口県"), ("徳島", "徳島県"),
    ("香川", "香川県"), ("愛媛", "愛媛県"), ("高知", "高知県"), ("福岡", "福岡県"),
    ("佐賀", "佐賀県"), ("長崎", "長崎県"), ("熊本", "熊本県"), ("大分", "大分県"),
    ("宮崎", "宮崎県"), ("鹿児島", "鹿児島県"), ("沖縄", "沖縄県"),
]

# ── キャッシュ ────────────────────────────────────────────────────────────────

def _cache_path(company_name: str) -> str:
    h = hashlib.md5(company_name.encode()).hexdigest()[:12]
    return os.path.join(CACHE_DIR, f"{h}.json")


def load_cache(company_name: str):
    path = _cache_path(company_name)
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return None


def save_cache(company_name: str, data: dict) -> None:
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(_cache_path(company_name), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def clear_cache(company_name: str) -> None:
    path = _cache_path(company_name)
    if os.path.exists(path):
        os.remove(path)


# ── HTTP ─────────────────────────────────────────────────────────────────────

def _get_ajsm_session() -> requests.Session:
    global _AJSM_SESSION
    if _AJSM_SESSION is None:
        _AJSM_SESSION = requests.Session()
        _AJSM_SESSION.headers.update(BASE_HEADERS)
        # トップページにアクセスしてCookieを取得
        try:
            _AJSM_SESSION.get("https://www.ajsm.jp/", timeout=10)
            time.sleep(1.0)
        except Exception:
            pass
    return _AJSM_SESSION


def _rate_limited_get(url: str, is_ajsm: bool = True, max_retries: int = 2) -> str:
    """レート制限付きHTTPアクセス。"""
    global _LAST_REQUEST_TIME

    if is_ajsm:
        elapsed = time.time() - _LAST_REQUEST_TIME
        if elapsed < _MIN_INTERVAL:
            time.sleep(_MIN_INTERVAL - elapsed)
        session = _get_ajsm_session()
        headers = {"Referer": "https://www.ajsm.jp/"}
    else:
        session = requests.Session()
        session.headers.update(BASE_HEADERS)
        headers = {}

    for attempt in range(max_retries + 1):
        try:
            _LAST_REQUEST_TIME = time.time()
            resp = session.get(url, headers=headers, timeout=14)

            if resp.status_code == 403:
                if attempt < max_retries:
                    time.sleep(5 * (attempt + 1))
                    continue
                return ""
            if resp.status_code != 200:
                return ""

            resp.encoding = resp.apparent_encoding or "utf-8"
            soup = BeautifulSoup(resp.text, "lxml")
            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()
            return soup.get_text(" ", strip=True)

        except Exception:
            if attempt < max_retries:
                time.sleep(3)
    return ""


# ── テキスト解析 ──────────────────────────────────────────────────────────────

def _extract_pref_counts(text: str) -> dict[str, int]:
    """テキストから都道府県別店舗数を抽出する。"""
    counts: dict[str, int] = {}

    # パターン1: 「東京都(93)」形式 (ajsm.jp)
    pat_paren = re.compile(
        r"(北海道|青森|岩手|宮城|秋田|山形|福島|茨城|栃木|群馬|埼玉|千葉|東京|神奈川"
        r"|新潟|富山|石川|福井|山梨|長野|岐阜|静岡|愛知|三重|滋賀|京都|大阪|兵庫|奈良|和歌山"
        r"|鳥取|島根|岡山|広島|山口|徳島|香川|愛媛|高知"
        r"|福岡|佐賀|長崎|熊本|大分|宮崎|鹿児島|沖縄)"
        r"[都道府県]?\s*[（(]\s*(\d+)\s*[)）]"
    )
    for m in pat_paren.finditer(text):
        short = m.group(1)
        n = int(m.group(2))
        pref = PREF_SHORT.get(short, short)
        if n > 0:
            counts[pref] = max(counts.get(pref, 0), n)

    # パターン2: 「東京都：15店」「東京都 15店舗」
    if not counts:
        pat_colon = re.compile(
            r"(北海道|青森|岩手|宮城|秋田|山形|福島|茨城|栃木|群馬|埼玉|千葉|東京|神奈川"
            r"|新潟|富山|石川|福井|山梨|長野|岐阜|静岡|愛知|三重|滋賀|京都|大阪|兵庫|奈良|和歌山"
            r"|鳥取|島根|岡山|広島|山口|徳島|香川|愛媛|高知"
            r"|福岡|佐賀|長崎|熊本|大分|宮崎|鹿児島|沖縄)"
            r"[都道府県]?\s*[：:\s]\s*(\d+)\s*店"
        )
        for m in pat_colon.finditer(text):
            short = m.group(1)
            n = int(m.group(2))
            pref = PREF_SHORT.get(short, short)
            if n > 0:
                counts[pref] = max(counts.get(pref, 0), n)

    return counts


def _extract_total(text: str) -> int:
    """総店舗数を抽出する。"""
    patterns = [
        r"【店舗数】\s*(\d{2,4})\s*店",
        r"店舗数\s*[】\]）)：:]\s*(\d{2,4})\s*店",
        r"全国\s*(\d{2,4})\s*店",
        r"(\d{2,4})\s*店舗\s*[をを]?\s*展開",
        r"合計\s*(\d{2,4})\s*店",
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            n = int(m.group(1))
            if 3 <= n <= 9999:
                return n
    return 0


# ── DuckDuckGo 検索 ───────────────────────────────────────────────────────────

def _ddg_search(query: str, max_results: int = 5) -> list[dict]:
    url = f"https://html.duckduckgo.com/html/?q={quote(query)}&kl=jp-jp"
    try:
        session = requests.Session()
        session.headers.update(BASE_HEADERS)
        resp = session.get(url, timeout=14)
        if resp.status_code != 200:
            return []
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        for r in soup.select(".result__body")[:max_results]:
            a = r.select_one(".result__a")
            s = r.select_one(".result__snippet")
            if not a:
                continue
            raw = a.get("href", "")
            m = re.search(r"uddg=([^&]+)", raw)
            real_url = unquote(m.group(1)) if m else raw
            results.append({
                "title": a.get_text(strip=True),
                "url": real_url,
                "snippet": s.get_text(strip=True) if s else "",
            })
        return results
    except Exception:
        return []


# ── メイン ────────────────────────────────────────────────────────────────────

def fetch_company_data(company_name: str, short_name: str, force: bool = False) -> dict:
    """
    企業の店舗データを取得して返す。

    戻り値:
        {
            "total": int,
            "by_prefecture": {都道府県名: 店舗数, ...},
            "status": "ok" | "partial" | "not_found",
            "source": str,
        }
    """
    if not force:
        cached = load_cache(company_name)
        if cached:
            return cached

    result = {
        "total": 0,
        "by_prefecture": {},
        "status": "not_found",
        "source": "",
    }

    # ── Step 1: ajsm.jp URLマッピングから直接取得 ────────────────
    ajsm_url = get_ajsm_url(company_name)
    if ajsm_url:
        text = _rate_limited_get(ajsm_url, is_ajsm=True)
        if text and "403" not in text[:50]:
            pref_counts = _extract_pref_counts(text)
            total = _extract_total(text)
            if pref_counts:
                result.update({
                    "total": total or sum(pref_counts.values()),
                    "by_prefecture": pref_counts,
                    "status": "ok",
                    "source": ajsm_url,
                })
                save_cache(company_name, result)
                return result
            elif total > 0:
                result["total"] = total
                result["status"] = "partial"
                result["source"] = ajsm_url

    # ── Step 2: DuckDuckGo で ajsm.jp ページを検索 ───────────────
    if result["status"] != "ok":
        queries = [
            f"ajsm.jp {short_name} 基礎情報 店舗一覧",
            f"{short_name} ajsm 都道府県別 店舗数",
        ]
        for query in queries:
            results = _ddg_search(query, max_results=5)
            time.sleep(1.5)

            for r in results:
                url = r["url"]
                # スニペットから抽出
                snippet_counts = _extract_pref_counts(r["snippet"])
                if snippet_counts:
                    result["by_prefecture"].update(snippet_counts)
                    result["source"] = url

                # ajsm.jpページなら本体もアクセス
                if "ajsm.jp" in url and re.search(r"/[a-zA-Z].*\.(html|htm)$", url):
                    text = _rate_limited_get(url, is_ajsm=True)
                    page_counts = _extract_pref_counts(text)
                    if page_counts:
                        result["by_prefecture"].update(page_counts)
                        t = _extract_total(text)
                        if t:
                            result["total"] = t
                        result["source"] = url

            if result["by_prefecture"]:
                break

    # ── Step 3: 総店舗数の補完 ───────────────────────────────────
    if result["total"] == 0:
        for query in [f"{short_name} 総店舗数 全国", f"{short_name} 店舗数 {company_name}"]:
            for r in _ddg_search(query, max_results=3):
                t = _extract_total(r["snippet"])
                if t:
                    result["total"] = t
                    break
            if result["total"]:
                break
            time.sleep(1.0)

    # 都道府県合計で補完
    if result["total"] == 0 and result["by_prefecture"]:
        result["total"] = sum(result["by_prefecture"].values())

    # ステータス決定
    if result["by_prefecture"]:
        result["status"] = "ok"
    elif result["total"] > 0:
        result["status"] = "partial"

    save_cache(company_name, result)
    return result
