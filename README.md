# Análisis LatAm 2025 — Pipeline de Bienestar Financiero

## Propósito del proyecto

Este repositorio contiene el proyecto final de capstone: un pipeline repetible de
análisis de bienestar financiero para **Futuro Digital LatAm**, construido sobre
el trabajo previo de **Midterm II / Option B**. El objetivo es tomar una encuesta
cruda de bienestar financiero de 500 jóvenes profesionales (18–32 años) en seis
países de América Latina (México, Colombia, Argentina, Chile, Perú y Brasil), y
convertirla — a través de un pipeline de seis fases, validado y documentado en
cada paso — en un informe ejecutivo con hallazgos accionables para el negocio.

Todo el pipeline se ejecutó con Claude Code, usando hooks, skills y un agente
personalizado configurados en `.claude/`, con cada fase confirmada y comiteada
individualmente antes de avanzar a la siguiente.

## Estructura de carpetas

```
.
├── .claude/                       # Configuración de Claude Code para este proyecto
│   ├── agents/
│   │   └── country-profiler.md    # Agente para generar perfiles estadísticos por país
│   ├── hooks/
│   │   ├── chart-counter.sh       # Cuenta gráficos guardados en charts/ (hook PostToolUse: Write)
│   │   ├── session-logger.sh      # Registra cada comando Bash en session-log.md
│   │   └── validate-phases.sh     # Verifica qué fases del pipeline están completas (hook Stop)
│   ├── settings.json               # Hooks + servidor MCP de Notion (clave de marcador de posición)
│   ├── settings.local.json.example # Plantilla para la clave real de Notion (ver sección MCP más abajo)
│   └── skills/
│       ├── interpret/SKILL.md         # Formato de interpretación de 3 oraciones en español
│       └── publish-finding/SKILL.md   # Publicación de hallazgos a Notion
├── data/
│   ├── latam_finanzas_2025.csv     # Dataset crudo (500 filas, 21 columnas)
│   └── latam_finanzas_clean.csv    # Dataset limpio (500 filas, 22 columnas) — Fase 2
├── scripts/
│   ├── 01_explore.py               # Fase 1 — exploración inicial
│   ├── 02_clean.py                 # Fase 2 — limpieza documentada
│   ├── 03_analyse.py               # Fase 3 — seis análisis estadísticos
│   ├── 04_visualise.py             # Fase 4 — cinco gráficos de respaldo
│   ├── country_Mexico.py, country_Colombia.py, country_Argentina.py,
│   │   country_Chile.py, country_Peru.py, country_Brasil.py   # Fase 2.5 — perfiles por país
│   ├── country_profiles.md         # Fase 2.5 — perfiles combinados
│   ├── analysis_findings.md        # Fase 3 — seis hallazgos con estadísticas
│   └── interpretations.md          # Fase 5 — interpretaciones en español (formato /interpret)
├── charts/                          # Fase 4 — 5 gráficos PNG
├── data-quality-log.md             # Fase 2 — decisiones de limpieza documentadas
├── analysis-report.md              # Fase 6 — informe ejecutivo final (español)
├── final-deliverables.md           # Checklist de entregables finales
├── session-log.md                  # Registro automático de cada comando ejecutado (hook)
└── CLAUDE.md                       # Instrucciones del proyecto para Claude Code
```

## Cómo ejecutar los scripts

Requiere Python del sistema (sin entorno virtual) con `pandas`, `matplotlib`,
`seaborn` y `scipy` instalados:

```bash
python -m pip install pandas matplotlib seaborn scipy
```

Los scripts se ejecutan en orden, cada uno depende del artefacto generado por
el anterior:

```bash
python scripts/01_explore.py      # Explora data/latam_finanzas_2025.csv
python scripts/02_clean.py        # Genera data/latam_finanzas_clean.csv
python scripts/country_Mexico.py  # (y los otros 5 country_*.py) — perfiles por país
python scripts/03_analyse.py      # Genera scripts/analysis_findings.md
python scripts/04_visualise.py    # Genera los 5 PNG en charts/
```

`scripts/interpretations.md` y `analysis-report.md` fueron escritos directamente
a partir de los resultados de `03_analyse.py` y `04_visualise.py` (Fases 5 y 6),
no son generados por un script automático.

## Qué produjo cada fase

