"""
Country profile: Peru
Reads the Phase 2 cleaned dataset and computes financial wellness metrics
for respondents in Peru.

Run standalone:
    python scripts/country_Peru.py
"""

import pandas as pd

CSV_PATH = "data/latam_finanzas_clean.csv"
COUNTRY = "Perú"

GASTO_COLS = [
    "gasto_vivienda_usd",
    "gasto_alimentacion_usd",
    "gasto_transporte_usd",
    "gasto_entretenimiento_usd",
    "gasto_educacion_usd",
    "gasto_salud_usd",
]

GASTO_LABELS = {
    "gasto_vivienda_usd": "vivienda",
    "gasto_alimentacion_usd": "alimentacion",
    "gasto_transporte_usd": "transporte",
    "gasto_entretenimiento_usd": "entretenimiento",
    "gasto_educacion_usd": "educacion",
    "gasto_salud_usd": "salud",
}


def main():
    df = pd.read_csv(CSV_PATH, encoding="utf-8")
    peru = df[df["pais"] == COUNTRY].copy()

    # 1. Sample size and age range
    n = len(peru)
    age_min = peru["edad"].min()
    age_max = peru["edad"].max()

    # 2. Income stats
    income = peru["ingreso_mensual_usd"]
    income_median = income.median()
    income_mean = income.mean()
    income_min = income.min()
    income_max = income.max()
    income_std = income.std()

    # 3. Housing burden (% of income)
    housing_pct = (peru["gasto_vivienda_usd"] / peru["ingreso_mensual_usd"] * 100)
    housing_pct_avg = housing_pct.mean()

    # 4. Spending breakdown (% of income) for each gasto_* column
    spending_breakdown = {}
    for col in GASTO_COLS:
        pct = (peru[col] / peru["ingreso_mensual_usd"] * 100)
        spending_breakdown[GASTO_LABELS[col]] = pct.mean()

    # 5. Savings
    ahorro_avg = peru["ahorro_mensual_usd"].mean()
    pct_negative_savings = (peru["ahorro_mensual_usd"] < 0).mean() * 100

    # 6. AI tools
    ia_hours_avg = peru["horas_herramientas_ia_semana"].mean()
    satisfaccion_avg = peru["satisfaccion_financiera"].mean()

    # 7. Most common industria
    industria_mode = peru["industria"].mode().iloc[0]
    industria_count = (peru["industria"] == industria_mode).sum()

    # 8. Most common ocupacion
    ocupacion_mode = peru["ocupacion"].mode().iloc[0]
    ocupacion_count = (peru["ocupacion"] == ocupacion_mode).sum()

    # 9. Most common meta_financiera
    meta_mode = peru["meta_financiera"].mode().iloc[0]
    meta_count = (peru["meta_financiera"] == meta_mode).sum()

    # 10 & 11 support figures
    deuda_avg = peru["deuda_total_usd"].mean()
    pct_con_deuda = peru["tiene_deuda"].mean() * 100

    print(f"=== Country Profile: {COUNTRY} ===\n")

    print("1. Sample size and age range")
    print(f"   n = {n}")
    print(f"   age range = {age_min}-{age_max}\n")

    print("2. Income (USD)")
    print(f"   median = {income_median:.2f}")
    print(f"   mean   = {income_mean:.2f}")
    print(f"   min    = {income_min:.2f}")
    print(f"   max    = {income_max:.2f}")
    print(f"   std    = {income_std:.2f}\n")

    print("3. Housing burden")
    print(f"   avg gasto_vivienda_usd as % of ingreso_mensual_usd = {housing_pct_avg:.2f}%\n")

    print("4. Spending breakdown (avg % of income)")
    for label, pct in spending_breakdown.items():
        print(f"   {label}: {pct:.2f}%")
    print()

    print("5. Savings")
    print(f"   avg ahorro_mensual_usd = {ahorro_avg:.2f}")
    print(f"   % respondents with negative savings = {pct_negative_savings:.2f}%\n")

    print("6. AI tools")
    print(f"   avg horas_herramientas_ia_semana = {ia_hours_avg:.2f}")
    print(f"   avg satisfaccion_financiera = {satisfaccion_avg:.2f}\n")

    print("7. Most common industria")
    print(f"   {industria_mode} (n={industria_count})\n")

    print("8. Most common ocupacion")
    print(f"   {ocupacion_mode} (n={ocupacion_count})\n")

    print("9. Most common meta_financiera")
    print(f"   {meta_mode} (n={meta_count})\n")

    print("Supporting figures for risk/insight")
    print(f"   avg deuda_total_usd = {deuda_avg:.2f}")
    print(f"   % con deuda = {pct_con_deuda:.2f}%")


if __name__ == "__main__":
    main()
