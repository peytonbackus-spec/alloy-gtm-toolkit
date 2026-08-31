#!/usr/bin/env python3
"""
Fraud Loss Reduction & Synthetic ID Economics Model
Calculates annual savings achieved by reducing synthetic identity fraud and false positives.
"""
import json

def calculate_fraud_mitigation_roi(annual_onboarded_users, avg_loss_per_fraud_case, baseline_fraud_rate_bps, target_reduction_pct):
    baseline_fraud_cases = annual_onboarded_users * (baseline_fraud_rate_bps / 10000.0)
    baseline_losses = baseline_fraud_cases * avg_loss_per_fraud_case
    
    prevented_fraud_cases = baseline_fraud_cases * target_reduction_pct
    annual_savings = prevented_fraud_cases * avg_loss_per_fraud_case
    
    return {
        "annual_onboarded_users": annual_onboarded_users,
        "baseline_fraud_losses": f"${baseline_losses:,.2f}",
        "prevented_fraud_cases": round(prevented_fraud_cases, 1),
        "annual_fraud_loss_savings": f"${annual_savings:,.2f}"
    }

if __name__ == "__main__":
    print("\n[+] Running Fraud Loss & Synthetic ID Reduction Model...")
    res = calculate_fraud_mitigation_roi(
        annual_onboarded_users=500000,
        avg_loss_per_fraud_case=4500,
        baseline_fraud_rate_bps=25,
        target_reduction_pct=0.40
    )
    print(json.dumps(res, indent=2))
