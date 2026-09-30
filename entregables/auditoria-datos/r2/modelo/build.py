"""Construye el HTML final a partir de plantilla.html y salida/resultados.json.

Sustituye {{clave}} por cifras formateadas en español y deja los datos del
laboratorio de hipótesis en window.R. Uso: python build.py [ruta_salida]
"""
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
R = json.loads((AQUI / "salida/resultados.json").read_text())
C = R["constantes"]
E = {e["clave"]: e for e in R["escenarios"]}
B = R["modelo_b"]
K = R["coste_m2"]
N = R["necesidad"]
PROV = {p["k"]: p for p in R["provincias"]}


def num(x, d=0):
    if d < 0:
        x, d = round(x, d), 0
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def mill(x, d=1):  # 21,6 millones
    return f"{num(x / 1e6, d)} millones"


def bill(x, d=2):  # euros en billones
    return f"{num(x / 1e12, d)} billones de €"


def mm(x):  # miles de millones como millones
    return f"{num(x / 1e6, 0)} millones de €"


def pct(x, d=1):
    return f"{num(x * 100, d)} %"


V = {}
# demografía y parque
V["adultos"] = mill(C["ADULTOS"])
V["adultos_n"] = num(C["ADULTOS"])
V["adultos_esp"] = mill(C["ADULTOS_ESP"])
V["hogares"] = mill(C["HOGARES"], 2)
V["jovenes_padres_pct"] = pct(C["JOVENES_CON_PADRES"])
V["jovenes_padres_n"] = mill(C["JOVENES_CON_PADRES_N"])
V["principales"] = mill(C["PRINCIPALES_2025"], 2)
V["no_principales"] = mill(C["NO_PRINCIPALES_2025"], 2)
V["parque_total"] = mill(C["PRINCIPALES_2025"] + C["NO_PRINCIPALES_2025"], 1)
V["vacias"] = mill(C["VACIAS_2021"], 2)
V["pct_propiedad"] = pct(C["PCT_PROPIEDAD"])
V["crec_adultos"] = num(C["crec_adultos_anual"], -3)
V["crec_hogares"] = num(C["crec_hogares_anual"], -3)
# módulo y costes
M = R["modulo"]
V["mod_util"] = num(M["m2_util"])
V["mod_c"] = num(M["m2c"], 1)
V["pem"] = num(K["pem"])
V["sin_suelo"] = num(K["sin_suelo_sin_iva"])
V["suelo_nac_m2c"] = num(K["suelo_nacional_m2c"])
V["total_nac_m2c"] = num(K["total_nacional_m2c"])
V["modulo_construir_nac"] = num(K["total_nacional_m2c"] * M["m2c"], -3)
V["vt_nac"] = num(K["valor_tasado_nacional"])
V["vt_madrid"] = num(K["madrid"]["valor_tasado"])
V["vt_madrid_cap"] = num(K["madrid"]["valor_capital"])
V["coste_madrid"] = num(K["madrid"]["coste"])
V["precio_medio"] = num(K["precio_medio_ponderado"])
V["modulo_precio_medio"] = num(K["precio_medio_ponderado"] * M["m2c"], -3)
V["horas_m2"] = num(K["horas_m2"], 1)
V["horas_modulo"] = num(K["horas_modulo"], -1)
V["madrid_brecha_m2"] = num(K["madrid"]["valor_capital"] - K["madrid"]["coste"])
for i, p in enumerate(K["partidas"]):
    V[f"partida{i}"] = num(p["eur_m2"])
# escenarios
for k, e in E.items():
    V[f"{k}_construir"] = mill(e["unidades_construir"])
    V[f"{k}_capital"] = bill(e["coste_capital"])
    V[f"{k}_capital_pib"] = pct(e["coste_capital_pib"], 0)
    V[f"{k}_capital_pibx"] = num(e["coste_capital_pib"], 1)
    V[f"{k}_sanidades"] = num(e["coste_capital_sanidades"], 0)
    V[f"{k}_anios_max"] = num(e["anios_ritmo_max"], 0)
    V[f"{k}_anios_act"] = num(e["anios_ritmo_actual"], 0)
    V[f"{k}_anual"] = mm(e["anual_total"])
    V[f"{k}_anual_pib"] = pct(e["anual_total_pib"])
    V[f"{k}_anual_sanidad"] = num(e["anual_vs_sanidad"], 1)
    V[f"{k}_irpf"] = num(e["factor_irpf"], 2)
    V[f"{k}_irpf_pct"] = pct(e["factor_irpf"], 0)
    V[f"{k}_irpf_total"] = num(1 + e["factor_irpf"], 1)
    V[f"{k}_iva"] = num(e["puntos_iva"], 0)
    V[f"{k}_por_adulto"] = num(e["por_adulto_anual"], -1)
    V[f"{k}_mant"] = mm(e["mantenimiento_anual"])
    V[f"{k}_altas"] = mm(e["altas_anual"])
    V[f"{k}_amort"] = mm(e["coste_capital"] / e["anios_financiacion"])
    V[f"{k}_interes"] = mm(e["intereses_si_deuda"])
    V[f"{k}_interes_pib"] = pct(e["intereses_si_deuda_pib"])
    V[f"{k}_deuda_pib"] = pct(e["deuda_pib_si_deuda"], 0)
