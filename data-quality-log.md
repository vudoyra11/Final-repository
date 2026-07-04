# Data Quality Log — Phase 2 Cleaning

Source: `data/latam_finanzas_2025.csv` (500 rows, 21 columns)
Output: `data/latam_finanzas_clean.csv` (500 rows, 22 columns)
Script: `scripts/02_clean.py`

## Cleaning decisions

### 1. Standardized `industria` category variants
Phase 1 found four spellings/casings referring to the same industry:
`Tecnología` (47), `Tecnologia` (5, missing accent), `tech` (3, lowercase
English), `TECNOLOGÍA` (2, all caps). All were mapped to the canonical
`Tecnología`, bringing the consolidated count to 57. No other `industria`
values, or any other categorical column, had variant spellings in Phase 1.

### 2. Converted Sí/No columns to booleans
`tiene_tarjeta_credito`, `tiene_cuenta_ahorro`, and `tiene_deuda` were
stored as the strings `"Sí"`/`"No"`. Converted to native booleans
(`True`/`False`) for consistent typing and easier downstream analysis.

### 3. Imputed missing `gasto_salud_usd` with the median
33 rows (6.6%) were missing `gasto_salud_usd`. Imputed with the column
median (45.66), which is robust to the right-skew observed in the Phase 1
`describe()` output (mean 49.88 > median, long right tail up to 150.23).
A new boolean column, `gasto_salud_usd_imputed`, flags exactly which rows
were imputed so downstream analysis can exclude or weight them if needed.

### 4. Preserved negative `ahorro_mensual_usd` values
74 rows have negative monthly savings (min -160.02). Checked these against
each row's income and total expenses: negative values are modest deficits
(mean ≈ -36 USD, max deficit ≈ 53% of that row's income) — consistent with
real overspending behavior, not corrupted data. No clipping, flooring, or
imputation was applied; these are kept as valid deficit-spending signals.

### 5. Verified uniqueness
Confirmed 0 duplicate rows and 0 duplicate `id` values, matching the
Phase 1 finding. No rows were dropped for duplication.

### 6. Left unchanged
- `pais`, `ocupacion`, `meta_financiera`: checked for whitespace/casing
  variants in Phase 2 — none found, no changes needed.
- Accented characters (México, Perú, Sí, etc.): confirmed in Phase 1 to be
  correctly UTF-8 encoded in the source file; any garbled display is a
  terminal codepage issue, not a data problem. Cleaned file is written
  with `encoding="utf-8"` to preserve this.
- `tiene_deuda` vs `deuda_total_usd`: verified consistent (`No` → 0 debt,
  `Sí` → positive debt) — no conflicting rows found.

## Result
| | Before | After |
|---|---|---|
| Rows | 500 | 500 |
| Columns | 21 | 22 (added `gasto_salud_usd_imputed`) |
| Missing values | 33 (`gasto_salud_usd`) | 0 |
| Duplicate rows/ids | 0 | 0 |
