"""Phase 2: Clean latam_finanzas_2025.csv -> latam_finanzas_clean.csv

Cleaning decisions are documented in data-quality-log.md.
"""
import pandas as pd

SRC = "data/latam_finanzas_2025.csv"
DST = "data/latam_finanzas_clean.csv"

df = pd.read_csv(SRC)
rows_before, cols_before = df.shape

# 1. Standardize `industria` variants (case/spelling/language drift) to a
#    single canonical label per industry. Only "Tecnología" had variants
#    in Phase 1 (Tecnologia, tech, TECNOLOGÍA all mean the same thing).
industria_map = {
    "Tecnologia": "Tecnología",
    "tech": "Tecnología",
    "TECNOLOGÍA": "Tecnología",
}
df["industria"] = df["industria"].replace(industria_map)

# 2. Convert Sí/No columns to real booleans.
si_no_cols = ["tiene_tarjeta_credito", "tiene_cuenta_ahorro", "tiene_deuda"]
for col in si_no_cols:
    df[col] = df[col].map({"Sí": True, "No": False})

# 3. Handle missing gasto_salud_usd (33 rows, 6.6%) via median imputation.
#    Median is robust to the right-skew visible in Phase 1 describe() output.
#    A flag column preserves which rows were imputed for downstream transparency.
gasto_salud_median = df["gasto_salud_usd"].median()
df["gasto_salud_usd_imputed"] = df["gasto_salud_usd"].isna()
df["gasto_salud_usd"] = df["gasto_salud_usd"].fillna(gasto_salud_median)

# 4. Negative ahorro_mensual_usd values are preserved as-is. Phase 2 sanity
#    check confirmed all 74 negative rows are modest deficits (max -53% of
#    that row's income, mean ~-36 USD) consistent with real overspending,
#    not corrupted data. No clipping or imputation applied.

# 5. Verify no duplicate ids or duplicate rows.
dup_rows = df.duplicated().sum()
dup_ids = df["id"].duplicated().sum()
assert dup_rows == 0, f"Found {dup_rows} duplicate rows"
assert dup_ids == 0, f"Found {dup_ids} duplicate ids"

rows_after, cols_after = df.shape

df.to_csv(DST, index=False, encoding="utf-8")

print("=" * 80)
print("PHASE 2 CLEANING SUMMARY")
print("=" * 80)
print(f"Rows before:    {rows_before}")
print(f"Columns before: {cols_before}")
print(f"Rows after:     {rows_after}")
print(f"Columns after:  {cols_after}")
print(f"gasto_salud_usd median used for imputation: {gasto_salud_median}")
print(f"gasto_salud_usd rows imputed: {int(df['gasto_salud_usd_imputed'].sum())}")
print(f"Duplicate rows: {dup_rows}")
print(f"Duplicate ids:  {dup_ids}")
print(f"Negative ahorro_mensual_usd rows preserved: {(df['ahorro_mensual_usd'] < 0).sum()}")
print()
print("industria value counts after standardization:")
print(df["industria"].value_counts())
print()
print(f"Saved cleaned dataset to {DST}")
