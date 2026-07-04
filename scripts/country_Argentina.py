"""
Country profile: Argentina
Reads the Phase 2 cleaned dataset (data/latam_finanzas_clean.csv) and prints
a statistical profile for respondents in Argentina.
"""

import pandas as pd

CSV_PATH = "data/latam_finanzas_clean.csv"
COUNTRY = "Argentina"

GASTO_COLS = [
    "gasto_vivienda_usd",
    "gasto_alimentacion_usd",
    "gasto_transporte_usd",
    "gasto_entretenimiento_usd",
    "gasto_educacion_usd",
    "gasto_salud_usd",
]


def main():
    df = pd.read_csv(CSV_PATH)
    d = df[df["pais"] == COUNTRY].copy()

    n = len(d)
    edad_min, edad_max = d["edad"].min(), d["edad"].max()

    ingreso = d["ingreso_mensual_usd"]
    ingreso_median = ingreso.median()
    ingreso_mean = ingreso.mean()
    ingreso_min = ingreso.min()
    ingreso_max = ingreso.max()
    ingreso_std = ingreso.std()

    housing_pct = (d["gasto_vivienda_usd"] / d["ingreso_mensual_usd"] * 100).mean()

    spending_breakdown = {}
    for col in GASTO_COLS:
        spending_breakdown[col] = (d[col] / d["ingreso_mensual_usd"] * 100).mean()

    ahorro_mean = d["ahorro_mensual_usd"].mean()
    pct_negative_savings = (d["ahorro_mensual_usd"] < 0).mean() * 100

    ia_horas_mean = d["horas_herramientas_ia_semana"].mean()
    satisfaccion_mean = d["satisfaccion_financiera"].mean()

    industria_mode = d["industria"].mode().iloc[0]
    industria_count = (d["industria"] == industria_mode).sum()

    ocupacion_mode = d["ocupacion"].mode().iloc[0]
    ocupacion_count = (d["ocupacion"] == ocupacion_mode).sum()

    meta_mode = d["meta_financiera"].mode().iloc[0]
    meta_count = (d["meta_financiera"] == meta_mode).sum()

    deuda_mean = d["deuda_total_usd"].mean()
    pct_con_deuda = d["tiene_deuda"].mean() * 100

    print(f"=== Country profile: {COUNTRY} ===")
    print()
    print(f"1. Sample size: {n}")
    print(f"   Age range: {edad_min} - {edad_max}")
    print()
    print("2. Income (USD):")
    print(f"   Median: {ingreso_median:.2f}")
    print(f"   Mean:   {ingreso_mean:.2f}")
    print(f"   Min:    {ingreso_min:.2f}")
    print(f"   Max:    {ingreso_max:.2f}")
    print(f"   Std:    {ingreso_std:.2f}")
    print()
    print(f"3. Housing burden (avg gasto_vivienda_usd as % of ingreso_mensual_usd): {housing_pct:.2f}%")
    print()
    print("4. Spending breakdown (avg % of income):")
    for col, pct in spending_breakdown.items():
        print(f"   {col}: {pct:.2f}%")
    print()
    print("5. Savings:")
    print(f"   Avg ahorro_mensual_usd: {ahorro_mean:.2f}")
    print(f"   % respondents with negative savings: {pct_negative_savings:.2f}%")
    print()
    print("6. AI tools:")
    print(f"   Avg horas_herramientas_ia_semana: {ia_horas_mean:.2f}")
    print(f"   Avg satisfaccion_financiera: {satisfaccion_mean:.2f}")
    print()
    print(f"7. Most common industria: {industria_mode} (count={industria_count})")
    print(f"8. Most common ocupacion: {ocupacion_mode} (count={ocupacion_count})")
    print(f"9. Most common meta_financiera: {meta_mode} (count={meta_count})")
    print()
    print("Additional context for risk assessment:")
    print(f"   Avg deuda_total_usd: {deuda_mean:.2f}")
    print(f"   % respondents with tiene_deuda=True: {pct_con_deuda:.2f}%")


if __name__ == "__main__":
    main()
