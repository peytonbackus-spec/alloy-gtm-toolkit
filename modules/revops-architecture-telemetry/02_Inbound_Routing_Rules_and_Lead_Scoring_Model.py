#!/usr/bin/env python3
"""
Automated Inbound Routing & Lead Scoring Engine
Routes leads to Enterprise Bank vs. Commercial Fintech sales pods based on firmographics and risk profile.
"""
import json

def score_and_route_lead(lead_data):
    score = 0
    # Firmographic Scoring
    if lead_data.get("asset_size_millions", 0) > 1000 or lead_data.get("monthly_active_users", 0) > 250000:
        score += 50
    if lead_data.get("has_fraud_executive_hire", False):
        score += 30
    if "Salesforce" in lead_data.get("tech_stack", []):
        score += 20
        
    # Segment Assignment
    segment = "Enterprise Bank Pod" if lead_data.get("is_chartered_bank", False) else "Mid-Market Fintech Pod"
    tier = "Tier 1 - Priority Outreach" if score >= 70 else "Tier 2 - Nurture Workflow"
    
    return {
        "company": lead_data["company"],
        "calculated_score": score,
        "target_segment": segment,
        "routing_action": tier
    }

if __name__ == "__main__":
    print("\n[+] Simulating Inbound Lead Routing Logic...")
    sample_lead = {
        "company": "Horizon Commercial Bank",
        "asset_size_millions": 2400,
        "is_chartered_bank": True,
        "has_fraud_executive_hire": True,
        "tech_stack": ["Salesforce", "Experian"]
    }
    print(json.dumps(score_and_route_lead(sample_lead), indent=2))