V["teorico_esp"] = bill(R["coste_teorico_solo_espanoles"])
V["sin_suelo_teo"] = mill(N["sin_suelo_teorico"])
V["sin_suelo_plaus"] = mill(N["sin_suelo_plausible"])
V["siu"] = mill(N["siu_pendientes"], 2)
V["sustitucion"] = num(N["sustitucion"])
V["ritmo_max"] = num(597632)
V["ritmo_act"] = num(80792)
V["ritmo10"] = mill(E["teorico"]["unidades_construir"] / 10, 2)
md = PROV["madrid"]
V["mad_adultos"] = mill(md["adultos"], 2)
V["mad_princ"] = mill(md["principales"], 2)
V["mad_nec"] = mill(md["necesidad_teorica"], 2)
V["mad_siu"] = num(md["siu_pendientes"])
V["mad_cubre"] = pct(md["siu_pendientes"] / md["necesidad_teorica"], 0)
V["mad_nec_plaus"] = num(md["necesidad_plausible"], -3)
bc = PROV["barcelona"]
V["bcn_nec"] = mill(bc["necesidad_teorica"], 2)
V["bcn_siu"] = num(bc["siu_pendientes"])
# fiscal
V["pib"] = bill(C["PIB"])
V["sanidad"] = mm(C["SANIDAD"])
V["irpf"] = mm(C["IRPF_2025"])
V["iva"] = mm(C["IVA_2025"])
V["gasto_aapp"] = mm(C["GASTO_AAPP"])
V["deuda_pib"] = "100,7 %"  # Eurostat PDE 2025
V["declarantes"] = mill(C["DECLARANTES"])
V["iva_punto"] = mm(R["hipotesis"]["iva_recaudacion_por_punto_eur"]["valor"])
V["vivienda_cofog"] = mm(C["VIVIENDA_COFOG"])
# modelo B
V["b_viv"] = num(B["viviendas_anio"])
V["b_m2"] = num(B["m2c"])
V["b_pv_m2"] = num(B["precio_venta_m2"])
V["b_pv_ud"] = num(B["precio_venta_ud"], -3)
V["b_pm_ud"] = num(B["precio_mercado_ud"], -3)
V["b_sub_ud"] = num(B["subvencion_ud"], -3)
V["b_coste"] = mm(B["coste_anual"])
V["b_coste_pib"] = pct(B["coste_anual_pib"], 2)
V["b_sg_pib"] = pct(B["singapur_deficit_pib"], 2)
V["b_anios_def"] = num(B["anios_cerrar_deficit_bde"], 0)
V["b_ritmo_total"] = num(B["ritmo_total_con_mercado"])
V["b_sin_suelo"] = mm(B["coste_anual_sin_suelo"])
V["ratio_ab"] = num(E["teorico"]["anual_total"] / B["coste_anual"], 0)
V["ratio_ab_plaus"] = num(E["plausible"]["anual_total"] / B["coste_anual"], 0)
V["fecha"] = "28 de septiembre de 2026"


