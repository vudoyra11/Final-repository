# Análisis de Bienestar Financiero LatAm 2025
### Informe Ejecutivo — Futuro Digital LatAm

**Fecha:** 3 de julio de 2026
**Fuente de datos:** `data/latam_finanzas_2025.csv` (500 encuestados, 6 países)
**Autores del pipeline:** Equipo de Análisis de Datos, con asistencia de Claude Code

---

## 1. Resumen ejecutivo

Este informe presenta los resultados del análisis de la Encuesta de Bienestar Financiero 2025, realizada sobre 500 profesionales jóvenes (18–32 años) en seis países de América Latina: México, Colombia, Argentina, Chile, Perú y Brasil. El objetivo es identificar patrones de ingreso, gasto, ahorro, deuda y bienestar financiero que permitan a Futuro Digital LatAm priorizar sus productos y su programa de educación financiera.

Los hallazgos principales muestran que **la carga de vivienda y el nivel de ingreso varían de forma significativa por país** (no por industria), y que **el uso de herramientas de inteligencia artificial financiera es el predictor más fuerte de satisfacción financiera** encontrado en todo el análisis. También se identificó que los usuarios más jóvenes ahorran significativamente menos que sus pares de mayor edad, y que el gasto en vivienda y alimentación concentra la mayor parte del ingreso mensual en toda la región.

Es importante destacar que varias hipótesis intuitivas —como que la deuda o su relación con el ingreso predicen directamente la insatisfacción financiera— **no encontraron respaldo estadístico** en esta muestra. Este informe reporta esos resultados nulos con la misma transparencia que los hallazgos positivos, para evitar decisiones de producto basadas en supuestos no confirmados por los datos.

---

## 2. Metodología

El pipeline de análisis se ejecutó en seis fases secuenciales, cada una validada y confirmada antes de avanzar a la siguiente:

| Fase | Entregable | Descripción |
|---|---|---|
| 1 | `scripts/01_explore.py` | Exploración inicial: dimensiones, tipos de datos, valores faltantes, estadísticas descriptivas |
| 2 | `scripts/02_clean.py`, `data-quality-log.md` | Limpieza documentada del dataset |
| 2.5 | `scripts/country_*.py`, `scripts/country_profiles.md` | Perfiles estadísticos por país (agente `country-profiler`) |
| 3 | `scripts/03_analyse.py`, `scripts/analysis_findings.md` | Seis análisis estadísticos con pruebas formales (ANOVA, correlación de Pearson, chi-cuadrado) |
| 4 | `scripts/04_visualise.py`, `charts/*.png` | Cinco visualizaciones de respaldo para los hallazgos principales |
| 5 | `scripts/interpretations.md` | Interpretaciones de negocio en español, formato de 3 oraciones por hallazgo |
| 6 | `analysis-report.md` (este documento) | Síntesis ejecutiva para stakeholders |

Todas las pruebas estadísticas usan un umbral de significancia de **alpha = 0.05**. El pipeline se ejecutó con Python del sistema (pandas, matplotlib, seaborn, scipy), sin entornos virtuales, según lo especificado por el equipo. Cada paso quedó registrado automáticamente en `session-log.md` mediante hooks de `.claude/settings.json` (registro de sesión y contador de gráficos), y un hook de validación de fases (`validate-phases.sh`) confirma al final de cada respuesta qué entregables existen en el repositorio.

---

## 3. Calidad de datos y decisiones de limpieza

El dataset original contenía 500 filas y 21 columnas. Se aplicaron las siguientes decisiones de limpieza, documentadas en detalle en `data-quality-log.md`:

