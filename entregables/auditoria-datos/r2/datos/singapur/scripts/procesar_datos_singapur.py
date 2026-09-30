"""
Procesa los datos oficiales descargados en raw/ y genera CSV limpios en limpio/.
Fuentes: data.gov.sg (SingStat, HDB). Ver ficha.md para URLs exactas de cada dataset.
"""
import json
import pandas as pd
from pathlib import Path

RAW = Path(__file__).resolve().parent.parent / "raw"
LIMPIO = Path(__file__).resolve().parent.parent / "limpio"
LIMPIO.mkdir(exist_ok=True)


def datastore_json_to_df(path):
    d = json.load(open(path))
    return pd.DataFrame(d["result"]["records"])


def main():
    # 1. Hogares residentes por tipo de vivienda (SingStat vía data.gov.sg)
    df = datastore_json_to_df(RAW / "resident_households_by_dwelling_type.json")
    df.to_csv(LIMPIO / "resident_households_by_dwelling_type.csv", index=False)

    # 2. Poblacion (SingStat "Indicators on Population" via data.gov.sg)
    df = datastore_json_to_df(RAW / "population_indicators.json")
    df.to_csv(LIMPIO / "population_indicators.csv", index=False)

    # 3. PIB nominal (SingStat "Expenditure on GDP at Current Prices" via data.gov.sg)
    df = datastore_json_to_df(RAW / "gdp_expenditure_current_prices.json")
    df.to_csv(LIMPIO / "gdp_expenditure_current_prices.csv", index=False)

    print("CSV limpios generados en", LIMPIO)


if __name__ == "__main__":
    main()
