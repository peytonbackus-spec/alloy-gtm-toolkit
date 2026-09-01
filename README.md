# Alloy GTM & RevOps Execution Toolkit

End-to-end RevOps architecture, signal-based prospecting engines, dynamic waterfall rules, and identity decisioning ROI models built for enterprise financial technology and identity risk platforms.

## Architecture Overview

```
[Inbound Prospect / Signal Events]
                │
                ▼
   [Waterfall Enrichment Engine] ──── (ZeroBounce / Clay / Clearbit)
                │
                ▼
    [4-Tier L2A Matcher Cascade] ──── (Domain ➔ Legal Name ➔ Jaro-Winkler ➔ Fallback)
                │
                ├─► [FastAPI Webhook & Ingestion] ──── (Pydantic Validation / Health Check)
                │
                ▼
[Identity Decisioning & ROI Telemetry] (Risk Scoring / Fraud Loss / Co-Sell Attribution)
```

## Repository Structure

| Folder / File | Description |
| :--- | :--- |
| **`core/engine/`** | Asynchronous waterfall rules engine and 4-tier Lead-to-Account (L2A) matching cascade. |
| **`core/api/`** | FastAPI inbound enrichment receiver (`POST /api/v1/enrich`) with Pydantic payload validation. |
| **`modules/identity-decisioning-roi/`** | ICP segmentation matrices, programmatic ROI calculators, and synthetic fraud loss engines. |
| **`modules/revops-architecture-telemetry/`** | Automated inbound lead scoring models and signal-matching fraud risk prospecting scripts. |
| **`config/`** | YAML rulesets for dynamic waterfall routing, enrichment providers, and scoring models. |
| **`tests/`** | Full pytest suite covering rule engines, API webhooks, and matcher logic (21 passing tests). |
| **`gtm_menu.sh`** | Interactive CLI execution menu for local testing and demonstration. |

## Quick Start (Toolkit)

```zsh
# Run interactive CLI menu
./gtm_menu.sh

# Launch FastAPI webhook ingestion server
PYTHONPATH=. .venv/bin/python3 -m uvicorn core.api.webhook:app --reload

# Run test suite
PYTHONPATH=. .venv/bin/python3 -m pytest tests/ -v
```

## GTM Stack Coverage (added for Alloy GTM Engineer alignment)

| Folder | Description |
|---|---|
| `core/integrations/salesforce/` | Salesforce CRM sync client (Lead/Contact/Opportunity upsert). |
| `core/integrations/ipaas/` | n8n and Zapier workflow definitions for enrichment-to-CRM automation. |
| `modules/sql-analytics/` | SQL models feeding BI reporting (Looker/Tableau-ready). |
| `modules/sales-engagement/` | Outreach/Salesloft/Gong sync stubs. |
| `modules/customer-success/` | Gainsight/ChurnZero sync stubs. |
