"""Modelo de viabilidad: vivienda gratuita universal (modelo A) frente a vivienda
a precio fijo al estilo de Singapur (modelo B).

Lee las tablas limpias de trabajo/datos/*/limpio y las hipótesis de
hipotesis.json. Escribe resultados.json y tablas CSV en trabajo/modelo/salida/.
Requiere pandas y xlrd. Ejecutar desde cualquier carpeta:
    python modelo.py
"""
import json
import re
import unicodedata
from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parent
DATOS = AQUI.parent / "datos"
SALIDA = AQUI / "salida"
SALIDA.mkdir(exist_ok=True)

H = {k: v for k, v in json.loads((AQUI / "hipotesis.json").read_text()).items() if not k.startswith("_")}


def hv(k):
    return H[k]["valor"]


# ---------------------------------------------------------------- nombres
ALIAS = {
    "araba alava": "alava", "alava": "alava", "gipuzkoa": "gipuzkoa", "guipuzcoa": "gipuzkoa",
    "bizkaia": "bizkaia", "vizcaya": "bizkaia", "asturias principado de": "asturias",
    "asturias ppdo de": "asturias", "asturias": "asturias", "balears illes": "balears",
    "illes balears": "balears", "balears": "balears", "madrid comunidad de": "madrid", "madrid": "madrid",
    "murcia region de": "murcia", "murcia": "murcia", "navarra comunidad foral de": "navarra",
    "navarra": "navarra", "rioja la": "rioja", "la rioja": "rioja", "rioja": "rioja",
    "coruna a": "coruna", "a coruna": "coruna", "coruna": "coruna", "palmas las": "palmas",
    "las palmas": "palmas", "palmas": "palmas", "cantabria": "cantabria",
    "alicante alacant": "alicante", "castellon castello": "castellon", "valencia valencia": "valencia",
    "avila": "avila",
}


def norm(s):
    s = unicodedata.normalize("NFKD", str(s)).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return ALIAS.get(s, s)


# ---------------------------------------------------------------- datos
dem = pd.read_csv(DATOS / "demografia/limpio/poblacion_18mas_por_provincia_ECP.csv")
dem["k"] = dem["provincia_o_ambito"].map(norm)
nac = pd.read_csv(DATOS / "demografia/limpio/poblacion_18mas_por_provincia_y_nacionalidad_APROX.csv")
nac["k"] = nac["geo"].map(norm)
esp = nac[nac.nacionalidad == "Española"].set_index("k")["poblacion_18mas_aprox"]

hog = pd.read_csv(DATOS / "demografia/limpio/hogares_provincia_tamano.csv")
hog["k"] = hog["geo"].map(norm)
hogp = hog.pivot_table(index="k", columns="tamano_hogar", values="valor", aggfunc="sum")

edad = pd.read_csv(DATOS / "demografia/limpio/raw_poblacion_provincia_edadsimple.csv")
edad = edad[edad.sexo == "Total"].copy()
edad["n"] = edad["edad"].str.extract(r"^(\d+)").astype(float)
edad["k"] = edad["geo"].map(norm)
p1834 = edad[(edad.n >= 18) & (edad.n <= 34)].groupby("k")["Valor"].sum()

parque = pd.read_csv(DATOS / "parque/limpio/mivau_parque_viviendas_tipo_ccaa_provincia_2001_2025.csv")
parque["k"] = parque["region"].map(norm)
parque = parque.drop_duplicates("k", keep="last").set_index("k")

siu = pd.read_csv(DATOS / "parque/limpio/siu_areas_desarrollo_por_provincia.csv")
siu["k"] = siu["DenProv"].map(norm)
siu = siu.set_index("k")

suelo = pd.read_csv(DATOS / "parque/limpio/mivau_precio_suelo_urbano_provincias_ultimo_periodo.csv")
suelo["k"] = suelo["region"].map(norm)
suelo = pd.to_numeric(suelo.drop_duplicates("k", keep="last").set_index("k")["precio_eur_m2_ultimo_periodo"], errors="coerce").dropna()

