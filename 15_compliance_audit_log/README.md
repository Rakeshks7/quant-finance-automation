# 🏛️ Compliance Audit Log

An automated governance workflow that generates a statutory "End of Day" report. It consolidates all algorithmic activity into a human-readable format and stores it in an immutable location for future auditing.

## Workflow Logic
1.  **Trigger:** Scheduled for 11:55 PM daily (End of Day).
2.  **Data Gathering:** Queries the SQL Ledger for all trades executed `WHERE date = CURRENT_DATE`.
3.  **Report Generation:**
    * Maps the raw data into a standardized HTML/PDF template.
    * Generates a unique Checksum/Hash for the file to prove non-tampering.
4.  **Archival:** Uploads the file to an AWS S3 Bucket configured with **Object Lock** (WORM - Write Once, Read Many).
5.  **Distribution:** Emails the file to the Internal Auditor/Compliance Officer.

## Why this is critical
For any regulated financial entity (or a serious proprietary desk), having a clear, unalterable history of *why* a bot made a trade is a legal requirement. This bot automates that compliance.