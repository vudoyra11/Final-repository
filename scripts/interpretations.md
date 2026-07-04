# Phase 5 — Interpretaciones (Encuesta de Bienestar Financiero 2025)

Generadas con el formato del skill `/interpret` (`.claude/skills/interpret/SKILL.md`).
Fuente de datos: `scripts/analysis_findings.md` y los 5 gráficos de `charts/`.

Nota de alcance: se interpretan los 5 hallazgos con respaldo gráfico directo. Los
Hallazgos 4-6 de `scripts/analysis_findings.md` (relación deuda/ingreso vs.
satisfacción, tenencia de deuda vs. ahorro negativo, y meta financiera por país)
resultaron estadísticamente no significativos en la Fase 3 y no cuentan con un
gráfico dedicado en la Fase 4, por lo que no se incluyen aquí como hallazgos
principales.

---

**Hallazgo 1: La carga de vivienda supera el umbral crítico en Argentina y Chile**

En Argentina el gasto en vivienda representa el 34.1% del ingreso mensual y en Chile el 32.6%, superando el umbral convencional de "carga excesiva" del 30%, una diferencia estadísticamente significativa entre los seis países (ANOVA, F=39.50, p<0.001). Esto significa que los usuarios argentinos y chilenos disponen de una porción menor de su ingreso para ahorro o inversión, independientemente de su nivel de ingreso, lo cual limita el impacto de programas de educación financiera enfocados solo en fomentar el ahorro. Futuro Digital LatAm debería priorizar módulos de presupuesto de vivienda y optimización de alquiler o hipoteca para los segmentos de Argentina y Chile antes de promover productos de inversión de largo plazo.

**Fuente:** ANOVA de carga de vivienda por país, F=39.50, p=3.779e-34 (`scripts/analysis_findings.md`, Hallazgo 1) — gráfico: `charts/04_housing_burden_by_country.png`

---

**Hallazgo 2: El ingreso varía significativamente por país, no por industria**

El ingreso mensual promedio varía significativamente entre países, desde 766 USD en Argentina hasta 1,388 USD en Brasil (ANOVA, F=44.28, p<0.001), mientras que la industria laboral no mostró un efecto significativo sobre el ingreso (F=0.50, p=0.87). Esto indica que el país de residencia, y no el sector industrial, es el eje relevante para segmentar la capacidad económica de los usuarios de Futuro Digital LatAm. Se recomienda diseñar niveles de producto y contenido educativo diferenciados por país en lugar de por industria, ya que esta última no predice de forma confiable el nivel de ingreso en esta muestra.

**Fuente:** ANOVA de ingreso por país, F=44.28, p=9.633e-38 (`scripts/analysis_findings.md`, Hallazgo 2) — gráfico: `charts/02_income_by_country.png`

---

**Hallazgo 3: El uso de herramientas de IA es el predictor más fuerte de satisfacción financiera**

El uso semanal de herramientas de inteligencia artificial se correlaciona fuertemente con la satisfacción financiera reportada (r=0.571, p<0.001), la relación más fuerte encontrada en todo el análisis de la Fase 3. Esto sugiere que el compromiso con herramientas de IA financiera podría ser la palanca más prometedora para mejorar el bienestar financiero percibido entre los usuarios de todos los países, aunque la correlación no implica causalidad. Futuro Digital LatAm debería priorizar la inversión en funciones de IA dentro de su plataforma, validando primero si el uso impulsa la satisfacción o si los usuarios ya satisfechos simplemente usan más estas herramientas.

**Fuente:** Correlación de Pearson r=0.571, p=1.193e-44 (`scripts/analysis_findings.md`, Hallazgo 3) — gráfico: `charts/03_ai_usage_vs_satisfaction.png`

---

**Hallazgo 4: Los usuarios más jóvenes ahorran menos cada mes**

La edad se correlaciona positivamente con el ahorro mensual (r=0.385, p<0.001), lo que indica que los encuestados de mayor edad dentro del rango de 18 a 32 años tienden a ahorrar montos más altos cada mes. Esto es relevante para el programa de educación financiera porque sugiere que los usuarios más jóvenes son el grupo con menor capacidad de ahorro y, por lo tanto, el segmento más vulnerable a no desarrollar hábitos de ahorro tempranos. Se recomienda diseñar contenido e incentivos de ahorro dirigidos específicamente a los usuarios más jóvenes de la plataforma, reforzando estos hábitos desde el inicio de su vida laboral.

**Fuente:** Correlación de Pearson r=0.385, p=4.16e-19 (hallazgo complementario, no incluido en los 6 originales de la Fase 3, calculado para la Fase 4) — gráfico: `charts/01_age_vs_savings.png`

---

**Hallazgo 5: La vivienda y la alimentación concentran la mayor parte del ingreso en toda la región**

El desglose de gasto por país muestra que la vivienda y la alimentación combinadas representan entre el 48.3% (Perú) y el 57.9% (Argentina) del ingreso mensual en los seis países. Esto confirma que las categorías de gasto fijo, y no el gasto discrecional como entretenimiento, son las que más limitan la capacidad de ahorro de los usuarios en la región, especialmente en los países con mayor carga de vivienda identificados en el Hallazgo 1. Futuro Digital LatAm debería enfocar sus herramientas de optimización de gasto en vivienda y alimentación en lugar de en el gasto discrecional, ya que estas dos categorías representan la mayor palanca real de ahorro potencial.

**Fuente:** Desglose promedio de gasto por categoría e ingreso (`data/latam_finanzas_clean.csv`, calculado en `scripts/04_visualise.py`) — gráfico: `charts/05_spending_breakdown.png`
