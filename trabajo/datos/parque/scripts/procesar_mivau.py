import pandas as pd
import re, sys

RAW = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/parque/raw/mivau"
OUT = "/Users/ivancarrillo/Documents/second-brain/proyectos/vivienda-universal/encargos/viabilidad-vivienda-universal-gratuita/trabajo/datos/parque/limpio"

def load_annual_series(fname, title):
    """For files with a single year per column (10 header row, 11 TOTAL NACIONAL data row onward)."""
    df = pd.read_excel(f"{RAW}/{fname}", header=None)
    # find header row (years) - row containing many floats between 1990-2030
    header_row = None
    for i in range(min(15, len(df))):
        vals = df.iloc[i].tolist()
        numyears = sum(1 for v in vals if isinstance(v,(int,float)) and not pd.isna(v) and 1980<v<2035)
        if numyears > 5:
            header_row = i
            break
    years = df.iloc[header_row].tolist()
    years = [int(y) if isinstance(y,(int,float)) and not pd.isna(y) else None for y in years]
    rows = []
    for i in range(header_row+1, len(df)):
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
    print(f"-> {title}: filas={len(out)} cols_years={[c for c in out.columns if c!='region'][:3]}...{[c for c in out.columns if c!='region'][-3:]}")
    return out

for fname, title in [
    ("32200500.xls","mivau_viviendas_libres_iniciadas_1991_2025"),
    ("32201000.xls","mivau_viviendas_libres_terminadas_1991_2025"),
    ("31303000.xls","mivau_vpo_calificaciones_provisionales_1991_2025"),
    ("31306000.xls","mivau_vpo_calificaciones_definitivas_1991_2025"),
]:
    load_annual_series(fname, title)
