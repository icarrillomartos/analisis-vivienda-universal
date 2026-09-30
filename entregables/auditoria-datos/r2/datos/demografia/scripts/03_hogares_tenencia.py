import json, re
import pandas as pd

RAW = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/demografia/raw"
OUT = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/demografia/limpio"

def load(fname):
    with open(f"{RAW}/{fname}") as f:
        return json.load(f)

def first_val(s):
    if s["Data"]:
        return s["Data"][0]["Valor"], s["Data"][0]["Anyo"]
    return None, None

# ---- Hogares por tamaño: nacional, CCAA, provincia ----
def parse_hogares_tamano(nombre):
    parts = [p.strip() for p in nombre.split(".") if p.strip()!=""]
    parts = [p for p in parts if p not in ("Hogares en viviendas familiares","Número")]
    # remaining should be [geo, tamano]  or  [tamano, geo] etc. tamano in {Total,1,2,3,'4 y más'}
    tam = None
    geo_parts = []
    for p in parts:
        if p in ("Total","1","2","3","4 y más"):
            tam = p
        else:
            geo_parts.append(p)
    geo = ". ".join(geo_parts) if geo_parts else "Total Nacional"
    return geo, tam

def process_tamano(fname, label):
    data = load(fname)
    rows = []
    for s in data:
        geo, tam = parse_hogares_tamano(s["Nombre"])
        val, anyo = first_val(s)
        rows.append({"geo": geo, "tamano_hogar": tam, "valor": val, "anyo": anyo})
    df = pd.DataFrame(rows)
    df.to_csv(f"{OUT}/hogares_{label}_tamano.csv", index=False)
    print(label, "rows:", len(df), "anyo max:", df['anyo'].max())
    return df

df_nac = process_tamano("ecp_hogares_nacional_tamano_60135.json", "nacional")
df_ccaa = process_tamano("ecp_hogares_ccaa_tamano_60131.json", "ccaa")
df_prov = process_tamano("ecp_hogares_provincia_tamano_60133.json", "provincia")

def parse_tamanomedio(nombre):
    parts = [p.strip() for p in nombre.split(".") if p.strip()!=""]
    parts = [p for p in parts if p not in ("Tamaño medio del hogar","Número")]
    geo = ". ".join(parts) if parts else "Total Nacional"
    return geo

def process_tamanomedio(fname, label):
    data = load(fname)
    rows = []
    for s in data:
        geo = parse_tamanomedio(s["Nombre"])
        val, anyo = first_val(s)
        rows.append({"geo": geo, "tamano_medio_hogar": val, "anyo": anyo})
    df = pd.DataFrame(rows)
    df.to_csv(f"{OUT}/hogares_{label}_tamanomedio.csv", index=False)
    print(label, "medio rows:", len(df))
    return df

process_tamanomedio("ecp_hogares_nacional_tamanomedio_60136.json", "nacional")
process_tamanomedio("ecp_hogares_ccaa_tamanomedio_60132.json", "ccaa")
process_tamanomedio("ecp_hogares_provincia_tamanomedio_60134.json", "provincia")

print("\n--- Nacional hogares por tamano ---")
print(df_nac.to_string())

# ---- ECV Tenencia (CCAA + nacional), porcentajes ----
data = load("ecv_tenencia_ccaa_nacional_76845.json")
TEN_CATS = ["Propiedad","Propiedad sin hipoteca","Propiedad con hipoteca",
            "Alquiler a precio de mercado","Alquiler inferior al precio de mercado","Cesión"]
rows = []
for s in data:
    parts = [p.strip() for p in s["Nombre"].split(".") if p.strip()!=""]
    parts = [p for p in parts if p != "Hogar"]
    cat = None
    for c in TEN_CATS:
        if c in parts:
            cat = c
            break
    geo_parts = [p for p in parts if p != cat]
    geo = ". ".join(geo_parts) if geo_parts else "Total Nacional"
    val, anyo = first_val(s)
    rows.append({"geo": geo, "regimen_tenencia": cat, "porcentaje_hogares": val, "anyo": anyo})
dft = pd.DataFrame(rows)
dft.to_csv(f"{OUT}/ecv_tenencia_vivienda_ccaa.csv", index=False)
print("\n--- ECV tenencia (Total Nacional) ---")
print(dft[dft['geo']=='Total Nacional'].to_string())
print("anyo max:", dft['anyo'].max())

# Compute absolute households in "Propiedad" nationally using ECP national household total for same year if possible
hh_total_national = df_nac[df_nac['tamano_hogar']=='Total']['valor'].iloc[0]
pct_propiedad = dft[(dft['geo']=='Total Nacional') & (dft['regimen_tenencia']=='Propiedad')]['porcentaje_hogares'].iloc[0]
hogares_propietarios = hh_total_national * pct_propiedad/100
print(f"\nHogares totales (ECP, Jul2026-ish): {hh_total_national}")
print(f"% Propiedad (ECV, ultimo anio): {pct_propiedad}")
print(f"Hogares propietarios (estimado, cruzando ECP x ECV): {hogares_propietarios:,.0f}")

with open(f"{OUT}/resumen_hogares_tenencia.txt","w") as f:
    f.write(f"Hogares totales nacional (ECP): {hh_total_national}\n")
    f.write(f"Porcentaje en propiedad (ECV, ultimo anio disponible): {pct_propiedad}%\n")
    f.write(f"Hogares propietarios estimados (ECP total x ECV%): {hogares_propietarios:,.0f}\n")
    f.write("NOTA: cruce de dos operaciones distintas (ECP y ECV) con fechas de referencia distintas; ver ficha para detalle de vintage.\n")
