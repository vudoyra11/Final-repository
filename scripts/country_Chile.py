"""
Country profile: Chile
Reads the Phase 2 cleaned dataset (data/latam_finanzas_clean.csv), filters to
pais == "Chile", and prints the standard country-profile metrics.
Run standalone: python scripts/country_Chile.py
"""

import pandas as pd

CSV_PATH = "data/latam_finanzas_clean.csv"
COUNTRY = "Chile"

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

    print(f"=== Country profile: {COUNTRY} ===")

    # 1. Sample size and age range
    n = len(d)
    age_min, age_max = d["edad"].min(), d["edad"].max()
    print(f"\n1. Sample size: {n}")
    print(f"   Age range: {age_min}-{age_max}")

    # 2. Income stats
    ing = d["ingreso_mensual_usd"]
    print("\n2. Income (USD):")
    print(f"   Median: {ing.median():.2f}")
    print(f"   Mean: {ing.mean():.2f}")
    print(f"   Min: {ing.min():.2f}")
    print(f"   Max: {ing.max():.2f}")
    print(f"   Std dev: {ing.std():.2f}")

    # 3. Housing burden
    housing_pct = (d["gasto_vivienda_usd"] / d["ingreso_mensual_usd"] * 100)
    print(f"\n3. Housing burden (avg % of income): {housing_pct.mean():.2f}%")

    # 4. Spending breakdown (avg % of income per gasto_* column)
    print("\n4. Spending breakdown (avg % of income):")
    spending_pct = {}
    for col in GASTO_COLS:
        pct = (d[col] / d["ingreso_mensual_usd"] * 100).mean()
        spending_pct[col] = pct
        print(f"   {col}: {pct:.2f}%")

    # 5. Savings
    ahorro = d["ahorro_mensual_usd"]
    avg_ahorro = ahorro.mean()
    pct_negative = (ahorro < 0).mean() * 100
    print(f"\n5. Savings:")
    print(f"   Average ahorro_mensual_usd: {avg_ahorro:.2f}")
    print(f"   % respondents with negative savings: {pct_negative:.2f}%")

    # 6. AI tools
    avg_ia_hours = d["horas_herramientas_ia_semana"].mean()
    avg_satisfaccion = d["satisfaccion_financiera"].mean()
    print(f"\n6. AI tools:")
    print(f"   Average horas_herramientas_ia_semana: {avg_ia_hours:.2f}")
    print(f"   Average satisfaccion_financiera: {avg_satisfaccion:.2f}")

    # 7. Most common industria
    industria_mode = d["industria"].mode().iloc[0]
    industria_count = (d["industria"] == industria_mode).sum()
    print(f"\n7. Most common industria: {industria_mode} ({industria_count})")

    # 8. Most common ocupacion
    ocupacion_mode = d["ocupacion"].mode().iloc[0]
    ocupacion_count = (d["ocupacion"] == ocupacion_mode).sum()
    print(f"\n8. Most common ocupacion: {ocupacion_mode} ({ocupacion_count})")

    # 9. Most common meta_financiera
    meta_mode = d["meta_financiera"].mode().iloc[0]
    meta_count = (d["meta_financiera"] == meta_mode).sum()
    print(f"\n9. Most common meta_financiera: {meta_mode} ({meta_count})")

    # 10. Key financial risk signal (computed for narrative, not hardcoded)
    avg_debt = d["deuda_total_usd"].mean()
    debt_share_of_income = (d["deuda_total_usd"] / (d["ingreso_mensual_usd"] * 12) * 100).mean()
    print(f"\n10. Risk indicators (for narrative):")
    print(f"    Avg deuda_total_usd: {avg_debt:.2f}")
    print(f"    Avg debt as % of annual income: {debt_share_of_income:.2f}%")
    print(f"    Housing burden %: {housing_pct.mean():.2f}%")
    print(f"    % negative savers: {pct_negative:.2f}%")

    print("\nDone.")


if __name__ == "__main__":
    main()
