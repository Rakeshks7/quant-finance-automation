#  Club Member Onboarding (Automated Vetting)

A fully automated recruitment pipeline for the **Praxis Finance Club**. It screens applicants via a technical quiz and automatically onboards the top talent.

## Workflow Logic
1.  **Trigger:** Listens for new submissions from the Application Form (Typeform/Google Forms).
2.  **Scoring Engine:** The Code Node acts as the "Exam Proctor."
    * It checks the applicant's answers against a secure `quiz_answer_key.json`.
    * Calculates the score.
3.  **Decision Gate:**
    * **Score >= 80%:** The user is added to the Notion "Member Directory" and emailed a one-time Discord Invite link.
    * **Score < 80%:** The user is sent a polite rejection email with resources to study.

## Setup
* **Webhooks:** Configure your Typeform to POST to the n8n production URL.
* **Notion:** Ensure the n8n integration has "Connect" access to your Members database.