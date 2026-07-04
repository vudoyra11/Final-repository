# Checklist de Entregables Finales — Capstone Análisis LatAm 2025

Estado a fecha 2026-07-03. Marcado ✅ = completo y en el repositorio; ⬜ = pendiente.

| # | Entregable | Estado | Ubicación / Nota |
|---|---|---|---|
| 1 | URL del repositorio de GitHub | ✅ Completo | https://github.com/vudoyra11/Final-repository |
| 2 | Archivo ZIP del proyecto | ✅ Completo | `final-capstone-submission.zip` |
| 3 | Video de demostración | ⬜ Pendiente | No grabado aún |
| 4 | `analysis-report.md` | ✅ Completo | Raíz del repo — informe ejecutivo en español |
| 5 | Gráficos (`charts/`) | ✅ Completo | 5 PNG: `01_age_vs_savings.png`, `02_income_by_country.png`, `03_ai_usage_vs_satisfaction.png`, `04_housing_burden_by_country.png`, `05_spending_breakdown.png` |
| 6 | Scripts (`scripts/`) | ✅ Completo | `01_explore.py`, `02_clean.py`, `03_analyse.py`, `04_visualise.py`, 6 scripts `country_*.py`, más `country_profiles.md`, `analysis_findings.md`, `interpretations.md` |
| 7 | Configuración `.claude/` (settings, hooks, skills, agente) | ✅ Completo | `settings.json` (hooks + MCP Notion), `hooks/` (chart-counter, session-logger, validate-phases), `skills/interpret`, `skills/publish-finding`, `agents/country-profiler.md` |
| 8 | Registro de calidad de datos | ✅ Completo | `data-quality-log.md` |
| 9 | `session-log.md` | ✅ Completo | Actualizado automáticamente por el hook `session-logger.sh` en cada comando Bash |
| 10 | URL del workspace de Notion | ⬜ Pendiente | Placeholder — integración configurada en `.claude/settings.json` pero la clave de API (`OPENAPI_MCP_HEADERS`) sigue siendo un valor de marcador de posición; no se ha publicado nada en Notion (`[URL DEL WORKSPACE NOTION]`) |

## Resumen

- **Completo (8/10):** URL del repositorio de GitHub, archivo ZIP del proyecto, informe ejecutivo, gráficos, scripts, configuración de Claude Code, log de calidad de datos, session log, y (implícitamente) el dataset limpio que los respalda.
- **Pendiente (2/10):** video de demostración — y la URL del workspace de Notion, bloqueada hasta reemplazar la clave de API de marcador de posición por una clave real y verificada.

El repositorio ya fue pusheado a GitHub (https://github.com/vudoyra11/Final-repository). No se ha publicado nada en Notion, conforme a las instrucciones recibidas durante el proyecto.
