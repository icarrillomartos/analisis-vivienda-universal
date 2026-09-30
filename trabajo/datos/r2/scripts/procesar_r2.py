"""Limpieza de los datos añadidos en la revisión r2.

Genera limpio/r2_constantes.json (flujos demográficos, COFOG, Singapur) y
limpio/mapa_provincias.json (trazados SVG simplificados de GISCO NUTS3).
"""
import json, re, math, unicodedata
from pathlib import Path
R = Path(__file__).resolve().parent.parent / "raw"
L = Path(__file__).resolve().parent.parent / "limpio"

def cofog():
    d = json.load(open(R / "eurostat_cofog_es_2023.json"))
    dims, sizes = d["id"], d["size"]
    inv = {k: {v: kk for kk, v in d["dimension"][k]["category"]["index"].items()} for k in dims}
    out = {}
    for key, val in d["value"].items():
        i, idx = int(key), []
        for s in reversed(sizes):
            idx.append(i % s); i //= s
        idx = list(reversed(idx))
        lab = {dims[j]: inv[dims[j]][idx[j]] for j in range(len(dims))}
        out.setdefault(lab["cofog99"], {})[lab["unit"]] = val
    return out

def migracion_adultos():
    m = json.load(open(R / "ine_saldos_migratorios_69759.json"))
    tot = 0
    for s in m:
        n = s["Nombre"]
        if n.startswith("Total. ") and ". Total. Saldo exterior" in n and "Todas las edades" not in n:
            g = re.search(r"De (\d+) a (\d+)|(\d+) y m", n)
            v = [x["Valor"] for x in s["Data"] if x["Anyo"] == 2024][0]
            lo = int(g.group(1) or g.group(3))
            tot += v if lo >= 20 else (v * 0.4 if lo == 15 else 0)
    return tot

def defunciones():
    d = json.load(open(R / "ine_defunciones_6545.json"))
    for s in d:
        if s["Nombre"].startswith("Total Nacional. Defunción. Total."):
            return {x["Anyo"]: x["Valor"] for x in s["Data"]}

wb = json.load(open(R / "wb_gdp_pc_ppp.json"))[1]
ppp = {(r["countryiso3code"], int(r["date"])): r["value"] for r in wb if r["value"]}
ecb = [l.split(",") for l in open(R / "ecb_eur_sgd.csv").read().splitlines()[1:]]
tc = float(ecb[-1][7]); tc_mes = ecb[-1][6]
area = json.load(open(R / "sg_d_0b2c034da121ef8efc71949af1694b4d.json"))["result"]["records"][0]
inc = json.load(open(R / "sg_d_d31bb77bd99f8305e6c65b61d9762617.json"))["result"]["records"][-1]
ecv = json.load(open(R / "ine_ecv_renta_hogar_9949.json"))
renta_es = [s["Data"][0]["Valor"] for s in ecv if s["Nombre"].startswith("Total Nacional. Renta neta media por hogar")][0]
area_es = json.load(open(R / "eurostat_reg_area3_es.json"))["value"]["13"]
cons = dict(
    cofog_2023=cofog(), saldo_exterior_adultos_2024=migracion_adultos(), defunciones=defunciones(),
    ppp_esp_2025=ppp[("ESP", 2025)], ppp_sgp_2025=ppp[("SGP", 2025)], eur_sgd=tc, eur_sgd_mes=tc_mes,
    sg_area_km2=float(area["2025"]), es_area_km2=area_es,
    sg_renta_hogar_mediana_mes_sgd=float(inc["ResidentHouseholds_Median1"]),
    sg_renta_hogar_media_mes_sgd=float(inc["ResidentHouseholds_Average"]), sg_renta_anio=inc["Dollar"],
    es_renta_neta_media_hogar=renta_es,
)
json.dump(cons, open(L / "r2_constantes.json", "w"), ensure_ascii=False, indent=1)

# ------------------------------------------------ mapa
def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z ]", " ", s)).strip()

ISLAS = {"ES531": "balears", "ES532": "balears", "ES533": "balears",
         "ES703": "santa cruz de tenerife", "ES704": "palmas", "ES705": "palmas", "ES706": "santa cruz de tenerife",
         "ES707": "santa cruz de tenerife", "ES708": "palmas", "ES709": "santa cruz de tenerife"}
ALIAS = {"araba alava": "alava", "alicante alacant": "alicante", "castellon castello": "castellon",
         "valencia valencia": "valencia", "a coruna": "coruna", "la rioja": "rioja", "asturias": "asturias",
         "cantabria": "cantabria", "navarra": "navarra", "region de murcia": "murcia", "murcia": "murcia",
         "madrid": "madrid", "gipuzkoa": "gipuzkoa", "bizkaia": "bizkaia"}

def dp(pts, eps):
    if len(pts) < 3: return pts
    a, b = pts[0], pts[-1]
    dmax, idx = 0, 0
    for i in range(1, len(pts) - 1):
        x0, y0 = pts[i]; x1, y1 = a; x2, y2 = b
        num = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
        den = math.hypot(y2 - y1, x2 - x1) or 1e-12
        d = num / den
        if d > dmax: dmax, idx = d, i
    if dmax > eps:
        return dp(pts[:idx + 1], eps)[:-1] + dp(pts[idx:], eps)
    return [a, b]

g = json.load(open(R / "gisco_nuts3_2024_10m.geojson"))
K = math.cos(math.radians(40))
def proj(lon, lat, canarias):
    if canarias:  # inset: desplaza Canarias al suroeste de la península
        lon, lat = lon + 5.5, lat + 7.2
    return (lon * K, -lat)
feats = {}
for f in g["features"]:
    p = f["properties"]
    if p.get("CNTR_CODE") != "ES": continue
    code = p["NUTS_ID"]
    k = ISLAS.get(code) or ALIAS.get(norm(p["NUTS_NAME"]), norm(p["NUTS_NAME"]))
    can = code.startswith("ES70")
    geom = f["geometry"]
    polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
    for poly in polys:
        ring = [proj(x, y, can) for x, y in poly[0]]
        mid = len(ring) // 2
        ring = dp(ring[:mid + 1], 0.012)[:-1] + dp(ring[mid:], 0.012)
        if len(ring) >= 4:
            feats.setdefault(k, {"nombre": p["NUTS_NAME"], "rings": []})["rings"].append(ring)
xs = [x for v in feats.values() for r in v["rings"] for x, _ in r]
ys = [y for v in feats.values() for r in v["rings"] for _, y in r]
minx, miny = min(xs), min(ys); W = 800; s = W / (max(xs) - minx); H = (max(ys) - miny) * s
out = {"w": W, "h": round(H), "prov": {}}
for k, v in feats.items():
    d = " ".join("M" + " L".join(f"{(x - minx) * s:.1f},{(y - miny) * s:.1f}" for x, y in r) + "Z" for r in v["rings"])
    out["prov"][k] = {"d": d, "n": v["nombre"]}
# recuadro de Canarias
cx = [x for k in ("palmas", "santa cruz de tenerife") for r in feats[k]["rings"] for x, _ in r]
cy = [y for k in ("palmas", "santa cruz de tenerife") for r in feats[k]["rings"] for _, y in r]
out["canarias"] = [round((min(cx) - minx) * s - 8), round((min(cy) - miny) * s - 8), round((max(cx) - min(cx)) * s + 16), round((max(cy) - min(cy)) * s + 16)]
json.dump(out, open(L / "mapa_provincias.json", "w"), ensure_ascii=False)
print(len(out["prov"]), "provincias ·", round(len(json.dumps(out)) / 1024), "KB ·", json.dumps(cons)[:300])
