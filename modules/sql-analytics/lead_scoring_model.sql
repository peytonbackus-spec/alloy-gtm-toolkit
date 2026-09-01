-- Scores enriched leads against ICP fit + engagement signals
-- Feeds BI layer (Looker/Tableau) for GTM leadership reporting

SELECT
    lead_id,
    icp_fit_score,
    engagement_score,
    (icp_fit_score * 0.6 + engagement_score * 0.4) AS composite_score
FROM enriched_leads
WHERE created_at >= CURRENT_DATE - INTERVAL '30 days';
