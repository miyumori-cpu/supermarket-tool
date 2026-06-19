"""
ajsm.jp の企業・ブランド別店舗一覧ページURL マッピング。
ブランドページ(.html) を優先、なければ企業ページ(.htm) を使用。
"""
from __future__ import annotations

# key: COMPANIES の name フィールド → value: ajsm.jp のパス
AJSM_URL_MAP = {
    # ── SM ────────────────────────────────────────────────────────────────────
    "サミット株式会社":                                         "summitstore.html",
    "株式会社西友":                                             "seiyu.html",
    "株式会社イトーヨーカ堂":                                   "itoyokado.html",
    "株式会社神戸物産":                                         "kobebussan.html",
    "株式会社ローソンストア１００":                             "lawsonstore100.html",
    "株式会社パン・パシフィック・インターナショナルホールディングス": "donki.html",
    "オーケー株式会社":                                         "ok.html",
    "株式会社平和堂":                                           "heiwado.html",
    "株式会社ヨークベニマル":                                   "yorkbeni.html",
    "株式会社万代":                                             "mandai.html",
    "株式会社コノミヤ":                                         "konomiya.html",
    "株式会社エコス":                                           "ecosCorp.htm",
    "株式会社たいらや":                                         "ecosTAIRAYA.html",
    "株式会社フレスタ":                                         "fresta.html",
    "株式会社フィールコーポレーション":                         "feel.html",
    "株式会社東急ストア":                                       "tokyustor.html",
    "株式会社フレッセイ":                                       "fressay.html",
    "株式会社いなげや":                                         "inageya.html",
    "株式会社ラルズ":                                           "arcs-ralseCorp.htm",
    "株式会社ベイシア":                                         "beisiaCorp.htm",
    "株式会社ダイエー":                                         "daieiSM-AEON.html",
    "株式会社オークワ":                                         "ookuwa.html",
    "株式会社成城石井":                                         "seijoishiiCorp.htm",
    "株式会社トライアルカンパニー":                             "trial-Center.html",
    "イオン北海道株式会社":                                     "aeonhokkaidoCorp.htm",
    "イオン東北株式会社":                                       "aeontohokuCorp.htm",
    "イオン九州株式会社":                                       "aeonkyusyuCorp.htm",
    "イオンマーケット株式会社":                                 "AEON-marketCorp.htm",
    "イオンリテール株式会社 西日本カンパニー":                  "aeonretailCorp.htm",
    "イオンリテール株式会社 南関東カンパニー":                  "aeonretailCorp.htm",
    "イオンリテール株式会社 北関東・新潟カンパニー":            "aeonretailCorp.htm",
    "イオンリテール株式会社 中部カンパニー":                    "aeonretailCorp.htm",
    "イオンビッグ株式会社":                                     "aeonretailCorp.htm",
    "イオンフードスタイル株式会社":                             "aeonretailCorp.htm",
    "株式会社イオンフードスタイル":                             "aeonretailCorp.htm",
    "生活協同組合コープこうべ":                                 "kobecoopCorp.htm",
    "株式会社ワイズマート":                                     "ysmart.html",
    "株式会社京成ストア":                                       "keiseiCorp.htm",
    "株式会社オザム":                                           "superozam.html",
    "相鉄ローゼン株式会社":                                     "sotetsu.rosenCorp.htm",
    "株式会社ライフコーポレーション（近畿圏）":                 "life.html",
    "株式会社ライフコーポレーション（首都圏）":                 "life.html",
    "株式会社イズミ":                                           "izumiyumetown.html",
    "株式会社アオキスーパー":                                   "aoki.html",
    "原信ナルスオペレーションサービス株式会社":                 "harashin.html",
    "株式会社とりせん":                                         "torisen.html",
    "株式会社ウオロク":                                         "uoroku.html",
    "株式会社オオゼキ":                                         "oozeki.html",
    "株式会社三和":                                             "sanwa.html",
    "株式会社ジャパンミート":                                   "japanmeat-oroshi.html",
    "株式会社ドミー":                                           "domyCorp.htm",
    "株式会社道東アークス":                                     "arcs-ralseCorp.htm",
    "株式会社道北アークス":                                     "arcs-ralseCorp.htm",
    "株式会社セイコーマート":                                   "acoop-seikomart.html",
    "株式会社ゆめマート熊本":                                   "izumiyumetown.html",
    "株式会社ゆめマート北九州":                                 "izumiyumetown.html",
    "株式会社ビッグ・エー":                                     "big-a.html",
    "株式会社マルト商事":                                       "maruto.html",

    # ── DGS ───────────────────────────────────────────────────────────────────
    "スギホールディングス株式会社":                             "drug-sugi.html",
    "株式会社サンドラッグ":                                     "sundrug.html",
    "ダイレックス株式会社":                                     "ds-direx.html",
    "株式会社ツルハ":                                           "tsuruhadr.html",
    "株式会社スギヤマ薬品":                                     "sugiyamaCorp.htm",
    "株式会社杏林堂薬局":                                       "kyorindoCorp.htm",
    "株式会社ユタカファーマシー":                               "d-yutakaCorp.htm",
}

BASE_URL = "https://www.ajsm.jp/"


def get_ajsm_url(company_name: str) -> str | None:
    path = AJSM_URL_MAP.get(company_name)
    if path:
        return BASE_URL + path
    return None