# ---- r2: calendario, flujos, comparativas, Singapur, mapa
CAL = R["calendario"]; FL = R["flujo"]; CMP = R["comparativas"]; SG = R["singapur_vs_espana"]
DECL = C["DECLARANTES"]
for k in ("teorico", "plausible", "minimo", "brecha"):
    f1, f2 = CAL[k]["fase1"], CAL[k]["fase2"]
    V[f"{k}_f1"] = mm(f1["total"]); V[f"{k}_f1_pib"] = pct(f1["pib"])
    V[f"{k}_f1_adulto"] = num(f1["por_adulto"], -1); V[f"{k}_f1_mes"] = num(f1["por_adulto"] / 12, 0)
    V[f"{k}_f1_decl"] = num(f1["total"] / DECL, -1)
    V[f"{k}_f2"] = mm(f2["total"]); V[f"{k}_f2_pib"] = pct(f2["pib"])
    V[f"{k}_f2_adulto"] = num(f2["por_adulto"], -1); V[f"{k}_f2_mes"] = num(f2["por_adulto"] / 12, 0)
    V[f"{k}_f2_decl"] = num(f2["total"] / DECL, -1)
    for n in ("pensiones", "sanidad", "educacion", "defensa"):
        V[f"{k}_cap_{n}"] = num(E[k]["coste_capital"] / CMP[n], 0)
        V[f"{k}_f1_x_{n}"] = num(f1["total"] / CMP[n], 1)
        V[f"{k}_f2_x_{n}"] = num(f2["total"] / CMP[n], 2)
V["teorico_f2_mant"] = mm(CAL["teorico"]["fase2"]["mantenimiento"]); V["teorico_f2_nuevos"] = mm(CAL["teorico"]["fase2"]["nuevos"])
V["fl_18"] = num(FL["cumplen18"], -3); V["fl_mig"] = num(FL["saldo_exterior_adultos"], -3)
V["fl_def"] = num(FL["defunciones"], -3); V["fl_neto"] = num(FL["neto_observado"], -3)
V["fl_proy"] = num(FL["neto_proyectado"], -3); V["fl_30"] = num(C["crec_adultos_30"], -3); V["fl_anio_def"] = str(FL["anio_defunciones"])
for n in ("pensiones", "sanidad", "educacion", "defensa"):
    V["cmp_" + n] = mm(CMP[n])
V["sg_pob"] = mill(SG["pob"], 2); V["sg_res"] = mill(SG["residentes"], 2); V["es_pob"] = mill(SG["pob_es"], 1)
V["sg_pob_x"] = num(SG["pob_es"] / SG["pob"], 0); V["sg_area"] = num(SG["area"], 0); V["es_area"] = num(SG["area_es"])
V["sg_area_x"] = num(SG["area_es"] / SG["area"], 0); V["sg_dens"] = num(SG["dens"], -1); V["es_dens"] = num(SG["dens_es"], 0)
V["sg_dens_x"] = num(SG["dens"] / SG["dens_es"], 0)
V["sg_ppp"] = num(SG["ppp"], -2); V["es_ppp"] = num(SG["ppp_es"], -2); V["sg_ppp_x"] = num(SG["ppp"] / SG["ppp_es"], 1)
V["sg_renta_mes"] = num(SG["renta_med_mes_sgd"]); V["sg_renta_anio_eur"] = num(SG["renta_med_mes_sgd"] * 12 / SG["eur_sgd"], -2)
V["sg_eursgd"] = num(SG["eur_sgd"], 2); V["es_renta"] = num(SG["renta_es"])
bto = sum(SG["bto4_woodlands"]) / 2
V["sg_bto4"] = num(bto, -3); V["sg_bto_anios"] = num(bto / (SG["renta_med_mes_sgd"] * 12), 1)
V["es_70_anios"] = num(SG["viv_es_70m2"] / SG["renta_es"], 1)
V["sg_bto_mil"] = num(SG["bto_lanzados_2024"] / SG["pob"] * 1000, 1); V["b_mil"] = num(100000 / SG["pob_es"] * 1000, 1)
V["sg_bto_equiv"] = num(SG["bto_lanzados_2024"] / SG["pob"] * SG["pob_es"], -3)

# tabla IRPF
filas = []
for t in R["tramos_irpf"]:
    if t["cuota_actual"] < 1:
        continue
    filas.append(
        f'<tr><td>{t["tramo"].replace("(", "").replace("]", "").replace(" - ", "–")} €</td>'
        f'<td class="n">{num(t["declarantes"])}</td><td class="n">{num(t["cuota_actual"])}</td>'
        f'<td class="n neg">+{num(t["extra_teorico"])}</td><td class="n neg">+{num(t["extra_plausible"])}</td></tr>')
V["tabla_irpf"] = "\n".join(filas)