xl = pd.ExcelFile(DATOS / "costes/raw/mivau_valor_tasado_nacional_serie.xls")
vt_raw = pd.read_excel(xl, sheet_name=xl.sheet_names[-1], header=None)
vt = {}
for _, r in vt_raw.iloc[14:78].iterrows():
    if pd.notna(r[1]) and pd.notna(r[15]):
        vt[norm(r[1])] = float(r[15])  # 2T 2026
vt = pd.Series(vt)

irpf = pd.read_csv(DATOS / "fiscal/limpio/07_irpf_tramos_2023.csv")

ter = pd.read_csv(DATOS / "parque/limpio/mivau_viviendas_libres_terminadas_1991_2025.csv")
ini = pd.read_csv(DATOS / "parque/limpio/mivau_viviendas_libres_iniciadas_1991_2025.csv")
vpo = pd.read_csv(DATOS / "parque/limpio/mivau_vpo_calificaciones_provisionales_1991_2025.csv")
vts = pd.read_csv(DATOS / "costes/limpio/mivau_valor_tasado_serie_nacional_y_provincias_anual.csv")
eman = pd.read_csv(DATOS / "demografia/limpio/eurostat_yth_demo_030_edad_emancipacion.csv")
lvps = pd.read_csv(DATOS / "demografia/limpio/eurostat_ilc_lvps08_jovenes_con_padres.csv")
proy_ad = pd.read_csv(DATOS / "demografia/limpio/proyeccion_poblacion_18mas_nacional_2026_2039.csv")
proy_h = pd.read_csv(DATOS / "demografia/limpio/proyeccion_hogares_ccaa_tamano_2026_2041.csv")

# ---------------------------------------------------------------- constantes oficiales (fichas)
PIB = 1_690_012e6            # INE CNTR 2025
GASTO_AAPP = 764_884e6       # Eurostat/IGAE 2025
DEUDA = 1_698_224.6e6        # Eurostat PDE 2025
SANIDAD = 101_739e6          # Ministerio de Sanidad 2024
IRPF_2025 = 142_466e6        # AEAT 2025
IVA_2025 = 99_532e6          # AEAT 2025
RECAUD_AEAT = 325_356e6      # AEAT 2025
IBI = 14_820.9e6             # Hacienda 2023
VIVIENDA_COFOG = 3_588e6     # Eurostat 2023 GF0601+GF1006
ADULTOS = 42_009_991         # INE ECP 1-7-2026
HOGARES = 19_874_860         # INE ECP 1-7-2026
PCT_PROPIEDAD = 0.733        # INE ECV 2025
JOVENES_CON_PADRES = 0.687   # Eurostat ilc_lvps08 2025 (18-34)
HDB_DEFICIT_SGD = 6_339.012e6
SG_PIB_SGD = 765_497.5e6
VACIAS_2021 = 3_837_328
NO_PRINC_2021 = 8_087_092

# ---------------------------------------------------------------- coste de construir 1 m²
pem = hv("pem_eur_m2c_2024") * (1 + hv("actualizacion_pem_2024_2026"))
partidas = [
    ("Mano de obra (oficiales y peones)", pem * hv("peso_mano_obra_pem")),
    ("Materiales, maquinaria y medios", pem * (1 - hv("peso_mano_obra_pem"))),
    ("Gastos generales (13 %)", pem * hv("gastos_generales_pct_pem")),
    ("Beneficio industrial (6 %)", pem * hv("beneficio_industrial_pct_pem")),
    ("Arquitecto y aparejador", pem * hv("honorarios_tecnicos_pct_pem")),
    ("Seguridad, calidad, seguro decenal",
     pem * (hv("seguridad_salud_pct_pem") + hv("control_calidad_pct_pem") + hv("seguro_decenal_pct_pem"))),
    ("Licencia e ICIO", pem * (hv("icio_pct_pem") + hv("tasas_licencia_pct_pem"))),
]
sub = sum(v for _, v in partidas)
partidas.append(("Financiación y gestión", sub * (hv("financiacion_obra_pct") + hv("gestion_promocion_pct"))))
partidas.append(("Notaría, registro y AJD", sub * hv("notaria_registro_ajd_pct")))
coste_sin_suelo_sin_iva = sum(v for _, v in partidas)


