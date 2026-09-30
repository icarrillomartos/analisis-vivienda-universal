import json, re
import pandas as pd

RAW = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/demografia/raw"
OUT = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/demografia/limpio"

SEXO_SET = {"Total", "Hombres", "Mujeres"}
NAC_SET = {"Total", "Española", "Extranjera"}

def is_edad_grupo(tok):
    if tok == "Todas las edades":
        return True
    if re.match(r'^De\s+\d+\s+a\s+\d+\s+años$', tok):
        return True
    if re.match(r'^\d+\s*y\s*más\s*años$', tok):
        return True
    return False

def edad_grupo_min(tok):
    if tok == "Todas las edades":
        return None
    m = re.match(r'^De\s+(\d+)\s+a\s+(\d+)', tok)
    if m:
        return int(m.group(1)), int(m.group(2))
    m = re.match(r'^(\d+)\s*y\s*más', tok)
    if m:
        return int(m.group(1)), 200
    return None

with open(f"{RAW}/ecp_poblacion_geo_sexo_grupoedad_nacionalidad_82104.json") as f:
    data = json.load(f)

rows = []
for s in data:
    nombre = s["Nombre"].strip()
    parts = [p.strip() for p in nombre.split(".") if p.strip() != ""]
    parts = [p for p in parts if p not in ("Población", "Número")]
    sexo = None
    nac = None
    edad = None
    geo_parts = []
    for p in parts:
        if p in SEXO_SET and sexo is None and (p != "Total" or nac is not None or True):
            pass
        # we'll classify carefully below
    # Because "Total" is ambiguous between sexo and nacionalidad, classify with priority + consumption
    sexo = None; nac = None; edad = None; geo_parts = []
    used_total_as = None
    for p in parts:
        if edad is None and is_edad_grupo(p):
            edad = p
            continue
        if p == "Española" or p == "Extranjera":
            nac = p
            continue
        if p == "Hombres" or p == "Mujeres":
            sexo = p
            continue
        if p == "Total":
            # first "Total" encountered (in dimension order geo,nac,edad,sexo as printed) -> ambiguous
            geo_parts.append(("TOTAL_PLACEHOLDER"))
            continue
        geo_parts.append(p)
    # Now resolve TOTAL_PLACEHOLDERs: there can be 0,1, or 2 "Total" tokens remaining
    # representing missing nac and/or sexo (whichever wasn't already set), in the ORDER they appeared.
    n_placeholders = geo_parts.count("TOTAL_PLACEHOLDER")
    geo_parts2 = [g for g in geo_parts if g != "TOTAL_PLACEHOLDER"]
    # Determine which dims still need a value
    missing = []
    if nac is None:
        missing.append("nac")
    if sexo is None:
        missing.append("sexo")
    # assign placeholders in order to missing dims (nac before sexo, matches typical Nombre order: geo, nac, edad, sexo)
    for i in range(min(n_placeholders, len(missing))):
        if missing[i] == "nac":
            nac = "Total"
        elif missing[i] == "sexo":
            sexo = "Total"
    geo = ". ".join(geo_parts2) if geo_parts2 else None
    val = None
    if s["Data"]:
        val = s["Data"][0]["Valor"]
        anyo = s["Data"][0]["Anyo"]
    else:
        anyo = None
    rows.append({"geo": geo, "edad": edad, "nacionalidad": nac, "sexo": sexo, "Valor": val, "Anyo": anyo})

df = pd.DataFrame(rows)
print("Total rows:", len(df))
print("Missing any field:", df[df[['geo','edad','nacionalidad','sexo']].isna().any(axis=1)].shape[0])
print(df['nacionalidad'].value_counts())
print(df['sexo'].value_counts())
print(df['geo'].nunique())
df.to_csv(f"{OUT}/raw_poblacion_geo_edadgrupo_nacionalidad_parsed.csv", index=False)

# Filter Total sexo
d = df[df['sexo']=='Total'].copy()
latest = d['Anyo'].max()
d = d[d['Anyo']==latest]

FRACT_18_19_IN_1519 = 0.409626  # computed from national single-year data (56934), see nota_fraccion file

def compute_18plus(sub):
    total_all = sub[sub['edad']=='Todas las edades']['Valor'].sum()
    band_1519 = sub[sub['edad']=='De 15 a 19 años']['Valor'].sum()
    rest = sub[(sub['edad']!='Todas las edades') & (sub['edad']!='De 15 a 19 años') &
               (sub['edad'].apply(lambda e: (edad_grupo_min(e) is not None) and edad_grupo_min(e)[0] >= 20))]['Valor'].sum()
    approx_18plus = rest + FRACT_18_19_IN_1519*band_1519
    return total_all, approx_18plus

rows_out = []
for geo in sorted(d['geo'].dropna().unique()):
    for nac in ['Total','Española','Extranjera']:
        sub = d[(d['geo']==geo) & (d['nacionalidad']==nac)]
        if sub.empty:
            continue
        total_all, approx18 = compute_18plus(sub)
        rows_out.append({"geo": geo, "nacionalidad": nac, "poblacion_total": total_all,
                          "poblacion_18mas_aprox": round(approx18), "anyo": latest})

out = pd.DataFrame(rows_out)
out.to_csv(f"{OUT}/poblacion_18mas_por_provincia_y_nacionalidad_APROX.csv", index=False)
print(out[out['geo']=='Total Nacional'])
print(out.head(20).to_string())
