"""
Extrae del XLS oficial del MIVAU (Valor tasado de vivienda libre, tabla 1 "boletinonline2")
la serie nacional anual (media de los 4 trimestres, y trimestre 4) desde 1999-2000 hasta 2026,
y los valores de provincias objetivo (2T 2026, ultimo dato publicado).
Fuente: https://apps.fomento.gob.es/boletinonline2/sedal/35101000.XLS (MIVAU)
"""
import xlrd
import csv
import os

RAW = os.path.join(os.path.dirname(__file__), "..", "raw")
LIMPIO = os.path.join(os.path.dirname(__file__), "..", "limpio")
os.makedirs(LIMPIO, exist_ok=True)

wb = xlrd.open_workbook(os.path.join(RAW, "mivau_valor_tasado_nacional_serie.xls"))

sheet_names = [
    "1995, 1996, 1997, 1998",
    "1999, 2000, 2001, 2002",
    "2003, 2004, 2005, 2006",
    "2007, 2008, 2009, 2010",
    "2011, 2012, 2013, 2014",
    "2015, 2016, 2017, 2018",
    "2019, 2020, 2021, 2022",
    "2023, 2024, 2025, 2026",
]

anual_rows = []
provincias_2026t2 = {}

TARGET_PROV = ["Madrid (Comunidad de)", "Barcelona", "Valencia/València", "Sevilla", "Zaragoza", "Málaga",
               "TOTAL NACIONAL"]

for sname in sheet_names:
    sh = wb.sheet_by_name(sname)
    # Find header row with "TOTAL NACIONAL"
    # Years are in row 11 spaced every 4 columns starting col 2
    years_row = 11
    years = []
    for c in range(2, sh.ncols, 4):
        val = sh.cell_value(years_row, c)
        if val:
            year = str(val).replace("Año", "").strip()
            years.append((year, c))
    for r in range(13, sh.nrows):
        name = str(sh.cell_value(r, 1)).strip()
        if not name:
            continue
        if name == "TOTAL NACIONAL" or name in TARGET_PROV:
            for year, c0 in years:
                q_vals = []
                for q in range(4):
                    v = sh.cell_value(r, c0 + q)
                    if isinstance(v, float):
                        q_vals.append(v)
                if q_vals:
                    media_anual = sum(q_vals) / len(q_vals)
                    q4 = q_vals[-1] if len(q_vals) == 4 else None
                    anual_rows.append({
                        "territorio": name,
                        "anio": year,
                        "media_4_trimestres_eur_m2": round(media_anual, 1),
                        "valor_4T_eur_m2": q4,
                        "n_trimestres_disponibles": len(q_vals),
                    })
                    if year == "2026" and len(q_vals) >= 2:
                        provincias_2026t2[name] = q_vals[1]  # 2nd quarter

with open(os.path.join(LIMPIO, "mivau_valor_tasado_serie_nacional_y_provincias_anual.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["territorio", "anio", "media_4_trimestres_eur_m2", "valor_4T_eur_m2", "n_trimestres_disponibles"])
    w.writeheader()
    for row in anual_rows:
        w.writerow(row)

print("Filas escritas:", len(anual_rows))
print("\nProvincias objetivo, 2T 2026 (euros/m2):")
for k, v in provincias_2026t2.items():
    print(f"  {k}: {v}")

# ---- Municipios >25.000 hab: extraer 6 ciudades, ultimo trimestre T2A2026 ----
wb2 = xlrd.open_workbook(os.path.join(RAW, "mivau_valor_tasado_municipios25000.xls"))
sh2 = wb2.sheet_by_name("T2A2026")
targets = {"MADRID": "Madrid", "BARCELONA": "Barcelona", "VALENCIA": "Valencia", "SEVILLA": "Sevilla",
           "ZARAGOZA": "Zaragoza", "MALAGA": "Málaga", "MÁLAGA": "Málaga"}
muni_rows = []
cur_prov = ""
for r in range(17, sh2.nrows):
    prov = str(sh2.cell_value(r, 1)).strip()
    muni = str(sh2.cell_value(r, 2)).strip()
    if prov:
        cur_prov = prov
    if muni.upper() in targets:
        muni_rows.append({
            "provincia": cur_prov,
            "municipio": muni,
            "valor_hasta_5_anios_eur_m2": sh2.cell_value(r, 3),
            "valor_mas_5_anios_eur_m2": sh2.cell_value(r, 4),
            "valor_total_eur_m2": sh2.cell_value(r, 5),
            "num_tasaciones_total": sh2.cell_value(r, 9),
            "trimestre": "2T 2026",
        })

with open(os.path.join(LIMPIO, "mivau_valor_tasado_municipios_2T2026.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["provincia", "municipio", "valor_hasta_5_anios_eur_m2",
                                       "valor_mas_5_anios_eur_m2", "valor_total_eur_m2",
                                       "num_tasaciones_total", "trimestre"])
    w.writeheader()
    for row in muni_rows:
        w.writerow(row)

print("\nMunicipios extraidos:", len(muni_rows))
for row in muni_rows:
    print(row)
