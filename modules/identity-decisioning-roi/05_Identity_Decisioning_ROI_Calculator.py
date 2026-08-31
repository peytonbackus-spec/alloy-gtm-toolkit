#!/usr/bin/env python3
"""
Alloy Identity Decisioning & Fraud Reduction ROI Calculator
Calculates manual review cost savings, fraud reduction, and payback timeline.
"""

def calculate_roi(monthly_volume, manual_review_rate, fraud_loss_rate_bps, cost_per_review=12.50):
    print("\n" + "="*70)
    echo_header = "ALLOY IDENTITY DECISIONING & FRAUD ROI ANALYSIS"
    print(f"{echo_header:^70}")
    print("="*70)
    
    annual_volume = monthly_volume * 12
    current_reviews = annual_volume * (manual_review_rate / 100.0)
    current_review_cost = current_reviews * cost_per_review
    
    target_review_rate = max(manual_review_rate * 0.20, 3.0)
    target_reviews = annual_volume * (target_review_rate / 100.0)
    target_review_cost = target_reviews * cost_per_review
    review_savings = current_review_cost - target_review_cost
    
    estimated_arr_volume = annual_volume * 250
    current_fraud_loss = estimated_arr_volume * (fraud_loss_rate_bps / 10000.0)
    target_fraud_loss = current_fraud_loss * 0.65
    fraud_savings = current_fraud_loss - target_fraud_loss
    
    total_annual_benefit = review_savings + fraud_savings
    estimated_alloy_arr = max(annual_volume * 0.08, 45000)
    net_roi = ((total_annual_benefit - estimated_alloy_arr) / estimated_alloy_arr) * 100
    payback_months = (estimated_alloy_arr / total_annual_benefit) * 12

    print(f"Annual Onboarding Volume:      {annual_volume:,.0f} accounts")
    print(f"Current Manual Review Cost:   ${current_review_cost:,.2f} ({manual_review_rate}% review rate)")
    print(f"Target Review Cost (Alloy):   ${target_review_cost:,.2f} ({target_review_rate:.1f}% review rate)")
    print(f"-"*70)
    print(f"Annual Operational Savings:   ${review_savings:,.2f}")
    print(f"Annual Fraud Loss Savings:    ${fraud_savings:,.2f}")
    print(f"Total Economic Value Delivered:${total_annual_benefit:,.2f}")
    print(f"Estimated Alloy ACV/ARR:      ${estimated_alloy_arr:,.2f}")
    print(f"Net First-Year ROI:           {net_roi:.1f}%")
    print(f"CAC / ACV Payback Period:     {payback_months:.1f} months")
    print("="*70 + "\n")

if __name__ == "__main__":
    print("Running Baseline Benchmark: Tier-2 Regional Bank (50k onboarding apps/mo)")
    calculate_roi(monthly_volume=50000, manual_review_rate=18.5, fraud_loss_rate_bps=12.0)
