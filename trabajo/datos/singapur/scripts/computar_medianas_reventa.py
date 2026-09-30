"""
Reconstruye limpio/resale_flat_prices_2024_raw.csv y
limpio/resale_median_price_by_flat_type_2024.csv a partir de la API oficial
de data.gov.sg (HDB "Resale flat prices based on registration date from
Jan-2017 onwards", resource_id d_8b84c4ee58e3cfc0ece0d773c8ca6abc).

La API CKAN de data.gov.sg solo permite filtros por igualdad exacta, así que
se descarga mes a mes (filters={"month": "2024-XX"}) y se concatena.
"""
import json
import urllib.parse
import urllib.request
from pathlib import Path

import pandas as pd

LIMPIO = Path(__file__).resolve().parent.parent / "limpio"
LIMPIO.mkdir(exist_ok=True)

RESOURCE_ID = "d_8b84c4ee58e3cfc0ece0d773c8ca6abc"
BASE_URL = "https://data.gov.sg/api/action/datastore_search"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def fetch_month(month: str) -> list:
    filters = urllib.parse.quote(json.dumps({"month": month}))
    url = f"{BASE_URL}?resource_id={RESOURCE_ID}&filters={filters}&limit=10000"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)
    if not data.get("success"):
        raise RuntimeError(data)
    return data["result"]["records"]


def main(year: str = "2024"):
    records = []
    for m in range(1, 13):
        month = f"{year}-{m:02d}"
        records.extend(fetch_month(month))
    df = pd.DataFrame(records)
    df["resale_price"] = df["resale_price"].astype(float)
    df["floor_area_sqm"] = df["floor_area_sqm"].astype(float)
    df.to_csv(LIMPIO / f"resale_flat_prices_{year}_raw.csv", index=False)

    med = df.groupby("flat_type")["resale_price"].median().sort_values()
    med.to_csv(LIMPIO / f"resale_median_price_by_flat_type_{year}.csv")
    print(med)


if __name__ == "__main__":
    main()
