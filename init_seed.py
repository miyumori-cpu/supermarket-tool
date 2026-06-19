"""
seed_data.py のデータをキャッシュに書き込む初期化スクリプト。
初回実行時やリセット時に使う。
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

from scraper import save_cache, load_cache
from seed_data import SEED_DATA


def init_seed(overwrite: bool = False):
    written = 0
    skipped = 0
    for company_name, data in SEED_DATA.items():
        if not overwrite and load_cache(company_name):
            skipped += 1
            continue
        save_cache(company_name, data)
        written += 1
    print(f"初期データ書き込み完了: {written}社 (スキップ: {skipped}社)")


if __name__ == "__main__":
    force = "--force" in sys.argv
    init_seed(overwrite=force)
