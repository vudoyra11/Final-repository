"""Phase 4: Generate 5 charts supporting the Phase 3 findings.

Source: data/latam_finanzas_clean.csv
Findings reference: scripts/analysis_findings.md
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

os.makedirs("charts", exist_ok=True)
sns.set_theme(style="whitegrid")

df = pd.read_csv("data/latam_finanzas_clean.csv")
df["pct_vivienda"] = df["gasto_vivienda_usd"] / df["ingreso_mensual_usd"] * 100
SOURCE_NOTE = "Source: data/latam_finanzas_clean.csv (n=500) | Phase 4 — Análisis LatAm 2025"

# ---------------------------------------------------------------------------
# Chart 1: Age vs Savings
# Supplementary to Phase 3 (not one of the original 6 findings, but a real,
# statistically significant relationship: r=0.385, p=4.2e-19).
# ---------------------------------------------------------------------------
r1, p1 = stats.pearsonr(df["edad"], df["ahorro_mensual_usd"])
fig, ax = plt.subplots(figsize=(8, 6))
sns.regplot(
    data=df, x="edad", y="ahorro_mensual_usd", ax=ax,
    scatter_kws={"alpha": 0.4, "s": 25}, line_kws={"color": "firebrick"},
)
ax.set_title("Older Respondents Save More Each Month", fontsize=14, fontweight="bold")
ax.set_xlabel("Age (years)")
ax.set_ylabel("Monthly Savings (USD)")
ax.text(
    0.02, 0.96, f"Pearson r = {r1:.2f}, p = {p1:.2g} (significant)",
    transform=ax.transAxes, fontsize=10, va="top",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
)
fig.text(0.01, 0.01, SOURCE_NOTE, fontsize=8, color="gray")
fig.tight_layout(rect=[0, 0.03, 1, 1])
fig.savefig("charts/01_age_vs_savings.png", dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 2: Income by Country
# Supports Finding 2 — income differs significantly by country (ANOVA
# F=44.28, p=9.6e-38), Brasil highest, Argentina lowest.
# ---------------------------------------------------------------------------
order2 = df.groupby("pais")["ingreso_mensual_usd"].mean().sort_values(ascending=False).index
fig, ax = plt.subplots(figsize=(9, 6))
sns.barplot(
    data=df, x="pais", y="ingreso_mensual_usd", order=order2,
    errorbar="sd", ax=ax, hue="pais", legend=False, palette="crest",
)
ax.set_title("Average Monthly Income by Country", fontsize=14, fontweight="bold")
ax.set_xlabel("Country")
ax.set_ylabel("Monthly Income (USD)")
ax.text(
    0.02, 0.96, "One-way ANOVA F=44.28, p<0.001 (significant)",
    transform=ax.transAxes, fontsize=10, va="top",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
)
fig.text(0.01, 0.01, SOURCE_NOTE, fontsize=8, color="gray")
fig.tight_layout(rect=[0, 0.03, 1, 1])
fig.savefig("charts/02_income_by_country.png", dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 3: AI Tool Usage vs Financial Satisfaction
# Supports Finding 3 — the strongest relationship in Phase 3
# (r=0.571, p=1.2e-44).
# ---------------------------------------------------------------------------
r3, p3 = stats.pearsonr(df["horas_herramientas_ia_semana"], df["satisfaccion_financiera"])
fig, ax = plt.subplots(figsize=(8, 6))
sns.regplot(
    data=df, x="horas_herramientas_ia_semana", y="satisfaccion_financiera", ax=ax,
    scatter_kws={"alpha": 0.4, "s": 25}, line_kws={"color": "firebrick"},
)
ax.set_title("AI Financial Tool Usage vs Financial Satisfaction", fontsize=14, fontweight="bold")
ax.set_xlabel("AI Tool Usage (hours/week)")
ax.set_ylabel("Financial Satisfaction (1-5 scale)")
ax.text(
    0.02, 0.96, f"Pearson r = {r3:.2f}, p < 0.001 (strongest relationship in Phase 3)",
    transform=ax.transAxes, fontsize=10, va="top",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
)
fig.text(0.01, 0.01, SOURCE_NOTE, fontsize=8, color="gray")
fig.tight_layout(rect=[0, 0.03, 1, 1])
fig.savefig("charts/03_ai_usage_vs_satisfaction.png", dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 4: Housing Burden by Country
# Supports Finding 1 — Argentina and Chile exceed the 30% cost-burdened
# threshold (ANOVA F=39.50, p=3.8e-34).
# ---------------------------------------------------------------------------
order4 = df.groupby("pais")["pct_vivienda"].mean().sort_values(ascending=False).index
fig, ax = plt.subplots(figsize=(9, 6))
sns.barplot(
    data=df, x="pais", y="pct_vivienda", order=order4,
    errorbar="sd", ax=ax, hue="pais", legend=False, palette="flare",
)
ax.axhline(30, color="black", linestyle="--", linewidth=1.5, label="30% cost-burdened threshold")
ax.set_title("Housing Cost Burden by Country", fontsize=14, fontweight="bold")
ax.set_xlabel("Country")
ax.set_ylabel("Housing Spend (% of Monthly Income)")
ax.legend(loc="upper right")
fig.text(0.01, 0.01, SOURCE_NOTE, fontsize=8, color="gray")
fig.tight_layout(rect=[0, 0.03, 1, 1])
fig.savefig("charts/04_housing_burden_by_country.png", dpi=150)
plt.close(fig)

# ---------------------------------------------------------------------------
# Chart 5: Spending Breakdown by Country
# Context for Findings 1 & 2 — shows how the average income dollar is
# allocated across categories in each country.
# ---------------------------------------------------------------------------
gasto_cols = {
    "gasto_vivienda_usd": "Housing",
    "gasto_alimentacion_usd": "Food",
    "gasto_transporte_usd": "Transport",
    "gasto_entretenimiento_usd": "Entertainment",
    "gasto_educacion_usd": "Education",
    "gasto_salud_usd": "Health",
}
pct_df = pd.DataFrame({
    label: df[col] / df["ingreso_mensual_usd"] * 100
    for col, label in gasto_cols.items()
})
pct_df["pais"] = df["pais"]
breakdown = pct_df.groupby("pais")[list(gasto_cols.values())].mean()
breakdown = breakdown.loc[order2]  # order by income, consistent with Chart 2

fig, ax = plt.subplots(figsize=(10, 6))
breakdown.plot(kind="bar", stacked=True, ax=ax, colormap="tab20c")
ax.set_title("Average Spending Breakdown by Country (% of Income)", fontsize=14, fontweight="bold")
ax.set_xlabel("Country")
ax.set_ylabel("% of Monthly Income")
ax.legend(title="Category", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.setp(ax.get_xticklabels(), rotation=0)
fig.text(0.01, 0.01, SOURCE_NOTE, fontsize=8, color="gray")
fig.tight_layout(rect=[0, 0.03, 0.85, 1])
fig.savefig("charts/05_spending_breakdown.png", dpi=150)
plt.close(fig)

print("Charts saved:")
for f in sorted(os.listdir("charts")):
    if f.endswith(".png"):
        print(f" - charts/{f}")
