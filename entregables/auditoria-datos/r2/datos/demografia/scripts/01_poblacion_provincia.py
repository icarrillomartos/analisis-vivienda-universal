import json, re, sys
import pandas as pd

RAW = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/demografia/raw"
OUT = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/demografia/limpio"

SEXO_SET = {"Total", "Hombres", "Mujeres"}

def is_edad_token(tok):
    if tok == "Todas las edades":
        return True
    if re.match(r'^\d+\s*años?$', tok):
        return True
    if re.match(r'^\d+\s*y\s*más\s*años?$', tok):
        return True
    return False

def edad_to_num(tok):
    if tok == "Todas las edades":
        return None
    m = re.match(r'^(\d+)', tok)
    return int(m.group(1)) if m else None

def load(fname):
    with open(f"{RAW}/{fname}") as f:
        return json.load(f)

def series_to_rows(data):
    rows = []
    for s in data:
        name = s.get("Nombre","").strip()
        for d in s.get("Data", []):
            rows.append({
                "Nombre": name,
                "Anyo": d.get("Anyo"),
                "Fecha": d.get("Fecha"),
                "Valor": d.get("Valor"),
                "Secreto": d.get("Secreto"),
            })
    return pd.DataFrame(rows)

def classify_tokens(nombre):
    parts = [p.strip() for p in nombre.split(".") if p.strip()!=""]
    # drop trailing 'Población' and 'Número' tokens (and any unit tokens)
    parts = [p for p in parts if p not in ("Población", "Número")]
    sexo = None
    edad = None
    geo_parts = []
    for p in parts:
        if p in SEXO_SET and sexo is None:
            sexo = p
        elif is_edad_token(p) and edad is None:
            edad = p
        else:
            geo_parts.append(p)
    geo = ". ".join(geo_parts) if geo_parts else None
    return geo, edad, sexo

# ---------- 1a. Poblacion por provincia, sexo, edad simple (tabla 56940) ----------
data = load("ecp_poblacion_provincia_sexo_edadsimple_ACTUAL_59589.json")
df = series_to_rows(data)
print("56940 rows:", len(df), "max Anyo:", df['Anyo'].max())

parsed = df['Nombre'].apply(classify_tokens)
df[['geo','edad','sexo']] = pd.DataFrame(parsed.tolist(), index=df.index)
bad = df[df['geo'].isna() | df['edad'].isna() | df['sexo'].isna()]
print("Filas sin parsear bien:", len(bad))
df.to_csv(f"{OUT}/raw_poblacion_provincia_edadsimple.csv", index=False)

latest_year = df['Anyo'].max()
d1 = df[(df['Anyo']==latest_year) & (df['sexo']=='Total')].copy()
d1['edad_num'] = d1['edad'].apply(edad_to_num)

provincias = sorted(d1['geo'].dropna().unique())
print("N geos:", len(provincias))
rows_out = []
for geo in provincias:
    sub = d1[d1['geo']==geo]
    total = sub[sub['edad']=='Todas las edades']['Valor']
    total = total.iloc[0] if len(total) else None
    adultos = sub[(sub['edad_num'].notna()) & (sub['edad_num']>=18)]['Valor'].sum()
    rows_out.append({"provincia_o_ambito": geo, "poblacion_total": total, "poblacion_18_mas": adultos, "anyo": latest_year})

out1 = pd.DataFrame(rows_out).sort_values('provincia_o_ambito')
out1.to_csv(f"{OUT}/poblacion_18mas_por_provincia_ECP.csv", index=False)
print(out1.to_string())

# ---------- 1b. Poblacion nacional por edad simple sin nacionalidad (56934) para fraccion 15-19 ----------
data2 = load("ecp_poblacion_nacional_sexo_edadsimple_ACTUAL_59583.json")
df2 = series_to_rows(data2)
parsed2 = df2['Nombre'].apply(classify_tokens)
df2[['geo','edad','sexo']] = pd.DataFrame(parsed2.tolist(), index=df2.index)
latest_year2 = df2['Anyo'].max()
d2 = df2[(df2['Anyo']==latest_year2) & (df2['sexo']=='Total')].copy()
d2['edad_num'] = d2['edad'].apply(edad_to_num)
pob_15 = d2[d2['edad_num']==15]['Valor'].sum()
pob_16 = d2[d2['edad_num']==16]['Valor'].sum()
pob_17 = d2[d2['edad_num']==17]['Valor'].sum()
pob_18 = d2[d2['edad_num']==18]['Valor'].sum()
pob_19 = d2[d2['edad_num']==19]['Valor'].sum()
pob_1519 = pob_15+pob_16+pob_17+pob_18+pob_19
frac_18_19_of_1519 = (pob_18+pob_19)/pob_1519 if pob_1519 else None
print("pob 15-19 nacional:", pob_1519, "frac 18-19 dentro de 15-19:", frac_18_19_of_1519)
with open(f"{OUT}/nota_fraccion_18_19_en_15_19.txt","w") as f:
    f.write(f"Anyo referencia: {latest_year2}\n")
    f.write(f"Poblacion 15 anios: {pob_15}\nPoblacion 16: {pob_16}\nPoblacion 17: {pob_17}\nPoblacion 18: {pob_18}\nPoblacion 19: {pob_19}\n")
    f.write(f"Poblacion 15-19 total: {pob_1519}\n")
    f.write(f"Fraccion de (18+19) dentro del grupo quinquenal 15-19: {frac_18_19_of_1519}\n")

tot_nac = d2[d2['edad']=='Todas las edades']['Valor']
tot_nac = tot_nac.iloc[0] if len(tot_nac) else None
adultos_nac_exact = d2[(d2['edad_num'].notna()) & (d2['edad_num']>=18)]['Valor'].sum()
print("Poblacion total nacional (56934):", tot_nac, "Anyo:", latest_year2)
print("Adultos 18+ nacional EXACTO (56934):", adultos_nac_exact)

with open(f"{OUT}/resumen_poblacion_nacional.txt","w") as f:
    f.write(f"Fuente: ECP tabla 56934 (nacional, edad simple, sin nacionalidad)\n")
    f.write(f"Anyo referencia (Anyo INE): {latest_year2}\n")
    f.write(f"Poblacion total nacional: {tot_nac}\n")
    f.write(f"Poblacion 18+ nacional (exacta, edad simple): {adultos_nac_exact}\n")