# tabla de hipótesis
tipo_lbl = {"dato": "Dato", "derivado": "Cálculo propio", "hipotesis": "Hipótesis"}
hf = []
for k, h in R["hipotesis"].items():
    val = h["valor"]
    if isinstance(val, dict):
        val = " · ".join(f"{a}: {b}" for a, b in val.items())
    elif isinstance(val, float) and val < 1:
        val = pct(val, 1)
    elif isinstance(val, (int, float)):
        val = num(val, 2 if isinstance(val, float) and val < 100 else 0)
    rango = h.get("rango")
    rs = ""
    if rango:
        rs = " – ".join(pct(x, 1) if isinstance(x, float) and x < 1 else num(x, 0 if x >= 100 else 2) for x in rango)
    hf.append(f'<tr><td><span class="tag t-{h["tipo"]}">{tipo_lbl[h["tipo"]]}</span></td><td>{k.replace("_", " ")}</td>'
              f'<td class="n">{val}</td><td class="n">{rs}</td><td>{h["fuente"]}</td></tr>')
V["tabla_hipotesis"] = "\n".join(hf)

# datos compactos para gráficos y laboratorio
lab = dict(
    A=C["ADULTOS"], H=sum(p["hogares_plausibles"] for p in R["provincias"]), PR=C["PRINCIPALES_2025"],
    NP=C["NO_PRINCIPALES_2025"], SUST=N["sustitucion"], PIB=C["PIB"], SAN=C["SANIDAD"], IRPF=C["IRPF_2025"],
    DEUDA=C["DEUDA"], DECL=C["DECLARANTES"], IVAP=R["hipotesis"]["iva_recaudacion_por_punto_eur"]["valor"],
    PRECIO=K["precio_medio_ponderado"], CONSTR=K["total_nacional_m2c"], SINSUELO=K["sin_suelo_sin_iva"],
    M2PLAUS=sum(p["coste_plausible"] / p["precio_modulo_m2"] for p in R["provincias"]) / sum(p["hogares_plausibles"] for p in R["provincias"]),
    OWN=C["HOGARES"] * C["PCT_PROPIEDAD"], CRECA=C["crec_adultos_anual"], CRECH=C["crec_hogares_anual"],
    RATIO=R["hipotesis"]["ratio_util_construida"]["valor"], INT=R["hipotesis"]["tipo_interes_deuda"]["valor"],
    series=R["series"], partidas=K["partidas"], sueloNac=K["suelo_nacional_m2c"], iva=0.10,
    prov=[dict(n=p["provincia"], a=p["adultos"], pr=p["principales"], nec=p["necesidad_teorica"],
               siu=p["siu_pendientes"], pm=p["precio_modulo_m2"]) for p in R["provincias"]],
    esc={k: dict(cap=e["coste_capital"], anual=e["anual_total"], pib=e["anual_total_pib"]) for k, e in E.items()},
    B=dict(coste_pib=B["coste_anual_pib"], sg=B["singapur_deficit_pib"]),
    cal={k: [dict(a=f["anio"], am=f["amortizacion"], m=f["mantenimiento"], n=f["nuevos"], t=f["total"], pa=f["por_adulto"]) for f in CAL[k]["serie"]] for k in ("teorico", "plausible")},
    cmp=CMP, CRECA30=C["crec_adultos_30"], CRECH30=C["crec_hogares_30"],
    N2A=CAL["teorico"]["fase2"]["nuevos"] / (R["modulo"]["m2c"] * K["precio_medio_ponderado"]),
    AVGA1=sum(f["adultos"] for f in CAL["teorico"]["serie"][:30]) / 30, AVGA2=sum(f["adultos"] for f in CAL["teorico"]["serie"][30:]) / len(CAL["teorico"]["serie"][30:]),
    F2={k: CAL[k]["fase2"]["total"] for k in ("teorico", "plausible")}, F1={k: CAL[k]["fase1"]["total"] for k in ("teorico", "plausible")},
    mapa=json.loads((AQUI.parent / "datos/r2/limpio/mapa_provincias.json").read_text()),
    pm={p["k"]: dict(n=p["provincia"], a=p["adultos"], hp=p["hogares_plausibles"], pr=p["principales"], np=p["no_principales"],
                     nt=p["necesidad_teorica"], npl=p["necesidad_plausible"], siu=p["siu_pendientes"]) for p in R["provincias"]},
)

tpl = (AQUI / "plantilla.html").read_text()
faltan = sorted(set(re.findall(r"{{(\w+)}}", tpl)) - set(V))
if faltan:
    sys.exit(f"Faltan claves: {faltan}")
html = re.sub(r"{{(\w+)}}", lambda m: str(V[m.group(1)]), tpl)
html = html.replace("/*__DATOS__*/", "window.R = " + json.dumps(lab, ensure_ascii=False) + ";")
out = Path(sys.argv[1]) if len(sys.argv) > 1 else AQUI / "salida/index.html"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(html)
print("escrito", out, len(html), "bytes")
