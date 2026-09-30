"""
Descarga los datasets de Eurostat usados en ficha.md (gasto/ingreso AAPP, deficit/deuda,
COFOG, presion fiscal, PIB). Requiere Python 3 con urllib (stdlib).

Nota importante sobre la API de Eurostat: para pedir varios valores de una misma
dimension hay que REPETIR el parametro (na_item=A&na_item=B), no usar listas
separadas por comas (na_item=A,B), que la API interpreta como codigo invalido y
devuelve "value": {} vacio.

Uso: python3 fetch_eurostat.py
Los ficheros se guardan en ../raw/
"""
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

RAW = Path(__file__).resolve().parent.parent / "raw"
BASE = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"


def fetch(dataset, params, outfile):
    qs = urllib.parse.urlencode(params)
    url = f"{BASE}{dataset}?format=JSON&{qs}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    (RAW / outfile).write_bytes(data)
    d = json.loads(data)
    print(outfile, "values:", len(d.get("value", {})), "size:", d.get("size"))


QUERIES = [
    # Deficit (B9) y deuda (GD), España, 2023-2025
    ("gov_10dd_edpt1",
     [("geo", "ES"), ("sector", "S13"), ("na_item", "B9"), ("na_item", "GD"),
      ("unit", "MIO_EUR"), ("unit", "PC_GDP"),
      ("time", "2023"), ("time", "2024"), ("time", "2025")],
     "eurostat_gov_10dd_edpt1_ES.json"),
    # Gasto to (TE) e ingreso total (TR) AAPP, España, 2023-2025
    ("gov_10a_main",
     [("geo", "ES"), ("sector", "S13"), ("na_item", "TE"), ("na_item", "TR"),
      ("unit", "MIO_EUR"), ("unit", "PC_GDP"),
      ("time", "2023"), ("time", "2024"), ("time", "2025")],
     "eurostat_gov_10a_main_ES_2025.json"),
    # Gasto TE/TR en %PIB, España vs UE-27, 2023-2024 (comparacion)
    ("gov_10a_main",
     [("geo", "EU27_2020"), ("geo", "ES"), ("sector", "S13"),
      ("na_item", "TE"), ("na_item", "TR"), ("unit", "PC_GDP"),
      ("time", "2023"), ("time", "2024")],
     "eurostat_gov_10a_main_ES_EU_pcgdp.json"),
    # COFOG Espana: vivienda (GF06/GF0601/GF1006), sanidad (GF07), proteccion social (GF10/GF1002)
    ("gov_10a_exp",
     [("geo", "ES"), ("sector", "S13"), ("na_item", "TE"),
      ("unit", "MIO_EUR"), ("unit", "PC_GDP"),
      ("cofog99", "GF06"), ("cofog99", "GF0601"), ("cofog99", "GF07"),
      ("cofog99", "GF10"), ("cofog99", "GF1002"), ("cofog99", "GF1006"),
      ("time", "2022"), ("time", "2023")],
     "eurostat_gov_10a_exp_ES_v2.json"),
    # COFOG UE-27 (comparacion vivienda/sanidad/proteccion social)
    ("gov_10a_exp",
     [("geo", "EU27_2020"), ("sector", "S13"), ("na_item", "TE"),
      ("unit", "MIO_EUR"), ("unit", "PC_GDP"),
      ("cofog99", "GF06"), ("cofog99", "GF0601"), ("cofog99", "GF07"),
      ("cofog99", "GF10"), ("cofog99", "GF1006"),
      ("time", "2023")],
     "eurostat_gov_10a_exp_EU27_v2.json"),
    # Presion fiscal: total impuestos, total impuestos+cotizaciones, IVA, renta. Espana vs UE27
    ("gov_10a_taxag",
     [("geo", "ES"), ("geo", "EU27_2020"), ("sector", "S13"), ("unit", "PC_GDP"),
      ("na_item", "D2_D5_D91"), ("na_item", "D2_D5_D91_D61_M_D995"),
      ("na_item", "D211"), ("na_item", "D51"),
      ("time", "2022"), ("time", "2023")],
     "eurostat_gov_10a_taxag.json"),
    # Cotizaciones sociales (D61) en millones de euros, Espana
    ("gov_10a_taxag",
     [("geo", "ES"), ("sector", "S13"), ("unit", "MIO_EUR"), ("na_item", "D61"),
      ("time", "2022"), ("time", "2023")],
     "eurostat_social_contrib_ES.json"),
    # Gasto en intereses de la deuda (D41PAY)
    ("gov_10dd_edpt1",
     [("geo", "ES"), ("sector", "S13"), ("na_item", "D41PAY"),
      ("unit", "MIO_EUR"), ("unit", "PC_GDP"),
      ("time", "2023"), ("time", "2024")],
     "eurostat_interest_expenditure_ES.json"),
    # PIB nominal anual (contraste con INE)
    ("nama_10_gdp",
     [("geo", "ES"), ("na_item", "B1GQ"), ("unit", "CP_MEUR"),
      ("time", "2022"), ("time", "2023"), ("time", "2024")],
     "eurostat_nama_10_gdp_ES.json"),
    # PIB nominal trimestral (contraste con INE)
    ("namq_10_gdp",
     [("geo", "ES"), ("na_item", "B1GQ"), ("unit", "CP_MEUR"), ("s_adj", "NSA"),
      ("time", "2024-Q1"), ("time", "2024-Q2"), ("time", "2024-Q3"), ("time", "2024-Q4"),
      ("time", "2025-Q1"), ("time", "2025-Q2")],
     "eurostat_namq_10_gdp_ES.json"),
]


if __name__ == "__main__":
    RAW.mkdir(parents=True, exist_ok=True)
    for dataset, params, outfile in QUERIES:
        fetch(dataset, params, outfile)
        time.sleep(0.5)
