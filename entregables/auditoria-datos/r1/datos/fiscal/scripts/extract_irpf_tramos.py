"""
Extrae la tabla de tramos de rendimiento (partidas 595 "Cuota resultante de la
autoliquidacion" y 435 "Base imponible general") de las paginas HTML de la
Estadistica de los declarantes del IRPF 2023 (AEAT), ya descargadas en ../raw/.

IMPORTANTE sobre el formato numerico español en estas tablas AEAT:
- El punto "." es separador de MILES (23.987.211 = veintitres millones...).
- La coma "," es separador DECIMAL, usada solo en columnas de porcentaje.
- La columna "Importe" esta en EUROS (no en miles), pese a que el titulo de la
  tabla indica "(miles de euros)" -- esa anotacion se refiere a los limites de
  los TRAMOS (ej. "(6 - 12]" = 6.000-12.000 euros), no a la columna Importe.
  Se verifico por consistencia: Media * Numero_con_partida ~= Importe.

Uso: python3 extract_irpf_tramos.py
Imprime la tabla decodificada por tramo (declarantes, importe, media).
"""
import re
from pathlib import Path

RAW = Path(__file__).resolve().parent.parent / "raw"

FILES = {
    "cuota_resultante (595)": RAW / "aeat_irpf_2023_595_cuota_resultante_tabla.html",
    "base_imponible_general (435)": RAW / "aeat_irpf_2023_435_baseimponiblegeneral_tabla.html",
}


def parse_es_number(s):
    """Convierte '117.673.789.396' o '5,30' a float, segun formato español."""
    s = s.strip()
    if "," in s:
        return float(s.replace(".", "").replace(",", "."))
    return float(s.replace(".", ""))


def extract_table(html_path):
    html = html_path.read_text(encoding="utf-8", errors="ignore")
    tables = re.findall(r"<table.*?</table>", html, re.S)
    assert tables, f"No se encontro tabla en {html_path}"
    text = re.sub(r"<[^>]+>", "|", tables[0])
    text = re.sub(r"\|+", "|", text)
    return text


if __name__ == "__main__":
    for label, path in FILES.items():
        print(f"=== {label} ({path.name}) ===")
        print(extract_table(path)[:4000])
        print()
