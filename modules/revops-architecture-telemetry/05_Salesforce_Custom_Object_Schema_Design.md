# Salesforce Custom Object Schema & Data Model Architecture

## Custom Objects Design
1. **`Decision_Waterfall__c`**: Tracks specific vendor API sequencing, fallback logic, and latency SLAs per client.
2. **`Verification_Trial__c`**: Captures proof-of-concept benchmark performance (auto-approval %, false positive rates).
3. **`Data_Partner_Attribution__c`**: Maps co-sell revenue attribution across external identity data providers.
