"""
Country profile: Brasil
Reads the Phase 2 cleaned dataset and prints key financial wellness metrics
for respondents where pais == "Brasil".

Run standalone:
    python scripts/country_Brasil.py
"""

import pandas as pd

DATA_PATH = "data/latam_finanzas_clean.csv"
COUNTRY = "Brasil"

GASTO_COLS = [
    "gasto_vivienda_usd",
    "gasto_alimentacion_usd",
    "gasto_transporte_usd",
    "gasto_entretenimiento_usd",
    "gasto_educacion_usd",
    "gasto_salud_usd",
]


def main():
    df = pd.read_csv(DATA_PATH)
    d = df[df["pais"] == COUNTRY].copy()

    print(f"=== Country profile: {COUNTRY} ===\n")

    # 1. Sample size and age range
    n = len(d)
    age_min, age_max = d["edad"].min(), d["edad"].max()
    print(f"1. Sample size: {n}")
    print(f"   Age range: {age_min}-{age_max}\n")

    # 2. Income stats
    income = d["ingreso_mensual_usd"]
    print("2. Income (USD):")
    print(f"   median = {income.median():.2f}")
    print(f"   mean   = {income.mean():.2f}")
    print(f"   min    = {income.min():.2f}")
    print(f"   max    = {income.max():.2f}")
    print(f"   std    = {income.std():.2f}\n")

    # 3. Housing burden (row-wise % of income, then averaged)
    housing_pct = (d["gasto_vivienda_usd"] / d["ingreso_mensual_usd"]) * 100
    print("3. Housing burden:")
    print(f"   avg gasto_vivienda_usd as % of ingreso_mensual_usd = {housing_pct.mean():.2f}%\n")

    # 4. Spending breakdown (avg % of income per gasto_* column)
    print("4. Spending breakdown (avg % of income):")
    spending_pct = {}
    for col in GASTO_COLS:
        pct = (d[col] / d["ingreso_mensual_usd"]) * 100
        spending_pct[col] = pct.mean()
        print(f"   {col}: {pct.mean():.2f}%")
    print()

    # 5. Savings
    savings = d["ahorro_mensual_usd"]
    neg_savers_pct = (savings < 0).mean() * 100
    print("5. Savings:")
    print(f"   avg ahorro_mensual_usd = {savings.mean():.2f}")
    print(f"   % respondents with negative savings = {neg_savers_pct:.2f}%\n")

    # 6. AI tools
    ai_hours = d["horas_herramientas_ia_semana"].mean()
    satisfaction = d["satisfaccion_financiera"].mean()
    print("6. AI tools & satisfaction:")
    print(f"   avg horas_herramientas_ia_semana = {ai_hours:.2f}")
    print(f"   avg satisfaccion_financiera = {satisfaction:.2f}\n")

    # 7. Most common industria
    industria_mode = d["industria"].mode().iloc[0]
    industria_count = (d["industria"] == industria_mode).sum()
    print("7. Most common industria:")
    print(f"   {industria_mode} (count = {industria_count})\n")

    # 8. Most common ocupacion
    ocupacion_mode = d["ocupacion"].mode().iloc[0]
    ocupacion_count = (d["ocupacion"] == ocupacion_mode).sum()
    print("8. Most common ocupacion:")
    print(f"   {ocupacion_mode} (count = {ocupacion_count})\n")

    # 9. Most common meta_financiera
    meta_mode = d["meta_financiera"].mode().iloc[0]
    meta_count = (d["meta_financiera"] == meta_mode).sum()
    print("9. Most common meta_financiera:")
    print(f"   {meta_mode} (count = {meta_count})\n")

    # 10. Key financial risk signal — computed for context/inspection
    debt_holders_pct = d["tiene_deuda"].mean() * 100
    avg_debt = d.loc[d["tiene_deuda"], "deuda_total_usd"].mean()
    print("10. Risk-signal inputs:")
    print(f"   housing burden avg = {housing_pct.mean():.2f}%")
    print(f"   % negative savers = {neg_savers_pct:.2f}%")
    print(f"   % with debt (tiene_deuda) = {debt_holders_pct:.2f}%")
    print(f"   avg deuda_total_usd (debt holders only) = {avg_debt:.2f}\n")


if __name__ == "__main__":
    main()
