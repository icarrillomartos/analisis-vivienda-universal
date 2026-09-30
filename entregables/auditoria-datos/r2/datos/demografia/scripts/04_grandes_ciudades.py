import pandas as pd

OUT = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/demografia/limpio"

ciudades = {
    "Madrid": 3506730,
    "Barcelona": 1731649,
    "Valencia/València": 840792,
    "Sevilla": 689423,
    "Zaragoza": 693091,
    "Málaga": 599063,
}

prov_map = {
    "Madrid": "Madrid",
    "Barcelona": "Barcelona",
    "Valencia/València": "Valencia/València",  # will match provincia table key below
    "Sevilla": "Sevilla",
    "Zaragoza": "Zaragoza",
    "Málaga": "Málaga",
}

prov = pd.read_csv(f"{OUT}/poblacion_18mas_por_provincia_ECP.csv")
prov = prov.set_index("provincia_o_ambito")

rows = []
for city, pop in ciudades.items():
    key = prov_map[city]
    # provincia csv used key 'Valencia/València' spelled with accented characters; find matching index robustly
    match = [idx for idx in prov.index if idx.split("/")[0].strip() == key.split("/")[0].strip()]
    if not match:
        match = [idx for idx in prov.index if key in idx or idx in key]
    idxname = match[0]
    tot_prov = prov.loc[idxname, "poblacion_total"]
    ad_prov = prov.loc[idxname, "poblacion_18_mas"]
    share = ad_prov/tot_prov
    adultos_est = round(pop*share)
    rows.append({
        "municipio": city, "poblacion_total_padron_20250101": pop,
        "provincia": idxname, "pct_18mas_provincial_aplicado": round(share*100,2),
        "adultos_18mas_ESTIMADO": adultos_est
    })

df = pd.DataFrame(rows)
df.to_csv(f"{OUT}/grandes_ciudades_padron2025_adultos_estimado.csv", index=False)
print(df.to_string())
