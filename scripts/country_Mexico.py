"""
Country profile: Mexico (Mexico)
Reads data/latam_finanzas_clean.csv (Phase 2 cleaned dataset) and computes
summary statistics for the "pais" == "Mexico" subset.

Run standalone:
    python scripts/country_Mexico.py
"""

import pandas as pd

CSV_PATH = "data/latam_finanzas_clean.csv"
COUNTRY = "México"  # Mexico with accented i

GASTO_COLS = [
    "gasto_vivienda_usd",
    "gasto_alimentacion_usd",
    "gasto_transporte_usd",
    "gasto_entretenimiento_usd",
    "gasto_educacion_usd",
    "gasto_salud_usd",
]


def main():
    df = pd.read_csv(CSV_PATH, encoding="utf-8")
    mx = df[df["pais"] == COUNTRY].copy()

    n = len(mx)
    age_min = mx["edad"].min()
    age_max = mx["edad"].max()

    income = mx["ingreso_mensual_usd"]
    income_median = income.median()
    income_mean = income.mean()
    income_min = income.min()
    income_max = income.max()
    income_std = income.std()

    housing_pct = (mx["gasto_vivienda_usd"] / mx["ingreso_mensual_usd"] * 100)
    housing_pct_avg = housing_pct.mean()

    spending_breakdown = {}
    for col in GASTO_COLS:
        pct = (mx[col] / mx["ingreso_mensual_usd"] * 100)
        spending_breakdown[col] = pct.mean()

    ahorro_mean = mx["ahorro_mensual_usd"].mean()
    pct_negative_savings = (mx["ahorro_mensual_usd"] < 0).mean() * 100

    ia_hours_avg = mx["horas_herramientas_ia_semana"].mean()
    satisfaccion_avg = mx["satisfaccion_financiera"].mean()

    industria_mode = mx["industria"].mode().iloc[0]
    industria_count = (mx["industria"] == industria_mode).sum()

    ocupacion_mode = mx["ocupacion"].mode().iloc[0]
    ocupacion_count = (mx["ocupacion"] == ocupacion_mode).sum()

    meta_mode = mx["meta_financiera"].mode().iloc[0]
    meta_count = (mx["meta_financiera"] == meta_mode).sum()

    deuda_mean = mx["deuda_total_usd"].mean()
    pct_con_deuda = mx["tiene_deuda"].mean() * 100

    print(f"=== Country profile: {COUNTRY} ===")
    print()
    print(f"1. Sample size: {n}")
    print(f"   Age range: {age_min}-{age_max}")
    print()
    print("2. Income (USD):")
    print(f"   Median: {income_median:.2f}")
    print(f"   Mean:   {income_mean:.2f}")
    print(f"   Min:    {income_min:.2f}")
    print(f"   Max:    {income_max:.2f}")
    print(f"   Std:    {income_std:.2f}")
    print()
    print(f"3. Housing burden (avg % of income): {housing_pct_avg:.2f}%")
    print()
    print("4. Spending breakdown (avg % of income):")
    for col, val in spending_breakdown.items():
        print(f"   {col}: {val:.2f}%")
    print()
    print("5. Savings:")
    print(f"   Avg ahorro_mensual_usd: {ahorro_mean:.2f}")
    print(f"   % respondents with negative savings: {pct_negative_savings:.2f}%")
    print()
    print("6. AI tools:")
    print(f"   Avg horas_herramientas_ia_semana: {ia_hours_avg:.2f}")
    print(f"   Avg satisfaccion_financiera: {satisfaccion_avg:.2f}")
    print()
    print(f"7. Most common industria: {industria_mode} (n={industria_count})")
    print(f"8. Most common ocupacion: {ocupacion_mode} (n={ocupacion_count})")
    print(f"9. Most common meta_financiera: {meta_mode} (n={meta_count})")
    print()
    print("Additional context:")
    print(f"   Avg deuda_total_usd: {deuda_mean:.2f}")
    print(f"   % with tiene_deuda=True: {pct_con_deuda:.2f}%")


if __name__ == "__main__":
    main()