| Fase | Entregable principal | Contenido |
|---|---|---|
| **1 — Exploración** | `scripts/01_explore.py` | Dimensiones, tipos de datos, valores faltantes, estadísticas descriptivas y conteos categóricos del dataset crudo |
| **2 — Limpieza** | `scripts/02_clean.py`, `data-quality-log.md`, `data/latam_finanzas_clean.csv` | Estandarización de categorías, conversión a booleanos, imputación documentada de `gasto_salud_usd`, preservación de ahorro negativo válido |
| **2.5 — Perfiles por país** | `scripts/country_*.py`, `scripts/country_profiles.md` | Perfil estadístico y de negocio para cada uno de los 6 países, generado con el agente `country-profiler` |
| **3 — Análisis** | `scripts/03_analyse.py`, `scripts/analysis_findings.md` | Seis análisis con pruebas estadísticas formales (ANOVA, correlación de Pearson, chi-cuadrado), incluyendo hallazgos nulos reportados con transparencia |
| **4 — Visualización** | `scripts/04_visualise.py`, `charts/*.png` | Cinco gráficos que respaldan los hallazgos más relevantes de la Fase 3 |
| **5 — Interpretación** | `scripts/interpretations.md` | Interpretaciones de negocio en español (formato de 3 oraciones: hecho, implicación, recomendación) usando el skill `/interpret` |
| **6 — Informe final** | `analysis-report.md`, `final-deliverables.md` | Informe ejecutivo consolidado para stakeholders y checklist de entregables |

## Configuración de hooks, skills y agente

- **Hooks** (`.claude/settings.json` → `hooks`):
  - `session-logger.sh` — se dispara en `PostToolUse` para el matcher `Bash`; registra cada comando ejecutado en `session-log.md` con marca de tiempo.
  - `chart-counter.sh` — se dispara en `PostToolUse` para el matcher `Write`; cuenta cuántos de los 5 gráficos esperados existen en `charts/`. Nota: como los gráficos de este proyecto se generan con `matplotlib.savefig()` dentro de un script de Python (no con la herramienta Write), este hook no se activa durante la Fase 4; la verificación de los 5 PNG se hizo manualmente con `ls`.
  - `validate-phases.sh` — se dispara en `Stop`; imprime qué fases del pipeline (2, 2.5, 3, 4, 6) tienen su entregable presente en el repositorio.
- **Skills** (`.claude/skills/`):
  - `/interpret` — formato fijo de 3 oraciones en español para interpretar un hallazgo estadístico.
  - `/publish-finding` — publica un hallazgo completado a la base de datos "Findings Tracker" de Notion.
- **Agente** (`.claude/agents/country-profiler.md`):
  - Agente especializado que, dado un país, lee `data/latam_finanzas_clean.csv` y genera una sección Markdown con estadísticas de ingreso, gasto, ahorro y satisfacción para ese país. Se usó en paralelo para los 6 países en la Fase 2.5.

## Configuración de Notion (MCP)

`.claude/settings.json` define el servidor MCP `notion` (`@notionhq/notion-mcp-server`)
para publicar hallazgos y el informe final directamente a Notion. **La clave de
API incluida en el repositorio es un valor de marcador de posición**
(`YOUR_NOTION_API_KEY`) y no es funcional.

Para habilitar la publicación real a Notion en tu entorno local:

1. Copia `.claude/settings.local.json.example` a `.claude/settings.local.json`.
2. Reemplaza `YOUR_NOTION_API_KEY` con tu clave real de integración de Notion.
3. `settings.local.json` está en `.gitignore` y se fusiona sobre `settings.json`,
   por lo que la clave real **nunca se sube al repositorio**.

Mientras la clave siga siendo un marcador de posición, ningún hallazgo ni el
informe final deben publicarse en Notion — esto se respetó durante todo el
desarrollo del proyecto.

## Entregables finales incluidos en este repositorio

- `analysis-report.md` — informe ejecutivo final en español
- `final-deliverables.md` — checklist completo de entregables (incluye los pendientes fuera del repo: URL de GitHub, ZIP, video demo, URL de Notion)
- `data-quality-log.md` — registro de decisiones de limpieza de datos
- `session-log.md` — registro automático de todos los comandos ejecutados durante el proyecto
- `data/latam_finanzas_2025.csv` y `data/latam_finanzas_clean.csv` — datasets crudo y limpio
- `scripts/` — los 4 scripts numerados de fase, 6 scripts de perfil de país, y los 3 archivos Markdown intermedios (`country_profiles.md`, `analysis_findings.md`, `interpretations.md`)
- `charts/` — los 5 gráficos PNG que respaldan los hallazgos principales
- `.claude/` — configuración completa de settings, hooks, skills y agente usada para producir este pipeline

No incluidos en el repositorio (ver `final-deliverables.md`): la URL del repo de
GitHub una vez publicado, el archivo ZIP del proyecto, el video de demostración,
y la URL del workspace de Notion — pendientes hasta completar los pasos finales
de publicación.
