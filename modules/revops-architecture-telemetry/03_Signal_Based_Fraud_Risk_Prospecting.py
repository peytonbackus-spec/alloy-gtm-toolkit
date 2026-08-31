#!/usr/bin/env python3
"""
Signal-Based Outbound Engine for Financial Crime & Fraud Leadership
"""
import json

ACCOUNTS_PIPELINE = [
    {"account": "Apex Digital Bank", "type": "Neobank", "signals": ["New VP of Fraud Hired", "Adding Business Checking"], "icp_score": 92},
    {"account": "Heritage Regional Credit Union", "type": "Credit Union", "signals": ["Manual KYC Backlog Reported", "CFPB Compliance Audit"], "icp_score": 88},
    {"account": "PayFlow Commercial", "type": "B2B SaaS", "signals": ["Embedded Finance Launch"], "icp_score": 79}
]

def evaluate_signals():
    print("\n--- ALLOY SIGNAL-BASED OUTBOUND PROSPECTING PIPELINE ---")
    for acc in ACCOUNTS_PIPELINE:
        action = "High Priority Outbound" if acc["icp_score"] >= 85 else "Nurture Signal"
        print(f"Account: {acc['account']} | Type: {acc['type']} | ICP Score: {acc['icp_score']} | Action: {action}")
        print(f"Signals: {', '.join(acc['signals'])}")
        print("-" * 65)

if __name__ == "__main__":
    evaluate_signals()