def coste_m2(k, con_iva=True):
    """Coste de construir 1 m² construido en la provincia k, con suelo a precio de mercado."""
    rep_suelo = suelo.get(k, suelo["total nacional"]) / hv("edificabilidad_m2t_m2s")
    base = coste_sin_suelo_sin_iva + rep_suelo
    return base * (1 + hv("iva_vivienda_pct")) if con_iva else base


mano_obra_eur_m2 = pem * hv("peso_mano_obra_pem")
horas_m2 = mano_obra_eur_m2 / hv("coste_hora_oficial_eur")

# ---------------------------------------------------------------- tabla provincial
m2c_1p = hv("modulo_1p_util_m2") / hv("ratio_util_construida")
mod = {s: u / hv("ratio_util_construida") for s, u in hv("modulo_util_por_tamano_hogar").items()}

filas = []
for _, r in dem.iterrows():
    k = r["k"]
    if k in ("total nacional",):
        continue
    kp = "ceuta y melilla" if k in ("ceuta", "melilla") else k
    ad = r["poblacion_18_mas"]
    princ = parque.loc[kp, "2025_Principales"] if kp in parque.index else None
    noprinc = parque.loc[kp, "2025_No"] if kp in parque.index else None
    if kp == "ceuta y melilla":  # MIVAU agrupa Ceuta y Melilla: se reparte por adultos
        tot_cm = dem.loc[dem.k.isin(["ceuta", "melilla"]), "poblacion_18_mas"].sum()
        princ, noprinc = princ * ad / tot_cm, noprinc * ad / tot_cm
    vtp = vt.get(k, vt.get(kp, vt["total nacional"]))
    cm2 = coste_m2(k)
    precio_modulo = max(vtp, cm2)  # no se puede construir por debajo del coste
    hp = hogp.loc[k] if k in hogp.index else None
    jov = p1834.get(k, 0) * JOVENES_CON_PADRES
    hog_plaus = {"1": hp["1"] + jov, "2": hp["2"], "3": hp["3"], "4+": hp["4 y más"]}
    n_hog_plaus = sum(hog_plaus.values())
    siu_pend = siu.loc[k, "Pnvivpnd"] if k in siu.index else 0
    reuso = noprinc * hv("reuso_no_principales_pct")
    nec_teo = max(0.0, ad - princ - reuso)
    nec_plaus = max(0.0, n_hog_plaus - princ - reuso)
    filas.append(dict(
        k=k, provincia=r["provincia_o_ambito"], adultos=ad, adultos_esp=esp.get(k, None),
        hogares=hp["Total"], jovenes_con_padres=jov, hogares_plausibles=n_hog_plaus,
        principales=princ, no_principales=noprinc, valor_tasado=vtp, coste_construir_m2=cm2,
        precio_modulo_m2=precio_modulo, suelo_m2=suelo.get(k, None), siu_pendientes=siu_pend,
        necesidad_teorica=nec_teo, necesidad_plausible=nec_plaus,
        sin_suelo_teorico=max(0.0, nec_teo - siu_pend), sin_suelo_plausible=max(0.0, nec_plaus - siu_pend),
        coste_teorico=ad * m2c_1p * precio_modulo,
        coste_teorico_esp=(esp.get(k, 0) or 0) * m2c_1p * precio_modulo,
        coste_plausible=sum(n * mod[s] for s, n in hog_plaus.items()) * precio_modulo,
        coste_minimo=n_hog_plaus * (hv("modulo_minimo_legal_util_m2") / hv("ratio_util_construida")) * precio_modulo,
        coste_brecha=(hp["Total"] * (1 - PCT_PROPIEDAD) * sum(hp[c] * mod[s] for c, s in (("1", "1"), ("2", "2"), ("3", "3"), ("4 y más", "4+"))) / hp["Total"]
                      + jov * m2c_1p) * precio_modulo,
    ))
P = pd.DataFrame(filas)
P.to_csv(SALIDA / "provincias.csv", index=False)

