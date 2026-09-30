import pandas as pd

RAW = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/parque/raw/mivau"
OUT = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/parque/limpio"

def process(fname, title, data_start_row=13):
    df = pd.read_excel(f"{RAW}/{fname}", header=None)
    n = df.shape[1]
    # last quarter column = n-3 (last two cols are variaciones)
    last_col = n - 3
    last_year_label = None
    for j in range(last_col, -1, -1):
        v = df.iloc[10, j]
        if isinstance(v, str) and v.strip():
            last_year_label = v.strip()
            break
    last_q_label = df.iloc[12, last_col]
    rows = []
    for i in range(data_start_row, len(df)):
        label = df.iloc[i, 1]
        if isinstance(label, str) and label.strip():
            rows.append({
                "region": label.strip(),
                "precio_eur_m2_ultimo_periodo": df.iloc[i, last_col],
                "periodo": f"{last_year_label} T{last_q_label}",
                "var_trimestral_pct": df.iloc[i, n-2],
                "var_interanual_pct": df.iloc[i, n-1],
            })
    out = pd.DataFrame(rows)
    out.to_csv(f"{OUT}/{title}.csv", index=False)
    print(f"-> {title}: filas={len(out)} periodo={last_year_label} T{last_q_label}")
    return out

process("36400500.xls", "mivau_precio_suelo_urbano_provincias_ultimo_periodo")
process("36403000.xls", "mivau_precio_suelo_urbano_municipios_mas50000_ultimo_periodo")
