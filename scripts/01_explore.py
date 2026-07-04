"""Phase 1: Dataset exploration for latam_finanzas_2025.csv"""
import pandas as pd

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 160)

df = pd.read_csv("data/latam_finanzas_2025.csv")

print("=" * 80)
print("SHAPE (rows, columns)")
print("=" * 80)
print(df.shape)

print("\n" + "=" * 80)
print("COLUMNS")
print("=" * 80)
print(list(df.columns))

print("\n" + "=" * 80)
print("DATA TYPES")
print("=" * 80)
print(df.dtypes)

print("\n" + "=" * 80)
print("MISSING VALUES (count and %)")
print("=" * 80)
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_report = pd.DataFrame({"missing_count": missing, "missing_pct": missing_pct})
print(missing_report[missing_report["missing_count"] > 0].sort_values("missing_count", ascending=False))

print("\n" + "=" * 80)
print("NUMERIC STATISTICS (describe)")
print("=" * 80)
print(df.describe())

print("\n" + "=" * 80)
print("CATEGORICAL VALUE COUNTS")
print("=" * 80)
categorical_cols = df.select_dtypes(include=["object"]).columns
for col in categorical_cols:
    print(f"\n--- {col} ---")
    print(df[col].value_counts(dropna=False))

print("\n" + "=" * 80)
print("DUPLICATE ROWS")
print("=" * 80)
print(f"Full duplicate rows: {df.duplicated().sum()}")
if "id" in df.columns:
    print(f"Duplicate ids: {df['id'].duplicated().sum()}")