# ---------------------------------------------------------------- escenarios
sust = hv("sustituir_viviendas_estado_malo")
anios_obra = lambda u: u / hv("ritmo_max_viviendas_anio")
precio_medio_m2 = (P.adultos * P.precio_modulo_m2).sum() / P.adultos.sum()
coste_constr_medio_m2 = (P.adultos * P.coste_construir_m2).sum() / P.adultos.sum()
crec_adultos = (float(proy_ad.loc[proy_ad.anyo == 2030, "poblacion_18mas"].iloc[0]) - ADULTOS) / 3.5
ph = proy_h[(proy_h.tamano_hogar == "Total")]
ccaa_list = ["Andalucía", "Aragón", "Asturias, Principado de", "Balears, Illes", "Canarias", "Cantabria",
             "Castilla y León", "Castilla - La Mancha", "Cataluña", "Comunitat Valenciana", "Extremadura",
             "Galicia", "Madrid, Comunidad de", "Murcia, Región de", "Navarra, Comunidad Foral de",
             "País Vasco", "Rioja, La", "Ceuta", "Melilla"]
phn = ph[ph.geo.isin(ccaa_list)].groupby("anyo")["valor"].sum()
if phn.get(2026, 0) < 15e6:  # si los nombres de CCAA no casan, usar el total publicado en la ficha
    phn = pd.Series({2026: 19.76e6, 2030: 20.61e6})
crec_hogares = (phn[2030] - phn[2026]) / 4


def escenario(nombre, clave, unidades_construir, coste_cap, modulo_m2, altas_anio, parque_publico):
    anios = hv("horizonte_financiacion_anios")
    mant = parque_publico * modulo_m2 * coste_sin_suelo_sin_iva * (hv("mantenimiento_pct_anual") + 1 / hv("vida_util_anios"))
    altas = altas_anio * modulo_m2 * precio_medio_m2
    anual_recurrente = mant + altas
    anual_total = coste_cap / anios + anual_recurrente
    f_irpf = anual_total / IRPF_2025
    return dict(
        nombre=nombre, clave=clave, unidades_construir=unidades_construir,
        coste_capital=coste_cap, coste_capital_pib=coste_cap / PIB,
        coste_capital_sanidades=coste_cap / SANIDAD,
        anios_ritmo_max=anios_obra(unidades_construir),
        anios_ritmo_actual=unidades_construir / hv("ritmo_actual_viviendas_anio"),
        anios_financiacion=anios, mantenimiento_anual=mant, altas_anual=altas,
        recurrente_anual=anual_recurrente, recurrente_pib=anual_recurrente / PIB,
        anual_total=anual_total, anual_total_pib=anual_total / PIB,
        anual_vs_sanidad=anual_total / SANIDAD, anual_vs_gasto_aapp=anual_total / GASTO_AAPP,
        factor_irpf=f_irpf, puntos_iva=anual_total / hv("iva_recaudacion_por_punto_eur"),
        por_adulto_anual=anual_total / ADULTOS,
        intereses_si_deuda=coste_cap * hv("tipo_interes_deuda"),
        intereses_si_deuda_pib=coste_cap * hv("tipo_interes_deuda") / PIB,
        deuda_pib_si_deuda=(DEUDA + coste_cap) / PIB,
    )


u_teo = P.necesidad_teorica.sum() + sust
u_plaus = P.necesidad_plausible.sum() + sust
esc = [
    escenario("Teórico puro: cada adulto, su vivienda", "teorico", u_teo, P.coste_teorico.sum(), m2c_1p,
              crec_adultos, ADULTOS - HOGARES * PCT_PROPIEDAD),
    escenario("Plausible: convivencia real más emancipación", "plausible", u_plaus, P.coste_plausible.sum(),
              sum(mod.values()) / 4, crec_hogares, P.hogares_plausibles.sum() - HOGARES * PCT_PROPIEDAD),
    escenario("Mínimo legal gratis y el resto se paga", "minimo", u_plaus, P.coste_minimo.sum(),
              hv("modulo_minimo_legal_util_m2") / hv("ratio_util_construida"), crec_hogares,
              P.hogares_plausibles.sum() - HOGARES * PCT_PROPIEDAD),
    escenario("Referencia sin compensar a propietarios", "brecha", u_plaus, P.coste_brecha.sum(), sum(mod.values()) / 4,
              crec_hogares, P.hogares_plausibles.sum() - HOGARES * PCT_PROPIEDAD),
]
esc_esp = P.coste_teorico_esp.sum()

