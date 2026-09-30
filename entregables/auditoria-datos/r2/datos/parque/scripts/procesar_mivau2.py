import pandas as pd

RAW = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/parque/raw/mivau"
OUT = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/parque/limpio"

def load_simple_annual(fname, title, header_row, data_start):
    df = pd.read_excel(f"{RAW}/{fname}", header=None)
    years = df.iloc[header_row].tolist()
    years = [int(y) if isinstance(y,(int,float)) and not pd.isna(y) else None for y in years]
    rows = []
    for i in range(data_start, len(df)):
        label = df.iloc[i,1]
        if isinstance(label,str) and label.strip():
            vals = df.iloc[i].tolist()
            rec = {"region": label.strip()}
            for y, v in zip(years, vals):
                if y is not None:
                    rec[str(y)] = v
            rows.append(rec)
    out = pd.DataFrame(rows)
    out.to_csv(f"{OUT}/{title}.csv", index=False)
    ycols = [c for c in out.columns if c != 'region']
    print(f"-> {title}: filas={len(out)} years {ycols[0]}..{ycols[-1]}")
    return out

# Estimacion parque de viviendas: total por CCAA/provincia (2001-?)
load_simple_annual("33100500.xls", "mivau_parque_viviendas_total_ccaa_provincia_2001_", 11, 13)

print("--- checking 33102000 structure (multi-index Total/Principales/No principales per year) ---")
df = pd.read_excel(f"{RAW}/33102000.xls", header=None)
print(df.shape)
print(df.iloc[11,:10].tolist())
print(df.iloc[12,:10].tolist())
print(df.iloc[13,:10].tolist())
print(df.iloc[14,:10].tolist())
