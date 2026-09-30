import json, re, itertools
import pandas as pd

RAW = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/demografia/raw"
OUT = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/demografia/limpio"

# ---------- Proyeccion de hogares CCAA por tamano (54562) ----------
with open(f"{RAW}/proy_hogares_ccaa_tamano_54562.json") as f:
    data = json.load(f)

rows = []
for s in data:
    parts = [p.strip() for p in s["Nombre"].split(".") if p.strip()!=""]
    tam = None
    geo_parts = []
    for p in parts:
        if p in ("Total","1","2","3","4 y más","Tamaño medio del hogar"):
            tam = p
        else:
            geo_parts.append(p)
    geo = ". ".join(geo_parts) if geo_parts else "Total Nacional"
    for d in s["Data"]:
        rows.append({"geo": geo, "tamano_hogar": tam, "anyo": d["Anyo"], "valor": d["Valor"]})

df = pd.DataFrame(rows)
df.to_csv(f"{OUT}/proyeccion_hogares_ccaa_tamano_2026_2041.csv", index=False)
print("filas:", len(df))
nat = df[df['geo']=='Total Nacional']
print(nat[nat['anyo'].isin([2026,2030,2035,2039])].to_string())

# ---------- Eurostat ilc_lvps08 ----------
def eurostat_to_df(path):
    d = json.load(open(path))
    dims = d['dimension']
    dim_names = list(dims.keys())
    cats = {}
    for dn in dim_names:
        cat = dims[dn]['category']
        idx = cat['index']; lab = cat['label']
        pos_to_code = {v:k for k,v in idx.items()}
        cats[dn] = [(pos_to_code[i], lab[pos_to_code[i]]) for i in range(len(pos_to_code))]
    value = d['value']
    ranges = [range(len(cats[dn])) for dn in dim_names]
    rows = []
    for combo in itertools.product(*ranges):
        idx = 0
        for i, dn in enumerate(dim_names):
            idx = idx*len(cats[dn]) + combo[i]
        key = str(idx)
        if key in value:
            row = {dn: cats[dn][combo[i]][1] for i, dn in enumerate(dim_names)}
            row['value'] = value[key]
            rows.append(row)
    return pd.DataFrame(rows), d.get('label')

df_lvps, label1 = eurostat_to_df(f"{RAW}/eurostat_ilc_lvps08.json")
df_lvps.to_csv(f"{OUT}/eurostat_ilc_lvps08_jovenes_con_padres.csv", index=False)
print("\nEurostat ilc_lvps08:", label1)
print(df_lvps[(df_lvps['sex']=='Total') & (df_lvps['age']=='From 18 to 34 years')].sort_values('time').to_string())

df_yth, label2 = eurostat_to_df(f"{RAW}/eurostat_yth_demo_030.json")
df_yth.to_csv(f"{OUT}/eurostat_yth_demo_030_edad_emancipacion.csv", index=False)
print("\nEurostat yth_demo_030:", label2)
print(df_yth[df_yth['sex']=='Total'].sort_values('time').tail(10).to_string())