1. **Estandarización de `industria`:** se consolidaron cuatro variantes de "Tecnología" (`Tecnología`, `Tecnologia`, `tech`, `TECNOLOGÍA`) en una sola categoría, resultando en 57 registros combinados.
2. **Conversión de columnas Sí/No a booleanos:** `tiene_tarjeta_credito`, `tiene_cuenta_ahorro` y `tiene_deuda` se convirtieron a valores booleanos nativos.
3. **Imputación de `gasto_salud_usd`:** 33 registros (6.6%) tenían este valor faltante; se imputaron con la mediana (45.66 USD), robusta frente al sesgo observado en la distribución. Se añadió la columna `gasto_salud_usd_imputed` para mantener trazabilidad.
4. **Preservación de ahorro negativo:** 74 registros (14.8%) muestran ahorro mensual negativo. Se verificó que estos valores son consistentes con el ingreso y gasto de cada fila (déficit promedio de -36 USD, máximo -53% del ingreso de esa fila) y se conservaron como señal válida de sobregasto, sin recortes ni imputaciones.
5. **Verificación de unicidad:** 0 filas duplicadas y 0 IDs duplicados, confirmado en las Fases 1 y 2.
6. **Nota sobre codificación:** los caracteres acentuados (México, Perú, Sí, etc.) están correctamente codificados en UTF-8 en el archivo fuente; cualquier visualización distorsionada observada en consola durante el desarrollo fue un artefacto de la página de códigos de Windows (850), no un problema de los datos.

El dataset resultante (`data/latam_finanzas_clean.csv`) tiene 500 filas y 22 columnas (se añadió la columna de trazabilidad de imputación), sin valores faltantes ni duplicados.

---

## 4. Resumen de perfiles por país

El agente `country-profiler` generó un perfil estadístico independiente para cada país (`scripts/country_profiles.md`). Resumen comparativo:

| País | n | Ingreso mediano | Carga de vivienda | Ahorro promedio | % ahorro negativo | Señal de riesgo principal |
|---|---|---|---|---|---|---|
| México | 150 | 1,066.99 USD | 28.15% | 102.18 USD | 15.33% | Mayor razón deuda/ingreso de la región (2.04x) |
| Colombia | 80 | 856.62 USD | 25.41% | 81.75 USD | 18.75% | Subgrupo de riesgo oculto por el promedio agregado |
| Argentina | 70 | 798.49 USD | 34.09% (máxima) | 76.89 USD | 7.14% (mínima) | Mayor carga de vivienda, menor satisfacción |
| Chile | 70 | 1,246.01 USD | 32.55% | 117.63 USD | 11.43% | Carga de vivienda estructural pese a alto ingreso |
| Perú | 65 | 821.59 USD | 24.63% (mínima) | 80.84 USD | 20.00% (máxima) | Mayor incidencia de deuda y ahorro negativo |
| Brasil | 65 | 1,458.03 USD (máxima) | 26.90% | 134.84 USD (máximo) | 15.38% | Deuda ~4x el ingreso mensual |

---

## 5. Cinco hallazgos principales

*(Formato de interpretación completo en `scripts/interpretations.md`; estadísticas detalladas en `scripts/analysis_findings.md`.)*

**Hallazgo 1 — La carga de vivienda supera el umbral crítico en Argentina y Chile**
Argentina destina el 34.1% del ingreso mensual a vivienda y Chile el 32.6%, superando el umbral convencional de "carga excesiva" (30%), con diferencias significativas entre países (ANOVA F=39.50, p<0.001).
*Gráfico:* `charts/04_housing_burden_by_country.png`

**Hallazgo 2 — El ingreso varía significativamente por país, no por industria**
El ingreso promedio va de 766 USD (Argentina) a 1,388 USD (Brasil), diferencia significativa por país (F=44.28, p<0.001), mientras que la industria no mostró un efecto significativo (F=0.50, p=0.87).
*Gráfico:* `charts/02_income_by_country.png`

**Hallazgo 3 — El uso de herramientas de IA es el predictor más fuerte de satisfacción financiera**
La correlación entre horas semanales de uso de IA y satisfacción financiera es la más fuerte de todo el análisis (r=0.571, p<0.001).
*Gráfico:* `charts/03_ai_usage_vs_satisfaction.png`

**Hallazgo 4 — Los usuarios más jóvenes ahorran menos**
La edad se correlaciona positivamente con el ahorro mensual (r=0.385, p<0.001); los usuarios más jóvenes del rango 18-32 años ahorran montos significativamente menores.
*Gráfico:* `charts/01_age_vs_savings.png`

**Hallazgo 5 — Vivienda y alimentación concentran la mayor parte del ingreso regional**
Estas dos categorías combinadas representan entre el 48.3% (Perú) y el 57.9% (Argentina) del ingreso mensual en los seis países.
*Gráfico:* `charts/05_spending_breakdown.png`

