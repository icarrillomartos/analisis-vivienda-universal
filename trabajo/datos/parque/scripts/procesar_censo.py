# -*- coding: utf-8 -*-
import pandas as pd

RAW = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/parque/raw/censo2021"
OUT = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/parque/limpio"

# 1) Provincial: Total / Principal / No principal (tpx 59520)
df = pd.read_csv(f"{RAW}/59520_viviendas_tipo_ccaa_provincia_tamaño_municipio.csv", sep="\t")
df.columns = ["tipo", "ccaa_prov", "tam_mun", "total"]
sub = df[df.tam_mun == "Total (tamaño de municipio)"].copy()
sub["total"] = sub["total"].str.replace(".", "", regex=False).astype(int)
piv = sub.pivot(index="ccaa_prov", columns="tipo", values="total").reset_index()
piv.to_csv(f"{OUT}/censo2021_viviendas_total_principal_noprincipal_ccaa_provincia.csv", index=False)
print("provincial total/principal/no-principal ->", piv.shape)

# 2) Municipal detallado (tipo principal/secundaria/vacia) para municipios >2000 hab -> filtrar capitales objetivo
df2 = pd.read_csv(f"{RAW}/10mun00_tipo_detallado_municipios_mas2000hab.csv", sep="\t")
df2.columns = ["municipio", "tipo", "total"]
df2["total_num"] = pd.to_numeric(df2["total"].astype(str).str.replace(".", "", regex=False), errors="coerce")
target_codes = {
    "28079": "Madrid",
    "08019": "Barcelona",
    "46250": "Valencia",
    "41091": "Sevilla",
    "50297": "Zaragoza",
    "29067": "Málaga",
}
rows = []
for code, name in target_codes.items():
    m = df2[df2.municipio.str.startswith(code)]
    rec = {"municipio": name, "codigo_ine": code}
    for _, r in m.iterrows():
        rec[r["tipo"]] = r["total_num"]
    rows.append(rec)
out2 = pd.DataFrame(rows)
out2.to_csv(f"{OUT}/censo2021_viviendas_tipo_detallado_6_municipios.csv", index=False)
print(out2)

# 3) Superficie util x habitaciones, nacional (tpx 56829)
df3 = pd.read_csv(f"{RAW}/56829_superficie_habitaciones_nacional_tamano_municipio.csv", sep="\t")
df3.columns = ["tam_mun", "superficie", "habitaciones", "total"]
df3["total_num"] = pd.to_numeric(df3["total"].astype(str).str.replace(".", "", regex=False), errors="coerce")
nat = df3[df3.tam_mun == "Total"]
nat.to_csv(f"{OUT}/censo2021_superficie_habitaciones_nacional.csv", index=False)
print("superficie x habitaciones nacional filas:", len(nat))
print(sorted(nat.superficie.unique()))

# 4) Estado de conservación nacional (tpx 56894)
df4 = pd.read_csv(f"{RAW}/56894_viviendas_estado_conservacion_tipoedificio_anio_tamano.csv", sep="\t")
df4.columns = ["tam_mun", "tipo_edif", "anio", "estado", "total"]
df4["total_num"] = pd.to_numeric(df4["total"].astype(str).str.replace(".", "", regex=False), errors="coerce")
nat4 = df4[(df4.tam_mun == "Total") & (df4.tipo_edif == "Total") & (df4.anio == "Total")]
nat4.to_csv(f"{OUT}/censo2021_viviendas_estado_conservacion_nacional.csv", index=False)
print(nat4[["estado", "total_num"]])
