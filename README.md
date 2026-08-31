# Alloy GTM & RevOps Execution Toolkit

End-to-end RevOps architecture, signal-based prospecting engines, and identity decisioning ROI models built for enterprise financial technology and identity risk platforms.

## Architecture Overview

- `modules/identity-decisioning-roi/`: Quantitative ROI models, ICP segmentation, and 270+ data partner co-sell attribution schemas.
- `modules/revops-architecture-telemetry/`: Signal prospecting scripts, Salesforce custom data models, and Clay enrichment workflows.

## Directory Architecture

### 1. Identity Decisioning & ROI Models (`/modules/identity-decisioning-roi/`)

* **`01_Fintech_vs_Bank_ICP_Segmentation.md`**: Firmographic segmentation matrix comparing Tier-1 Banks vs. Fast-Growth FinTech requirements.
* **`02_Data_Partner_CoSell_Attribution.md`**: Co-sell attribution schema across 270+ open data partner network integrations.
* **`03_KYC_KYB_Automation_Cost_Benchmarking.md`**: Cost-per-review benchmarks and manual review reduction models.
* **`04_Enterprise_Business_Case_Presentation_Deck_Outline.md`**: CRO/CFO executive presentation framework for vendor migration.
* **`05_Identity_Decisioning_ROI_Calculator.py`**: Programmatic ROI calculator modeling manual review savings and conversion lift.
* **`06_Data_Network_Partner_Economics.py`**: Unit economics model quantifying margin expansion via orchestration.
* **`07_Fraud_Loss_Reduction_and_Synthetic_ID_Model.py`**: Synthetic identity fraud mitigation and false-positive reduction engine.
* **`08_Discovery_and_MEDDPICC_Framework.md`**: Discovery questioning strategy and MEDDPICC criteria for risk leadership.

### 2. RevOps Architecture & Telemetry (`/modules/revops-architecture-telemetry/`)

* **`01_Fintech_Signal_Matrix_and_Trigger_Catalog.md`**: Catalog of intent signals (CFPB audits, risk hires, product launches).
* **`02_Inbound_Routing_Rules_and_Lead_Scoring_Model.py`**: Automated scoring engine routing leads between Enterprise and FinTech pods.
* **`03_Signal_Based_Fraud_Risk_Prospecting.py`**: Signal-matching script generating personalized outreach payloads.
* **`04_90_Day_RevOps_Execution_Roadmap.md`**: 90-day strategy roadmap covering audit, telemetry, and ROI standardization.
* **`05_Salesforce_Custom_Object_Schema_Design.md`**: Custom object ERD and data dictionary (`Decision_Waterfall__c`, `Verification_Trial__c`).
* **`06_Outreach_Sequence_Templates_Signal_Based.md`**: Outbound sequence templates matched to risk triggers.
* **`07_Pipeline_Stage_Gate_Telemetry_Engine.py`**: Stage velocity analyzer tracking deal slippage and SLA breaches.
* **`08_Salesforce_Data_Model_and_Pipeline_Telemetry.md`**: Stage exit criteria, SLA definitions, and funnel conversion tracking.
* **`09_Clay_Automation_Data_Network_Enrichment.py`**: Simulation of Clay waterfalls for automated domain enrichment.
* **`10_RevOps_Tech_Stack_and_Stage_Gate_SOP.md`**: Standard operating procedure for lead-to-opportunity pipeline flow.

## Quick Execution

### Interactive CLI Menu

Clone the repo, then launch the interactive terminal menu to run any model in the toolkit:

```zsh
git clone https://github.com/peytonbackus-spec/alloy-gtm-toolkit.git
cd alloy-gtm-toolkit
./gtm_menu.sh
```

### Run a Single Script Directly

```zsh
python3 modules/identity-decisioning-roi/05_Identity_Decisioning_ROI_Calculator.py
python3 modules/revops-architecture-telemetry/03_Signal_Based_Fraud_Risk_Prospecting.py
```

### Run the Test Suite

Verifies every script in `modules/` executes cleanly:

```zsh
python3 test_toolkit.py -v
```
