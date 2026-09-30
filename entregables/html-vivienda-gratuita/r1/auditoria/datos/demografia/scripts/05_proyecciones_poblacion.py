import json, re
import pandas as pd

RAW = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/demografia/raw"
OUT = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/demografia/limpio"

def load(fname):
    with open(f"{RAW}/{fname}") as f:
        return json.load(f)

# ---------- National long-term projection, single-year age (36643) ----------
data = load("proy_poblacion_largoplazo_nacional_edad_36643.json")

def edad_to_num(tok):
    tok = tok.strip()
    if tok == "Todas las edades":
        return None
    m = re.match(r'^(\d+)', tok)
    return int(m.group(1)) if m else None

SEXO_SET = {"Total","Hombres","Mujeres"}
rows = []
for s in data:
    parts = [p.strip() for p in s["Nombre"].split(".") if p.strip()!=""]
    parts = [p for p in parts if p not in ("Población","Total Nacional","Proyección a largo plazo")]
    sexo = None
    edad = None
    for p in parts:
        if p in SEXO_SET:
            sexo = p
        elif p == "Todas las edades" or re.match(r'^\d+', p):
            edad = p
    for d in s["Data"]:
        rows.append({"sexo": sexo, "edad": edad, "anyo": d["Anyo"], "valor": d["Valor"]})

df = pd.DataFrame(rows)
df["edad_num"] = df["edad"].apply(edad_to_num)
df.to_csv(f"{OUT}/proyeccion_poblacion_nacional_edadsimple_largoplazo.csv", index=False)
print("Filas:", len(df), "anyos:", sorted(df['anyo'].unique())[:5], "...", sorted(df['anyo'].unique())[-5:])

dsex = df[df['sexo']=='Total']
# Cohorte que cumple 18 anyos cada anyo (aprox = poblacion de 18 anyos a 1 de enero de ese anyo)
cohortes = dsex[dsex['edad_num']==18][['anyo','valor']].sort_values('anyo')
cohortes.to_csv(f"{OUT}/cohorte_18_anyos_proyectada_2026_2039.csv", index=False)
print("\nCohorte de 18 anyos (aprox., poblacion de 18 anyos a 1-ene):")
print(cohortes[(cohortes['anyo']>=2026)&(cohortes['anyo']<=2039)].to_string())

# Poblacion adulta total (18+) nacional proyectada, por anyo
adultos = dsex[(dsex['edad_num'].notna()) & (dsex['edad_num']>=18)].groupby('anyo')['valor'].sum().reset_index()
totales = dsex[dsex['edad']=='Todas las edades'][['anyo','valor']].rename(columns={'valor':'poblacion_total'})
merged = adultos.rename(columns={'valor':'poblacion_18mas'}).merge(totales, on='anyo')
merged = merged.sort_values('anyo')
merged.to_csv(f"{OUT}/proyeccion_poblacion_18mas_nacional_2026_2039.csv", index=False)
print("\nPoblacion adulta proyectada 2026-2039 (nacional, proyeccion a largo plazo, escenario central):")
print(merged[(merged['anyo']>=2026)&(merged['anyo']<=2039)].to_string())

# ---------- Provincial short-term projection (36726) para 2030 y 2039 ----------
data2 = load("proy_poblacion_cortoplazo_provincia_edad_36726.json")
rows2 = []
for s in data2:
    parts = [p.strip() for p in s["Nombre"].split(".") if p.strip()!=""]
    parts = [p for p in parts if p not in ("Población","Proyección a corto plazo")]
    sexo = None; edad = None; geo_parts=[]
    for p in parts:
        if p in SEXO_SET:
            sexo = p
        elif p == "Todas las edades" or re.match(r'^\d+', p):
            edad = p
        else:
            geo_parts.append(p)
    geo = ". ".join(geo_parts) if geo_parts else None
    if sexo != "Total":
        continue
    edn = edad_to_num(edad) if edad else None
    for d in s["Data"]:
        if d["Anyo"] in (2030, 2035, 2039):
            rows2.append({"geo": geo, "edad": edad, "edad_num": edn, "anyo": d["Anyo"], "valor": d["Valor"]})

df2 = pd.DataFrame(rows2)
df2.to_csv(f"{OUT}/proyeccion_poblacion_provincia_edadsimple_2030_2035_2039_RAW.csv", index=False)

out_rows = []
for geo in sorted(df2['geo'].dropna().unique()):
    for anyo in (2030,2035,2039):
        sub = df2[(df2['geo']==geo) & (df2['anyo']==anyo)]
        total = sub[sub['edad']=='Todas las edades']['valor'].sum()
        adultos = sub[(sub['edad_num'].notna()) & (sub['edad_num']>=18)]['valor'].sum()
        out_rows.append({"provincia": geo, "anyo": anyo, "poblacion_total_proy": total, "poblacion_18mas_proy": adultos})

out2 = pd.DataFrame(out_rows)
out2.to_csv(f"{OUT}/proyeccion_poblacion_18mas_por_provincia_2030_2035_2039.csv", index=False)
print("\nProyeccion provincial (muestra Total Nacional):")
print(out2[out2['provincia']=='Total Nacional'].to_string())
