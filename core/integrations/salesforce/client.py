"""
Salesforce REST/Bulk API client for CRM sync.
Handles bidirectional field mapping between enrichment engine and SF objects (Lead, Contact, Opportunity).
"""

class SalesforceClient:
    def __init__(self, instance_url: str, access_token: str):
        self.instance_url = instance_url
        self.access_token = access_token

    def upsert_lead(self, external_id: str, payload: dict) -> dict:
        raise NotImplementedError

    def sync_opportunity_stage(self, opportunity_id: str, stage: str) -> dict:
        raise NotImplementedError