# ---------------------------------------------------------------- IRPF por tramos
irpf = irpf[irpf.tramo_rendimiento_eur.str.upper() != "TOTAL"].copy()
escala = IRPF_2025 / irpf.cuota_resultante_autoliquidacion_eur.sum()
irpf["cuota_media_2025"] = irpf.cuota_resultante_autoliquidacion_eur / irpf.num_declarantes_tramo * escala
tramos = []
for _, r in irpf.iterrows():
    d = dict(tramo=r.tramo_rendimiento_eur, declarantes=int(r.num_declarantes_tramo),
             cuota_actual=r.cuota_media_2025)
    for e in esc:
        d["extra_" + e["clave"]] = r.cuota_media_2025 * e["factor_irpf"]
    tramos.append(d)

# ---------------------------------------------------------------- modelo B: Singapur adaptado
n_b = hv("hdb_es_viviendas_anio")
m2_b = hv("hdb_es_m2c")
precio_venta_b = coste_sin_suelo_sin_iva * (1 + 0.04)  # vende a coste sin suelo, IVA superreducido del 4 %
subvencion_ud = (precio_medio_m2 - precio_venta_b) * m2_b
coste_b = n_b * subvencion_ud
suelo_medio = (P.adultos * P.suelo_m2.fillna(suelo["total nacional"])).sum() / P.adultos.sum() / hv("edificabilidad_m2t_m2s")
modelo_b = dict(
    viviendas_anio=n_b, m2c=m2_b, precio_venta_m2=precio_venta_b, precio_venta_ud=precio_venta_b * m2_b,
    precio_mercado_m2=precio_medio_m2, precio_mercado_ud=precio_medio_m2 * m2_b,
    subvencion_ud=subvencion_ud, coste_anual=coste_b, coste_anual_pib=coste_b / PIB,
    coste_anual_sin_suelo=n_b * (coste_sin_suelo_sin_iva * 1.10 - precio_venta_b) * m2_b,
    singapur_deficit_pib=HDB_DEFICIT_SGD / SG_PIB_SGD,
    anios_cerrar_deficit_bde=(700_000) / n_b,
    ritmo_total_con_mercado=n_b + hv("ritmo_actual_viviendas_anio"),
    siu_pendientes_nacional=float(siu["Pnvivpnd"].sum()),
)

# ---------------------------------------------------------------- series para gráficos
def serie(df, region="TOTAL NACIONAL"):
    row = df[df.region == region].iloc[0]
    return {c: (None if pd.isna(row[c]) else float(row[c])) for c in df.columns if c.isdigit()}


series = dict(
    terminadas=serie(ter), iniciadas=serie(ini), vpo=serie(vpo),
    valor_tasado={int(r.anio): r.media_4_trimestres_eur_m2 for r in vts[vts.territorio == "TOTAL NACIONAL"].itertuples()},
    emancipacion={int(r.time): r.value for r in eman.itertuples()},
    jovenes_con_padres={int(r.time): r.value for r in lvps[(lvps.age == "From 18 to 34 years") & (lvps.sex == "Total")].itertuples()},
)

