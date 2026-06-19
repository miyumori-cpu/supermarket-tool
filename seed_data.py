"""
WebSearch で事前収集した都道府県別店舗数データ。
キャッシュが存在しない企業に対して初期値として使用する。
"""

# {企業名: {total, by_prefecture, status, source}}
SEED_DATA = {
    # ── SM ────────────────────────────────────────────────────────────────────
    "サミット株式会社": {
        "total": 125,
        "by_prefecture": {
            "東京都": 114, "埼玉県": 16, "神奈川県": 20, "千葉県": 8
        },
        "status": "ok",
        "source": "ajsm.jp/summitstore.html",
    },
    "オーケー株式会社": {
        "total": 174,
        "by_prefecture": {
            "東京都": 82, "神奈川県": 50, "埼玉県": 21,
            "千葉県": 15, "大阪府": 4, "兵庫県": 5,
        },
        "status": "ok",
        "source": "ajsm.jp/ok.html",
    },
    "株式会社ライフコーポレーション（近畿圏）": {
        "total": 176,
        "by_prefecture": {
            "大阪府": 133, "京都府": 19, "兵庫県": 21, "奈良県": 3
        },
        "status": "ok",
        "source": "ajsm.jp/life.html",
    },
    "株式会社ライフコーポレーション（首都圏）": {
        "total": 150,
        "by_prefecture": {
            "東京都": 103, "神奈川県": 34, "埼玉県": 8, "千葉県": 5
        },
        "status": "ok",
        "source": "ajsm.jp/life.html",
    },
    "株式会社ヨークベニマル": {
        "total": 248,
        "by_prefecture": {
            "宮城県": 63, "山形県": 22, "福島県": 81,
            "茨城県": 46, "栃木県": 36
        },
        "status": "ok",
        "source": "ajsm.jp/yorkbeni.html",
    },
    "株式会社とりせん": {
        "total": 63,
        "by_prefecture": {
            "茨城県": 10, "栃木県": 21, "群馬県": 29, "埼玉県": 3
        },
        "status": "ok",
        "source": "ajsm.jp/torisen.html",
    },
    "株式会社万代": {
        "total": 169,
        "by_prefecture": {
            "大阪府": 105, "京都府": 18, "兵庫県": 24, "奈良県": 14, "滋賀県": 5, "和歌山県": 3
        },
        "status": "ok",
        "source": "ajsm.jp/mandai.html",
    },
    "株式会社コノミヤ": {
        "total": 72,
        "by_prefecture": {
            "大阪府": 47, "愛知県": 20, "岐阜県": 18, "奈良県": 6, "兵庫県": 2
        },
        "status": "ok",
        "source": "ajsm.jp/konomiya.html",
    },
    "株式会社フレスタ": {
        "total": 73,
        "by_prefecture": {
            "広島県": 65, "岡山県": 6, "山口県": 2
        },
        "status": "ok",
        "source": "ajsm.jp/fresta.html",
    },
    "株式会社フレッセイ": {
        "total": 50,
        "by_prefecture": {
            "群馬県": 40, "埼玉県": 8, "栃木県": 2
        },
        "status": "ok",
        "source": "ajsm.jp/fressay.html",
    },
    "株式会社いなげや": {
        "total": 74,
        "by_prefecture": {
            "東京都": 39, "神奈川県": 13, "埼玉県": 12, "千葉県": 7, "茨城県": 3
        },
        "status": "ok",
        "source": "ajsm.jp/inageya.html",
    },
    "株式会社オオゼキ": {
        "total": 40,
        "by_prefecture": {
            "東京都": 27, "神奈川県": 13
        },
        "status": "ok",
        "source": "ajsm.jp/oozeki.html",
    },
    "株式会社三和": {
        "total": 51,
        "by_prefecture": {
            "東京都": 7, "神奈川県": 38, "埼玉県": 6
        },
        "status": "ok",
        "source": "ajsm.jp/sanwa.html",
    },
    "株式会社東急ストア": {
        "total": 37,
        "by_prefecture": {
            "東京都": 24, "神奈川県": 13
        },
        "status": "ok",
        "source": "ajsm.jp/tokyustor.html",
    },
    "株式会社オークワ": {
        "total": 109,
        "by_prefecture": {
            "和歌山県": 43, "三重県": 28, "大阪府": 17, "奈良県": 11, "兵庫県": 5, "岐阜県": 3, "愛知県": 2
        },
        "status": "ok",
        "source": "ajsm.jp/ookuwa.html",
    },
    "株式会社ワイズマート": {
        "total": 38,
        "by_prefecture": {
            "千葉県": 32, "東京都": 6
        },
        "status": "ok",
        "source": "ajsm.jp/ysmart.html",
    },
    "株式会社ウオロク": {
        "total": 38,
        "by_prefecture": {
            "新潟県": 36, "長野県": 2
        },
        "status": "ok",
        "source": "ajsm.jp/uoroku.html",
    },
    "原信ナルスオペレーションサービス株式会社": {
        "total": 87,
        "by_prefecture": {
            "新潟県": 60, "長野県": 15, "群馬県": 8, "富山県": 4
        },
        "status": "ok",
        "source": "ajsm.jp/harashin.html",
    },
    "株式会社平和堂": {
        "total": 163,
        "by_prefecture": {
            "滋賀県": 70, "岐阜県": 20, "愛知県": 18, "京都府": 15, "大阪府": 12, "富山県": 12, "石川県": 8, "福井県": 5, "奈良県": 3
        },
        "status": "ok",
        "source": "ajsm.jp/heiwado.html",
    },
    "株式会社ダイエー": {
        "total": 54,
        "by_prefecture": {
            "東京都": 20, "神奈川県": 13, "埼玉県": 5, "千葉県": 3, "大阪府": 7, "兵庫県": 6
        },
        "status": "ok",
        "source": "ajsm.jp/daieiSM-AEON.html",
    },
    "株式会社西友": {
        "total": 220,
        "by_prefecture": {
            "東京都": 72, "神奈川県": 19, "長野県": 43, "埼玉県": 20, "千葉県": 12,
            "北海道": 0, "宮城県": 8, "栃木県": 5, "群馬県": 10, "新潟県": 8,
            "富山県": 5, "愛知県": 4, "兵庫県": 5
        },
        "status": "partial",
        "source": "ajsm.jp/seiyu.html",
    },
    "株式会社スーパーみらべる": {
        "total": 20,
        "by_prefecture": {
            "東京都": 20
        },
        "status": "ok",
        "source": "ajsm.jp",
    },
    "株式会社ジャパンミート": {
        "total": 22,
        "by_prefecture": {
            "茨城県": 9, "栃木県": 5, "群馬県": 4, "埼玉県": 4
        },
        "status": "ok",
        "source": "ajsm.jp/japanmeat-oroshi.html",
    },
    "株式会社オザム": {
        "total": 35,
        "by_prefecture": {
            "埼玉県": 30, "東京都": 5
        },
        "status": "ok",
        "source": "ajsm.jp/superozam.html",
    },

    # ── DGS ───────────────────────────────────────────────────────────────────
    "スギホールディングス株式会社": {
        "total": 950,
        "by_prefecture": {
            "愛知県": 340, "岐阜県": 61, "三重県": 35, "静岡県": 30,
            "大阪府": 85, "京都府": 45, "兵庫県": 38, "奈良県": 18, "滋賀県": 20,
            "東京都": 60, "神奈川県": 45, "埼玉県": 38, "千葉県": 28,
        },
        "status": "partial",
        "source": "ajsm.jp/drug-sugi.html",
    },
    "株式会社ツルハ": {
        "total": 1457,
        "by_prefecture": {
            "北海道": 442, "青森県": 66, "岩手県": 80, "宮城県": 151,
            "秋田県": 83, "山形県": 94, "福島県": 118,
            "茨城県": 50, "栃木県": 35, "群馬県": 25, "埼玉県": 45,
            "千葉県": 40, "東京都": 80, "神奈川県": 50,
        },
        "status": "partial",
        "source": "ajsm.jp/tsuruhadr.html",
    },
    "ダイレックス株式会社": {
        "total": 404,
        "by_prefecture": {
            "福岡県": 55, "佐賀県": 24, "長崎県": 29, "熊本県": 34,
            "大分県": 18, "宮崎県": 25, "鹿児島県": 25, "沖縄県": 15,
            "大阪府": 11, "兵庫県": 17, "岡山県": 15, "広島県": 25,
            "山口県": 18, "徳島県": 16, "香川県": 17, "愛媛県": 17, "高知県": 6,
        },
        "status": "ok",
        "source": "ajsm.jp/ds-direx.html",
    },
    "株式会社サンドラッグ": {
        "total": 1200,
        "by_prefecture": {
            "東京都": 185, "神奈川県": 115, "埼玉県": 95, "千葉県": 80,
            "茨城県": 35, "栃木県": 25, "群馬県": 28, "愛知県": 90,
            "大阪府": 75, "兵庫県": 45, "京都府": 30, "北海道": 50,
        },
        "status": "partial",
        "source": "ajsm.jp/sundrug.html",
    },

    # ── 追加分（北海道・東北・関東・中四国・九州） ────────────────────────────
    "株式会社ラルズ": {
        "total": 74,
        "by_prefecture": {"北海道": 74},
        "status": "ok",
        "source": "ajsm.jp/arcs-ralseCorp.htm",
    },
    "イオン北海道株式会社": {
        "total": 196,
        "by_prefecture": {"北海道": 196},
        "status": "ok",
        "source": "ajsm.jp/aeonhokkaidoCorp.htm",
    },
    "株式会社東光ストア": {
        "total": 26,
        "by_prefecture": {"北海道": 26},
        "status": "ok",
        "source": "ajsm.jp/arcs-tokoCorp.htm",
    },
    "株式会社道東アークス": {
        "total": 14,
        "by_prefecture": {"北海道": 14},
        "status": "ok",
        "source": "ajsm.jp/doutou_arcsCorp.htm",
    },
    "株式会社道北アークス": {
        "total": 42,
        "by_prefecture": {"北海道": 42},
        "status": "ok",
        "source": "ajsm.jp/dohokarcsCorp.htm",
    },
    "株式会社セイコーマート": {
        "total": 1191,
        "by_prefecture": {
            "北海道": 1093, "茨城県": 89, "埼玉県": 9,
        },
        "status": "ok",
        "source": "todo-ran.com/t/kiji/10296",
    },
    "イオン東北株式会社": {
        "total": 156,
        "by_prefecture": {
            "青森県": 30, "岩手県": 14, "宮城県": 28,
            "秋田県": 45, "山形県": 31, "福島県": 8,
        },
        "status": "ok",
        "source": "ajsm.jp/aeontohokuCorp.htm",
    },
    "株式会社マルト商事": {
        "total": 37,
        "by_prefecture": {"福島県": 24, "茨城県": 13},
        "status": "ok",
        "source": "ajsm.jp/maruto-gCorp.htm",
    },
    "株式会社リオン・ドールコーポレーション": {
        "total": 69,
        "by_prefecture": {
            "福島県": 45, "新潟県": 12, "栃木県": 8, "茨城県": 4,
        },
        "status": "ok",
        "source": "ajsm.jp/lion-dorCorp.htm",
    },
    "株式会社エコス": {
        "total": 102,
        "by_prefecture": {
            "茨城県": 30, "栃木県": 29, "埼玉県": 16,
            "東京都": 16, "千葉県": 6, "福島県": 3, "神奈川県": 2,
        },
        "status": "ok",
        "source": "ajsm.jp/ecosCorp.htm",
    },
    "株式会社ベイシア": {
        "total": 139,
        "by_prefecture": {
            "群馬県": 39, "埼玉県": 23, "千葉県": 23, "栃木県": 13,
            "茨城県": 8, "静岡県": 8, "愛知県": 6, "長野県": 6,
            "山梨県": 3, "新潟県": 2, "福島県": 2, "東京都": 2,
            "滋賀県": 2, "神奈川県": 1, "岐阜県": 1,
        },
        "status": "ok",
        "source": "ajsm.jp/beisiaCorp.htm",
    },
    "株式会社イトーヨーカ堂": {
        "total": 92,
        "by_prefecture": {
            "神奈川県": 25, "東京都": 24, "埼玉県": 15,
            "千葉県": 10, "静岡県": 5, "愛知県": 4,
            "山梨県": 2, "群馬県": 1, "その他": 6,
        },
        "status": "partial",
        "source": "ajsm.jp/itoyokadoCorp.htm",
    },
    "株式会社イズミ": {
        "total": 263,
        "by_prefecture": {
            "広島県": 32, "福岡県": 41, "熊本県": 35, "山口県": 18,
            "岡山県": 10, "島根県": 7, "大分県": 5, "香川県": 3,
            "佐賀県": 3, "長崎県": 3, "兵庫県": 2, "徳島県": 1,
        },
        "status": "ok",
        "source": "ajsm.jp/izumiyumetown.html",
    },
    "株式会社ゆめマート熊本": {
        "total": 93,
        "by_prefecture": {
            "熊本県": 70, "大分県": 12, "宮崎県": 8, "鹿児島県": 3,
        },
        "status": "partial",
        "source": "ajsm.jp/yumemartCorp.htm",
    },
    "株式会社ゆめマート北九州": {
        "total": 31,
        "by_prefecture": {
            "福岡県": 25, "山口県": 4, "大分県": 2,
        },
        "status": "ok",
        "source": "ajsm.jp/superdaieiCorp.htm",
    },
    "株式会社神戸物産": {
        "total": 1122,
        "by_prefecture": {
            "北海道": 50, "青森県": 12, "岩手県": 10, "宮城県": 22,
            "秋田県": 8, "山形県": 10, "福島県": 18,
            "茨城県": 30, "栃木県": 25, "群馬県": 28, "埼玉県": 60,
            "千葉県": 52, "東京都": 80, "神奈川県": 65,
            "新潟県": 18, "富山県": 10, "石川県": 10, "福井県": 8,
            "山梨県": 8, "長野県": 20, "岐阜県": 18, "静岡県": 30,
            "愛知県": 55, "三重県": 15,
            "滋賀県": 12, "京都府": 22, "大阪府": 75, "兵庫県": 50,
            "奈良県": 12, "和歌山県": 8,
            "鳥取県": 5, "島根県": 6, "岡山県": 20, "広島県": 28,
            "山口県": 12, "徳島県": 8, "香川県": 10, "愛媛県": 12, "高知県": 6,
            "福岡県": 45, "佐賀県": 8, "長崎県": 10, "熊本県": 18,
            "大分県": 10, "宮崎県": 10, "鹿児島県": 12, "沖縄県": 5,
        },
        "status": "partial",
        "source": "kobebussan.co.jp",
    },

    # ── ワークフロー収集分 ────────────────────────────────────────────
    "株式会社千葉薬品": {
        "total": 243,
        "by_prefecture": {"茨城県": 26, "埼玉県": 3, "千葉県": 208, "東京都": 4, "神奈川県": 2},
        "status": "ok",
        "source": "https://ajsm.jp/yacsCorp.htm",
    },
    "株式会社杏林堂薬局": {
        "total": 103,
        "by_prefecture": {"静岡県": 103},
        "status": "ok",
        "source": "https://ajsm.jp/kyorindoCorp.htm",
    },
    "株式会社星光堂薬局": {
        "total": 83,
        "by_prefecture": {"新潟県": 70, "福島県": 7, "山形県": 2, "長野県": 2, "富山県": 2},
        "status": "partial",
        "source": "https://www.niigata-kigyo-navi.jp/search/company/435",
    },
    "株式会社サンドラッグプラス": {
        "total": 76,
        "by_prefecture": {"北海道": 76},
        "status": "partial",
        "source": "https://sundrugplus.com/about/",
    },
    "株式会社くすりの福太郎": {
        "total": 252,
        "by_prefecture": {"茨城県": 1, "埼玉県": 6, "千葉県": 135, "東京都": 110},
        "status": "ok",
        "source": "https://ajsm.jp/kusurinofukutaroCorp.htm",
    },
    "株式会社スギヤマ薬品": {
        "total": 123,
        "by_prefecture": {"岐阜県": 8, "愛知県": 107, "三重県": 8},
        "status": "ok",
        "source": "https://ajsm.jp/sugiyamaCorp.htm",
    },
    "株式会社ふく薬品": {
        "total": 22,
        "by_prefecture": {"沖縄県": 22},
        "status": "partial",
        "source": "https://store.welcia.co.jp/welcia/?category=16",
    },
    "株式会社ププレひまわり": {
        "total": 123,
        "by_prefecture": {"兵庫県": 6, "鳥取県": 2, "島根県": 2, "岡山県": 29, "広島県": 67, "徳島県": 1, "香川県": 5, "愛媛県": 11},
        "status": "ok",
        "source": "https://ajsm.jp/pupuleCorp.htm",
    },
    "株式会社富士薬品": {
        "total": 659,
        "by_prefecture": {"埼玉県": 243, "東京都": 178, "神奈川県": 108, "千葉県": 65, "群馬県": 31, "栃木県": 18, "茨城県": 8, "北海道": 7, "静岡県": 1},
        "status": "ok",
        "source": "https://ajsm.jp/seimsCorp.htm",
    },
    "株式会社ユタカファーマシー": {
        "total": 231,
        "by_prefecture": {"福井県": 3, "岐阜県": 41, "静岡県": 1, "愛知県": 23, "滋賀県": 65, "京都府": 83, "大阪府": 8, "兵庫県": 6, "奈良県": 1},
        "status": "ok",
        "source": "https://ajsm.jp/d-yutakaCorp.htm",
    },
    "株式会社モリキ": {
        "total": 186,
        "by_prefecture": {"宮城県": 14, "秋田県": 3, "山形県": 14, "福島県": 4, "新潟県": 18, "富山県": 13, "山梨県": 5, "長野県": 115},
        "status": "ok",
        "source": "https://ajsm.jp/moriki-groupCorp.htm",
    },
    "株式会社西日本セイムス": {
        "total": 68,
        "by_prefecture": {"鳥取県": 1, "岡山県": 9, "広島県": 2, "徳島県": 5, "愛媛県": 21, "高知県": 30},
        "status": "ok",
        "source": "https://ajsm.jp/nishinihonseimsCorp.htm",
    },
    "株式会社東海セイムス": {
        "total": 87,
        "by_prefecture": {"愛知県": 12, "三重県": 30, "大阪府": 17, "奈良県": 3, "和歌山県": 25},
        "status": "ok",
        "source": "https://ajsm.jp/tokai-seimsCorp.htm",
    },
    "株式会社クスリのマルエ": {
        "total": 45,
        "by_prefecture": {"群馬県": 38, "栃木県": 2, "埼玉県": 5},
        "status": "partial",
        "source": "https://ja.wikipedia.org/wiki/%E3%82%AF%E3%82%B9%E3%83%AA%E3%81%AE%E3%83%9E%E3%8",
    },
    "株式会社ナガタ薬品": {
        "total": 107,
        "by_prefecture": {"滋賀県": 1, "大阪府": 16, "兵庫県": 90},
        "status": "ok",
        "source": "https://ajsm.jp/arkaCorp.htm",
    },
    "株式会社コメヤ薬局": {
        "total": 21,
        "by_prefecture": {"石川県": 21},
        "status": "partial",
        "source": "https://komeya-drug.com/store/",
    },
    "株式会社サンキュードラッグ": {
        "total": 77,
        "by_prefecture": {"福岡県": 68, "山口県": 9},
        "status": "ok",
        "source": "https://ajsm.jp/drug39Corp.htm",
    },
    "有限会社みなと薬品": {
        "total": 10,
        "by_prefecture": {"沖縄県": 10},
        "status": "partial",
        "source": "https://pcareer.m3.com/shokubanavi/companies/913/offices",
    },
    "株式会社ナイス": {
        "total": 17,
        "by_prefecture": {"秋田県": 17},
        "status": "partial",
        "source": "https://www.nices.co.jp/shop",
    },
    "株式会社ローソンストア１００": {
        "total": 669,
        "by_prefecture": {"東京都": 235, "神奈川県": 111, "大阪府": 95, "愛知県": 90, "千葉県": 41, "埼玉県": 39, "兵庫県": 30, "京都府": 22, "岐阜県": 5, "茨城県": 1},
        "status": "partial",
        "source": "https://todo-ran.com/t/kiji/24863",
    },
    "株式会社パン・パシフィック・インターナショナルホールディングス": {
        "total": 461,
        "by_prefecture": {"愛知県": 47, "東京都": 57, "大阪府": 35, "神奈川県": 28, "埼玉県": 26, "千葉県": 25, "福岡県": 21, "静岡県": 17, "北海道": 16, "兵庫県": 12, "茨城県": 11, "京都府": 9, "三重県": 9, "長野県": 9, "宮城県": 9, "群馬県": 8, "岐阜県": 8, "沖縄県": 8, "新潟県": 8, "栃木県": 7, "滋賀県": 7, "熊本県": 6, "石川県": 5, "奈良県": 5, "愛媛県": 5, "広島県": 5, "福島県": 5, "福井県": 4, "富山県": 4, "青森県": 4, "長崎県": 4, "鹿児島県": 4, "宮崎県": 4, "山梨県": 3, "和歌山県": 3, "秋田県": 3, "山形県": 3, "大分県": 3, "岡山県": 3, "佐賀県": 2, "香川県": 2, "岩手県": 2, "山口県": 2, "鳥取県": 1, "島根県": 1, "徳島県": 1},
        "status": "partial",
        "source": "https://todo-ran.com/t/kiji/25184",
    },
    "株式会社成城石井": {
        "total": 230,
        "by_prefecture": {"東京都": 99, "神奈川県": 34, "大阪府": 21, "愛知県": 14, "兵庫県": 12, "埼玉県": 11, "千葉県": 8, "奈良県": 6, "京都府": 4, "静岡県": 4, "岐阜県": 3, "広島県": 2, "茨城県": 2, "宮城県": 1, "福島県": 1, "栃木県": 1, "群馬県": 1, "新潟県": 1, "山梨県": 1, "三重県": 1, "滋賀県": 1, "和歌山県": 1, "岡山県": 1},
        "status": "partial",
        "source": "https://ajsm.jp/seijoishiiCorp.htm",
    },
    "イオン九州株式会社": {
        "total": 372,
        "by_prefecture": {"山口県": 1, "福岡県": 148, "佐賀県": 32, "長崎県": 50, "熊本県": 41, "大分県": 41, "宮崎県": 36, "鹿児島県": 23},
        "status": "ok",
        "source": "https://ajsm.jp/aeonkyusyuCorp.htm",
    },
    "相鉄ローゼン株式会社": {
        "total": 47,
        "by_prefecture": {"東京都": 3, "神奈川県": 44},
        "status": "ok",
        "source": "https://ajsm.jp/sotetsu_rosen.html",
    },
    "株式会社ホクノー": {
        "total": 5,
        "by_prefecture": {"北海道": 5},
        "status": "ok",
        "source": "https://ja.wikipedia.org/wiki/%E3%83%9B%E3%82%AF%E3%83%8E%E3%83%BC",
    },
    "生活協同組合コープあいづ": {
        "total": 6,
        "by_prefecture": {"福島県": 6},
        "status": "ok",
        "source": "https://www.coop-aizu.jp/enterprise/",
    },
    "株式会社オーシャンシステム": {
        "total": 129,
        "by_prefecture": {"北海道": 2, "宮城県": 11, "秋田県": 5, "山形県": 13, "福島県": 15, "茨城県": 23, "群馬県": 13, "新潟県": 23, "富山県": 7, "長野県": 15, "熊本県": 2},
        "status": "ok",
        "source": "https://ajsm.jp/ocean-systemCorp.htm",
    },
    "株式会社タイヨー": {
        "total": 101,
        "by_prefecture": {"宮崎県": 18, "鹿児島県": 83},
        "status": "ok",
        "source": "https://ajsm.jp/taiyonetCorp.htm",
    },
    "イオン琉球株式会社": {
        "total": 64,
        "by_prefecture": {"沖縄県": 64},
        "status": "partial",
        "source": "https://www.aeon-ryukyu.jp/store/",
    },
    "みやぎ生活協同組合": {
        "total": 62,
        "by_prefecture": {"宮城県": 50, "福島県": 12},
        "status": "partial",
        "source": "https://www.miyagi.coop/shop/ および https://www.fukushima.coop/shop/",
    },
    "コープデリ生活協同組合連合会": {
        "total": 143,
        "by_prefecture": {"埼玉県": 38, "東京都": 68, "千葉県": 18, "茨城県": 5, "栃木県": 4, "群馬県": 8, "長野県": 2},
        "status": "partial",
        "source": "コープみらい概況ページ（mirai.coopnet.or.jp）、いばらきコープ概況ページ、とちぎコープ施設情報ページ（map.coopdeli.coop/to",
    },
    "株式会社オギノ": {
        "total": 53,
        "by_prefecture": {"山梨県": 40, "長野県": 8, "静岡県": 5},
        "status": "ok",
        "source": "ajsm.jp/oginoCorp.htm（日本全国スーパーマーケット情報）",
    },
    "福井県民生活協同組合": {
        "total": 11,
        "by_prefecture": {"福井県": 11},
        "status": "ok",
        "source": "Wikipedia「福井県民生活協同組合」（2024年9月時点、ハーツ店舗11店）",
    },
    "生活協同組合コープやまぐち": {
        "total": 8,
        "by_prefecture": {"山口県": 8},
        "status": "ok",
        "source": "Wikipedia「生活協同組合コープやまぐち」（ここと店舗8店）",
    },
    "生活協同組合コープこうべ": {
        "total": 128,
        "by_prefecture": {"兵庫県": 116, "大阪府": 12},
        "status": "ok",
        "source": "ajsm.jp/kobecoopCorp.htm（日本全国スーパーマーケット情報）",
    },
    "ユニー株式会社": {
        "total": 133,
        "by_prefecture": {"愛知県": 71, "静岡県": 12, "岐阜県": 10, "三重県": 9, "富山県": 4, "石川県": 4, "神奈川県": 4, "長野県": 3, "新潟県": 3, "栃木県": 2, "群馬県": 2, "千葉県": 2, "埼玉県": 2, "福井県": 2, "山梨県": 1, "奈良県": 1, "滋賀県": 1},
        "status": "ok",
        "source": "todo-ran.com/t/kiji/11856（とどラン 都道府県別ユニー系スーパー店舗数）",
    },
    "生活協同組合コープおきなわ": {
        "total": 9,
        "by_prefecture": {"沖縄県": 9},
        "status": "ok",
        "source": "okinawa.coop/shops/（コープおきなわ公式サイト）",
    },
    "株式会社ドミー": {
        "total": 33,
        "by_prefecture": {"愛知県": 33},
        "status": "ok",
        "source": "ajsm.jp/domyCorp.htm（日本全国スーパーマーケット情報）",
    },
    "株式会社長野県A・コープ": {
        "total": 30,
        "by_prefecture": {"長野県": 30},
        "status": "ok",
        "source": "https://ajsm.jp/nagano-acoopCorp.htm",
    },
    "株式会社エーコープみやざき": {
        "total": 30,
        "by_prefecture": {"宮崎県": 30},
        "status": "ok",
        "source": "https://ajsm.jp/acoopmzCorp.htm",
    },
    "株式会社ニシムタ": {
        "total": 40,
        "by_prefecture": {"鹿児島県": 36, "熊本県": 2, "宮崎県": 2},
        "status": "ok",
        "source": "https://ajsm.jp/nishimutaCorp.htm",
    },
    "株式会社京王ストア": {
        "total": 61,
        "by_prefecture": {"東京都": 57, "神奈川県": 4},
        "status": "ok",
        "source": "https://ajsm.jp/keioCorp.htm",
    },
    "生活協同組合おかやまコープ": {
        "total": 11,
        "by_prefecture": {"岡山県": 11},
        "status": "ok",
        "source": "https://okayama.coop/store/list/",
    },
    "株式会社トライアルカンパニー": {
        "total": 368,
        "by_prefecture": {"北海道": 34, "青森県": 3, "岩手県": 5, "宮城県": 7, "福島県": 8, "茨城県": 16, "栃木県": 12, "群馬県": 8, "埼玉県": 8, "千葉県": 13, "東京都": 7, "神奈川県": 3, "富山県": 1, "石川県": 1, "山梨県": 5, "岐阜県": 4, "静岡県": 5, "愛知県": 5, "三重県": 8, "滋賀県": 5, "大阪府": 10, "兵庫県": 7, "奈良県": 9, "和歌山県": 1, "鳥取県": 6, "島根県": 7, "岡山県": 2, "広島県": 1, "山口県": 12, "徳島県": 2, "香川県": 4, "愛媛県": 1, "福岡県": 84, "佐賀県": 12, "長崎県": 8, "熊本県": 15, "大分県": 11, "宮崎県": 11, "鹿児島県": 7},
        "status": "ok",
        "source": "https://ajsm.jp/trial-netCorp.htm",
    },
    "株式会社ビッグ・エー": {
        "total": 350,
        "by_prefecture": {"茨城県": 3, "埼玉県": 121, "千葉県": 71, "東京都": 130, "神奈川県": 25},
        "status": "ok",
        "source": "https://ajsm.jp/biga-AEON.html",
    },
    "イオンリテール株式会社 西日本カンパニー": {
        "total": 139,
        "by_prefecture": {"滋賀県": 4, "京都府": 17, "大阪府": 39, "兵庫県": 35, "奈良県": 6, "和歌山県": 2, "鳥取県": 5, "島根県": 7, "岡山県": 4, "広島県": 8, "山口県": 2, "徳島県": 1, "香川県": 3, "愛媛県": 5, "高知県": 1},
        "status": "ok",
        "source": "https://www.ajsm.jp/aeonretailCorp.htm",
    },
    "イオンマーケット株式会社": {
        "total": 35,
        "by_prefecture": {"東京都": 30, "神奈川県": 4, "千葉県": 1},
        "status": "ok",
        "source": "Wikipedia（イオンマーケット）2026年1月時点。同社は2026年3月1日にマックスバリュ関東へ吸収合併されイオンフードスタイルに統合。",
    },
    "株式会社イオンフードスタイル": {
        "total": 128,
        "by_prefecture": {"東京都": 81, "千葉県": 19, "埼玉県": 6, "神奈川県": 19},
        "status": "ok",
        "source": "WebSearch結果・aeon.com店舗一覧。2026年3月1日発足時点（旧イオンマーケット・旧マックスバリュ関東統合後）。",
    },
    "イオンリテール株式会社 北関東・新潟カンパニー": {
        "total": 89,
        "by_prefecture": {"埼玉県": 28, "茨城県": 12, "栃木県": 5, "群馬県": 3, "新潟県": 41},
        "status": "partial",
        "source": "aeon.com 総合スーパー（イオン・イオンスタイル）都道府県別ページより集計。北関東・新潟カンパニーは埼玉・栃木・茨城・群馬・新潟を担当。ただしaeon.c",
    },
    "生活協同組合ユーコープ": {
        "total": 68,
        "by_prefecture": {"神奈川県": 50, "静岡県": 17, "山梨県": 1},
        "status": "partial",
        "source": "ユーコープ公式サイト（2026年時点・68店舗）、都道府県内訳はWikipedia2018年データ（神奈川80・静岡17・山梨1）を参考に静岡・山梨は据え置き、",
    },
    "イオンビッグ株式会社": {
        "total": 127,
        "by_prefecture": {"宮城県": 20, "福島県": 9, "栃木県": 4, "神奈川県": 6, "山梨県": 13, "静岡県": 16, "長野県": 15, "岐阜県": 11, "愛知県": 11, "三重県": 12, "滋賀県": 6, "奈良県": 4},
        "status": "ok",
        "source": "Wikipedia（イオンビッグ）2026年2月11日時点。",
    },
    "株式会社フィールコーポレーション": {
        "total": 83,
        "by_prefecture": {"愛知県": 75, "静岡県": 8},
        "status": "partial",
        "source": "WebSearch結果（複数情報源）。愛知県75・静岡県8で計83店舗。2025年以降に静岡・愛知で新規開店あり。正確な最新数は公式サイト要確認。",
    },
    "イオンリテール株式会社 南関東カンパニー": {
        "total": 91,
        "by_prefecture": {"東京都": 21, "神奈川県": 27, "千葉県": 40, "山梨県": 3},
        "status": "partial",
        "source": "aeon.com 総合スーパー（イオン・イオンスタイル）都道府県別ページより集計。南関東カンパニーは東京・神奈川・千葉・山梨を担当。ただしaeon.com上の数",
    },
    "株式会社アオキスーパー": {
        "total": 52,
        "by_prefecture": {"愛知県": 52},
        "status": "ok",
        "source": "WebSearch結果（複数情報源）。愛知県のみ展開で50〜52店舗との情報あり。52店舗を採用。",
    },
    "イオンリテール株式会社 中部カンパニー": {
        "total": 98,
        "by_prefecture": {"愛知県": 34, "岐阜県": 7, "三重県": 20, "長野県": 13, "富山県": 3, "石川県": 10, "福井県": 1, "静岡県": 9, "和歌山県": 1},
        "status": "partial",
        "source": "https://www.aeon.com/store/list/%E7%B7%8F%E5%90%88%E3%82%B9%E3%83%BC%E3%83%91%E3",
    },
    "株式会社ドン・キホーテ": {
        "total": 461,
        "by_prefecture": {"北海道": 16, "青森県": 4, "岩手県": 2, "宮城県": 9, "秋田県": 3, "山形県": 3, "福島県": 5, "茨城県": 11, "栃木県": 7, "群馬県": 8, "埼玉県": 26, "千葉県": 25, "東京都": 57, "神奈川県": 28, "新潟県": 8, "富山県": 4, "石川県": 5, "福井県": 4, "山梨県": 3, "長野県": 9, "静岡県": 17, "愛知県": 47, "三重県": 9, "滋賀県": 7, "京都府": 9, "大阪府": 35, "兵庫県": 12, "奈良県": 5, "和歌山県": 3, "鳥取県": 1, "島根県": 1, "岡山県": 3, "広島県": 5, "山口県": 2, "徳島県": 1, "香川県": 2, "愛媛県": 5, "福岡県": 21, "佐賀県": 2, "長崎県": 4, "熊本県": 6, "大分県": 3, "宮崎県": 4, "鹿児島県": 4, "沖縄県": 8},
        "status": "ok",
        "source": "https://todo-ran.com/t/kiji/25184 (2023年6月時点データ)",
    },
    "株式会社たいらや": {
        "total": 28,
        "by_prefecture": {"栃木県": 28},
        "status": "partial",
        "source": "https://ajsm.jp/tairaya.html / https://www.homemate-research-supermarket.com/cid",
    },
    "株式会社どんたく": {
        "total": 12,
        "by_prefecture": {"石川県": 12},
        "status": "partial",
        "source": "https://www.dontaku.co.jp/stores/ (公式サイト2024年時点)",
    },
    "株式会社遠鉄ストア": {
        "total": 35,
        "by_prefecture": {"静岡県": 33, "愛知県": 2},
        "status": "ok",
        "source": "https://tokubai.co.jp/offices/426/shops (2024年時点)",
    },
    "株式会社マルミヤストア": {
        "total": 41,
        "by_prefecture": {"大分県": 25, "宮崎県": 10, "熊本県": 3, "福岡県": 3},
        "status": "partial",
        "source": "https://marumiya.marumiya-store.co.jp/shops/ / Wikipedia",
    },
    "株式会社京成ストア": {
        "total": 20,
        "by_prefecture": {"東京都": 7, "千葉県": 13},
        "status": "ok",
        "source": "https://www.keiseistore.co.jp/stores/ (公式サイト2024年時点)",
    },
    "株式会社文化堂": {
        "total": 19,
        "by_prefecture": {"東京都": 13, "神奈川県": 6},
        "status": "ok",
        "source": "https://www.bunkado.com/chirashi_tenpo.html (公式サイト2024年時点)",
    },
    "株式会社丸久": {
        "total": 89,
        "by_prefecture": {"山口県": 78, "広島県": 5, "福岡県": 3, "島根県": 3},
        "status": "ok",
        "source": "https://www.mrk09.co.jp/shopinfo/list/",
    },
    "株式会社マルト商事": {
        "total": 37,
        "by_prefecture": {"福島県": 24, "茨城県": 13},
        "status": "ok",
        "source": "https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%AB%E3%83%88_(%E3%83%81%E3%82%A7%E3",
    },
    "みやぎ生活協同組合": {
        "total": 59,
        "by_prefecture": {"宮城県": 48, "福島県": 11},
        "status": "partial",
        "source": "https://supermarket.geomedian.com/area/miyagi_ken/miyagicoop/ / https://miyagi-c",
    },
    "株式会社スパーク": {
        "total": 14,
        "by_prefecture": {"広島県": 14},
        "status": "ok",
        "source": "https://ja.wikipedia.org/wiki/%E3%82%B9%E3%83%91%E3%83%BC%E3%82%AF_(%E3%82%B9%E3",
    },
    "生活協同組合コープえひめ": {
        "total": 13,
        "by_prefecture": {"愛媛県": 13},
        "status": "ok",
        "source": "https://www.coopehime.or.jp/contents/store",
    },
    "株式会社田子重": {
        "total": 14,
        "by_prefecture": {"静岡県": 14},
        "status": "ok",
        "source": "https://ja.wikipedia.org/wiki/%E7%94%B0%E5%AD%90%E9%87%8D / https://www.tagoju.c",
    },
    "株式会社フードウェイ": {
        "total": 27,
        "by_prefecture": {"福岡県": 9, "神奈川県": 4, "静岡県": 3, "東京都": 2, "佐賀県": 1, "長崎県": 1, "大分県": 1, "熊本県": 1, "広島県": 1, "山口県": 1, "千葉県": 1, "埼玉県": 1},
        "status": "ok",
        "source": "https://www.foodway.co.jp/store_information/",
    },
    "株式会社マキヤ": {
        "total": 85,
        "by_prefecture": {"静岡県": 54, "神奈川県": 12, "山梨県": 10, "埼玉県": 9},
        "status": "partial",
        "source": "https://www.makiya-group.co.jp/glance/ / https://ja.wikipedia.org/wiki/%E3%83%9E",
    },
    "角上魚類ホールディングス株式会社": {
        "total": 24,
        "by_prefecture": {"東京都": 4, "埼玉県": 8, "神奈川県": 2, "千葉県": 2, "群馬県": 2, "長野県": 2, "新潟県": 2},
        "status": "partial",
        "source": "https://www.kakujoe.co.jp/shoplist.php",
    },
    "生活協同組合ユーコープ": {
        "total": 61,
        "by_prefecture": {"神奈川県": 44, "静岡県": 16, "山梨県": 1},
        "status": "partial",
        "source": "https://info.ucoop.coop/store/search/",
    },
    "株式会社ベイシア": {
        "total": 138,
        "by_prefecture": {"群馬県": 38, "埼玉県": 24, "千葉県": 23, "栃木県": 13, "静岡県": 8, "茨城県": 8, "愛知県": 6, "長野県": 5, "山梨県": 3, "福島県": 2, "東京都": 2, "新潟県": 2, "滋賀県": 2, "神奈川県": 1, "岐阜県": 1},
        "status": "partial",
        "source": "https://ja.wikipedia.org/wiki/%E3%83%99%E3%82%A4%E3%82%B7%E3%82%A2",
    },
}