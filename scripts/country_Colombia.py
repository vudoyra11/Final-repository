"""
Country profile script: Colombia
Reads the Phase 2 cleaned dataset and computes summary statistics for
respondents where pais == "Colombia".

Run standalone with:
    python scripts/country_Colombia.py
"""

import pandas as pd

CSV_PATH = "data/latam_finanzas_clean.csv"
COUNTRY = "Colombia"

GASTO_COLUMNS = [
    "gasto_vivienda_usd",
    "gasto_alimentacion_usd",
    "gasto_transporte_usd",
    "gasto_entretenimiento_usd",
    "gasto_educacion_usd",
    "gasto_salud_usd",
]


def main():
    df = pd.read_csv(CSV_PATH)
    df_c = df[df["pais"] == COUNTRY].copy()

    if df_c.empty:
        print(f"No rows found for pais == '{COUNTRY}'.")
        return

    # 1. Sample size and age range
    n = len(df_c)
    age_min = df_c["edad"].min()
    age_max = df_c["edad"].max()

    # 2. Income stats (USD)
    income = df_c["ingreso_mensual_usd"]
    income_median = income.median()
    income_mean = income.mean()
    income_min = income.min()
    income_max = income.max()
    income_std = income.std()

    # 3. Housing burden: avg % of income spent on housing
    housing_pct = (df_c["gasto_vivienda_usd"] / df_c["ingreso_mensual_usd"] * 100)
    housing_pct_avg = housing_pct.mean()

    # 4. Spending breakdown: avg % of income for each gasto_* column
    spending_breakdown = {}
    for col in GASTO_COLUMNS:
        pct = (df_c[col] / df_c["ingreso_mensual_usd"] * 100)
        spending_breakdown[col] = pct.mean()

    # 5. Savings
    ahorro = df_c["ahorro_mensual_usd"]
    ahorro_avg = ahorro.mean()
    pct_negative_savings = (ahorro < 0).mean() * 100

    # 6. AI tools
    ia_hours_avg = df_c["horas_herramientas_ia_semana"].mean()
    satisfaccion_avg = df_c["satisfaccion_financiera"].mean()

    # 7. Most common industria
    industria_mode = df_c["industria"].mode().iloc[0]
    industria_count = (df_c["industria"] == industria_mode).sum()

    # 8. Most common ocupacion
    ocupacion_mode = df_c["ocupacion"].mode().iloc[0]
    ocupacion_count = (df_c["ocupacion"] == ocupacion_mode).sum()

    # 9. Most common meta_financiera
    meta_mode = df_c["meta_financiera"].mode().iloc[0]
    meta_count = (df_c["meta_financiera"] == meta_mode).sum()

    # 10. Additional risk signal candidates
    debt_avg = df_c["deuda_total_usd"].mean()
    pct_with_debt = df_c["tiene_deuda"].mean() * 100

    # ---- Print results ----
    print(f"=== Country Profile: {COUNTRY} ===")
    print()
    print("1. Sample size & age range")
    print(f"   n = {n}")
    print(f"   age range = {age_min}-{age_max}")
    print()
    print("2. Income (USD)")
    print(f"   median = {income_median:.2f}")
    print(f"   mean   = {income_mean:.2f}")
    print(f"   min    = {income_min:.2f}")
    print(f"   max    = {income_max:.2f}")
    print(f"   std    = {income_std:.2f}")
    print()
    print("3. Housing burden")
    print(f"   avg gasto_vivienda_usd as % of income = {housing_pct_avg:.2f}%")
    print()
    print("4. Spending breakdown (avg % of income)")
    for col, pct in spending_breakdown.items():
        print(f"   {col} = {pct:.2f}%")
    print()
    print("5. Savings")
    print(f"   avg ahorro_mensual_usd = {ahorro_avg:.2f}")
    print(f"   % respondents with negative savings = {pct_negative_savings:.2f}%")
    print()
    print("6. AI tools")
    print(f"   avg horas_herramientas_ia_semana = {ia_hours_avg:.2f}")
    print(f"   avg satisfaccion_financiera = {satisfaccion_avg:.2f}")
    print()
    print("7. Most common industria")
    print(f"   {industria_mode} (n={industria_count})")
    print()
    print("8. Most common ocupacion")
    print(f"   {ocupacion_mode} (n={ocupacion_count})")
    print()
    print("9. Most common meta_financiera")
    print(f"   {meta_mode} (n={meta_count})")
    print()
    print("10. Additional risk context")
    print(f"   avg deuda_total_usd = {debt_avg:.2f}")
    print(f"   % respondents with tiene_deuda = True = {pct_with_debt:.2f}%")


if __name__ == "__main__":
    main()