# ---------------------------------------------------------------- guardar
top = P.sort_values("adultos", ascending=False)
res = dict(
    fecha="2026-09-28",
    constantes=dict(PIB=PIB, GASTO_AAPP=GASTO_AAPP, DEUDA=DEUDA, SANIDAD=SANIDAD, IRPF_2025=IRPF_2025,
                    IVA_2025=IVA_2025, RECAUD_AEAT=RECAUD_AEAT, IBI=IBI, VIVIENDA_COFOG=VIVIENDA_COFOG,
                    ADULTOS=ADULTOS, HOGARES=HOGARES, PCT_PROPIEDAD=PCT_PROPIEDAD,
                    JOVENES_CON_PADRES=JOVENES_CON_PADRES, VACIAS_2021=VACIAS_2021, NO_PRINC_2021=NO_PRINC_2021,
                    PRINCIPALES_2025=float(P.principales.sum()), NO_PRINCIPALES_2025=float(P.no_principales.sum()),
                    ADULTOS_ESP=float(P.adultos_esp.sum()), JOVENES_CON_PADRES_N=float(P.jovenes_con_padres.sum()),
                    DECLARANTES=int(irpf.num_declarantes_tramo.sum()), crec_adultos_anual=crec_adultos,
                    crec_hogares_anual=crec_hogares),
    hipotesis=H,
    modulo=dict(m2_util=hv("modulo_1p_util_m2"), m2c=m2c_1p, por_tamano_m2c=mod,
                minimo_m2c=hv("modulo_minimo_legal_util_m2") / hv("ratio_util_construida")),
    coste_m2=dict(pem=pem, partidas=[dict(nombre=n, eur_m2=v) for n, v in partidas],
                  sin_suelo_sin_iva=coste_sin_suelo_sin_iva, horas_m2=horas_m2,
                  horas_modulo=horas_m2 * m2c_1p, anios_trabajo_modulo=horas_m2 * m2c_1p / 1736,
                  suelo_nacional_m2c=suelo["total nacional"] / hv("edificabilidad_m2t_m2s"),
                  total_nacional_m2c=coste_m2("total nacional"), precio_medio_ponderado=precio_medio_m2,
                  coste_construir_medio_ponderado=coste_constr_medio_m2, valor_tasado_nacional=vt["total nacional"],
                  madrid=dict(coste=coste_m2("madrid"), valor_tasado=vt["madrid"], valor_capital=5418.4),
                  suelo_medio_ponderado=suelo_medio),
    escenarios=esc, coste_teorico_solo_espanoles=esc_esp,
    tramos_irpf=tramos, modelo_b=modelo_b, series=series,
    necesidad=dict(teorica=float(u_teo), plausible=float(u_plaus), sustitucion=sust,
                   sin_suelo_teorico=float(P.sin_suelo_teorico.sum()), sin_suelo_plausible=float(P.sin_suelo_plausible.sum()),
                   siu_pendientes=float(P.siu_pendientes.sum())),
    provincias=json.loads(top.to_json(orient="records")),
)
(SALIDA / "resultados.json").write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float))
pd.DataFrame(esc).to_csv(SALIDA / "escenarios.csv", index=False)
pd.DataFrame(tramos).to_csv(SALIDA / "irpf_tramos.csv", index=False)

# resumen en consola
print(f"PEM 2026 {pem:.0f} €/m²c · sin suelo ni IVA {coste_sin_suelo_sin_iva:.0f} · nacional con suelo e IVA {coste_m2('total nacional'):.0f}")
print(f"Precio medio ponderado del módulo {precio_medio_m2:.0f} €/m²c; módulo {m2c_1p:.1f} m²c = {precio_medio_m2*m2c_1p:,.0f} €")
print(f"Horas de mano de obra por m² {horas_m2:.1f}; por módulo {horas_m2*m2c_1p:.0f}")
for e in esc:
    print(f"{e['clave']:10s} construir {e['unidades_construir']/1e6:5.1f} M · capital {e['coste_capital']/1e12:5.2f} B€ ({e['coste_capital_pib']*100:4.0f}% PIB) · "
          f"años {e['anios_ritmo_max']:4.1f} · anual {e['anual_total']/1e9:6.0f} mm€ ({e['anual_total_pib']*100:4.1f}% PIB, x{e['factor_irpf']:.2f} IRPF, {e['puntos_iva']:.0f} pts IVA)")
print("solo españoles teórico", esc_esp / 1e12)
print("sin suelo teórico", P.sin_suelo_teorico.sum() / 1e6, "plausible", P.sin_suelo_plausible.sum() / 1e6)
print("B:", {k: round(v, 3) if isinstance(v, float) else v for k, v in modelo_b.items()})
print(P[["provincia", "adultos", "principales", "necesidad_teorica", "siu_pendientes", "precio_modulo_m2"]].sort_values("adultos", ascending=False).head(8).to_string())
