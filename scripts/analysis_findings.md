# Phase 3 — Analysis Findings

Source: `data/latam_finanzas_clean.csv`  
Script: `scripts/03_analyse.py`  
Significance threshold: alpha = 0.05. Findings 4-6 report non-significant results as genuine null findings rather than forcing a pattern.

## Finding 1: Housing cost burden varies sharply by country — Argentina and Chile are cost-burdened

- **Key statistic:** Average housing spend as % of income ranges from 24.6% (Perú) to 34.1% (Argentina); the difference across all six countries is statistically significant (one-way ANOVA F=39.50, p=3.779e-34). Argentina, Chile exceed the conventional 30% 'cost-burdened' threshold.
- **Affected segment/country:** Argentina, Chile
- **Business/stakeholder implication:** Users in Argentina and Chile have structurally less disposable income left after fixed housing costs, regardless of income level, which limits how much they can allocate to savings or investment products.
- **Recommended action:** Prioritize housing-cost budgeting and rent/mortgage-optimization features for Argentina and Chile before pushing investment-focused products in those markets.

## Finding 2: Average income differs significantly by country, not by industry

- **Key statistic:** Average monthly income ranges from $766 (Argentina) to $1388 (Brasil); this is statistically significant across countries (one-way ANOVA F=44.28, p=9.633e-38). By contrast, a parallel test of income across industria groups was not significant (F=0.50, p=0.87), meaning country of residence, not industry, is the meaningful income-segmentation axis in this data.
- **Affected segment/country:** Brasil (highest) vs Argentina (lowest)
- **Business/stakeholder implication:** Product pricing, tiering, and affordability assumptions should be built around country, not industry — industry alone does not reliably predict a user's income band in this dataset.
- **Recommended action:** Use country as the primary axis for income-based segmentation and pricing tiers; do not build industry-based pricing logic on this data, since it showed no significant income effect.

## Finding 3: AI financial tool usage is the strongest predictor of financial satisfaction found in this dataset

- **Key statistic:** Pearson correlation between horas_herramientas_ia_semana and satisfaccion_financiera is r=0.571 (p=1.193e-44) — a statistically significant, and by far the strongest relationship of any tested in Phase 3.
- **Affected segment/country:** All countries
- **Business/stakeholder implication:** Correlation is not causation, but AI tool engagement tracks financial satisfaction far more strongly than debt load, housing burden, or income in this sample — engagement with these tools may be a meaningful lever, or a proxy for underlying financial confidence/literacy.
- **Recommended action:** Investigate this relationship further (e.g. does usage drive satisfaction, or do already-satisfied users simply engage more?) before committing budget, but treat AI-tool engagement as the leading candidate signal for a satisfaction-focused product intervention.

## Finding 4: Debt-to-income ratio alone does not predict financial satisfaction

- **Key statistic:** Pearson correlation between debt-to-income ratio and satisfaccion_financiera is r=-0.044 (p=0.3221) — not statistically significant.
- **Affected segment/country:** All countries, debt-holding respondents (46.8% of the sample)
- **Business/stakeholder implication:** Contrary to a common assumption, carrying more debt relative to income does not, by itself, track with lower reported financial satisfaction in this sample — satisfaction is likely driven by other factors (see Finding 3).
- **Recommended action:** Do not rely on debt-to-income ratio alone as a proxy for user dissatisfaction or churn risk; validate any debt-focused intervention against an actual satisfaction or retention metric before scaling it.

## Finding 5: Simply holding debt does not significantly predict running a monthly deficit

- **Key statistic:** 13.7% of respondents with debt report negative monthly savings, versus 15.8% of those without debt (chi-square=0.29, p=0.5905) — not statistically significant.
- **Affected segment/country:** All countries
- **Business/stakeholder implication:** A binary 'has debt' flag is not, on its own, a reliable indicator of monthly cash-flow risk at the aggregate level. Country-level negative-savings rates (e.g. Perú 20.0%, Colombia 18.75% from Phase 2.5) are more informative than the debt flag alone.
- **Recommended action:** When targeting at-risk users, use continuous or country-level cash-flow indicators (negative ahorro_mensual_usd, debt-to-income ratio) instead of the binary tiene_deuda flag, which showed no significant discriminative value.

## Finding 6: Financial goal mix does not differ significantly by country at the aggregate level

- **Key statistic:** The full distribution of meta_financiera across countries is not statistically significant (chi-square=38.78, p=0.3032, dof=35). Descriptively, the share citing 'Pagar deudas' as their top goal ranges from 12.0% (México) to 23.1% (Brasil), but this spread is not statistically confirmed at the whole-table level.
- **Affected segment/country:** All countries (descriptive spread only, not statistically confirmed)
- **Business/stakeholder implication:** The country-level goal narratives from the Phase 2.5 profiles (e.g. debt payoff standing out in Brasil/Perú) are directional observations from small per-country samples, not a confirmed regional pattern — a formal test across the full 6-country x 8-goal table does not reach significance.
- **Recommended action:** Treat country-specific goal framing (e.g. leading with debt payoff in Brasil) as a hypothesis to validate with more data or a targeted survey, not as a statistically confirmed regional difference yet.