### Hallazgos nulos relevantes (transparencia metodológica)
Tres relaciones hipotetizadas en la Fase 3 **no resultaron estadísticamente significativas** y por ello no se presentan como hallazgos principales, pero se documentan por su valor para evitar decisiones erróneas: (a) la razón deuda/ingreso no predice la satisfacción financiera (r=-0.044, p=0.32); (b) tener deuda no predice de forma significativa un ahorro mensual negativo (chi²=0.29, p=0.59); (c) la meta financiera declarada no difiere significativamente por país a nivel agregado (chi²=38.78, p=0.30), pese a las diferencias descriptivas observadas en los perfiles de país. Detalle completo en `scripts/analysis_findings.md`, Hallazgos 4-6.

---

## 6. Recomendaciones

1. **Priorizar el desarrollo de funciones de IA financiera** como palanca principal de satisfacción, validando primero la dirección causal de la relación (Hallazgo 3).
2. **Segmentar productos y precios por país, no por industria**, dado que el país es el eje de ingreso estadísticamente relevante (Hallazgo 2).
3. **Enfocar herramientas de optimización de gasto en vivienda y alimentación**, no en gasto discrecional, especialmente en Argentina y Chile (Hallazgos 1 y 5).
4. **Diseñar contenido de ahorro dirigido a usuarios jóvenes**, dado que la capacidad de ahorro aumenta con la edad incluso dentro de este rango etario acotado (Hallazgo 4).
5. **Evitar el uso de la bandera binaria "tiene deuda" como único indicador de riesgo**; usar en su lugar la razón deuda/ingreso continua o las tasas de ahorro negativo por país, ya que la bandera binaria no mostró poder discriminativo significativo.
6. **Tratar la narrativa de metas financieras por país como hipótesis, no como hecho confirmado**, hasta contar con una muestra mayor o una encuesta dirigida.

---

## 7. Limitaciones

- **Tamaño de muestra por país:** entre 65 y 150 encuestados por país, lo cual limita el poder estadístico de algunas pruebas (p. ej., la tabla de contingencia meta financiera × país tiene 35 grados de libertad y celdas con conteos bajos).
- **Rango etario acotado:** la muestra cubre únicamente 18–32 años, por lo que los hallazgos no son generalizables a poblaciones de mayor edad.
- **Correlación, no causalidad:** las relaciones significativas (p. ej., uso de IA y satisfacción) son correlacionales; no se puede afirmar que una causa la otra sin un diseño experimental adicional.
- **Imputación de datos faltantes:** el 6.6% de los valores de `gasto_salud_usd` se imputó con la mediana global, lo cual puede subestimar la variabilidad real del gasto en salud.
- **Autoevaluación de satisfacción:** `satisfaccion_financiera` es una medida subjetiva de 1 a 5, sujeta a sesgos culturales de respuesta entre países.

---

## 8. Estado de publicación en Notion

La integración de Notion está **configurada pero no ejecutada**. El archivo `.claude/settings.json` incluye el servidor MCP `notion` (`@notionhq/notion-mcp-server`) con las bases de datos "Findings Tracker" y "Country Profiles", y el skill `/publish-finding` está listo para usarse. Sin embargo, la clave de API en `OPENAPI_MCP_HEADERS` es actualmente un valor de marcador de posición (`YOUR_NOTION_API_KEY`). **No se publicó ningún hallazgo ni este informe en Notion** hasta que se configure una clave de API real y verificada, conforme a las instrucciones recibidas en cada fase del proyecto.

---

## 9. Conclusión

El análisis confirma que el bienestar financiero de los jóvenes profesionales de América Latina está determinado principalmente por factores estructurales de país (costo de vivienda, nivel de ingreso) y por el compromiso con herramientas digitales de gestión financiera, más que por la industria de empleo o la sola tenencia de deuda. Estos resultados —incluyendo los hallazgos nulos reportados con la misma rigurosidad— ofrecen a Futuro Digital LatAm una base sólida y honesta para priorizar el desarrollo de producto: invertir en funciones de IA financiera, segmentar por país, y dirigir la educación financiera hacia el control del gasto fijo (vivienda y alimentación) y el fomento del ahorro temprano en usuarios jóvenes.

El pipeline completo —desde la exploración inicial hasta este informe— es reproducible mediante los scripts en `scripts/`, está documentado en cada fase, y queda registrado íntegramente en `session-log.md`.
