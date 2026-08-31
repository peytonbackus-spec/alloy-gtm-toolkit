#!/usr/bin/env python3
"""
Pipeline Stage Gate Telemetry & SLA Tracking Engine
Analyzes conversion velocity and flags deal slippage across enterprise sales stages.
"""
import json

def analyze_pipeline_telemetry(deal_cohort):
    print("\n[+] Analyzing Opportunity Stage Velocity & SLA Breaches...")
    metrics = []
    
    for deal in deal_cohort:
        stage_sla_days = {"Stage 1: Discovery": 14, "Stage 2: Technical Evaluation": 21, "Stage 3: InfoSec & Legal": 30}
        current_sla = stage_sla_days.get(deal["stage"], 14)
        sla_status = "OK" if deal["days_in_stage"] <= current_sla else "SLA BREACH"
        
        metrics.append({
            "account_name": deal["account"],
            "arr_value": f"${deal['arr']:,}",
            "current_stage": deal["stage"],
            "days_in_stage": deal["days_in_stage"],
            "max_sla_allowed": current_sla,
            "health_status": sla_status
        })
        
    return metrics

if __name__ == "__main__":
    sample_deals = [
        {"account": "Neobank Capital", "arr": 120000, "stage": "Stage 2: Technical Evaluation", "days_in_stage": 12},
        {"account": "Apex Commercial Bank", "arr": 350000, "stage": "Stage 3: InfoSec & Legal", "days_in_stage": 42},
        {"account": "PayFlow Payments", "arr": 85000, "stage": "Stage 1: Discovery", "days_in_stage": 18}
    ]
    report = analyze_pipeline_telemetry(sample_deals)
    print(json.dumps(report, indent=2))
