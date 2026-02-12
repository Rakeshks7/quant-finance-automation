#  Earnings Call Audio Analysis (Multimodal AI)

A forensic intelligence tool that processes raw audio from quarterly earnings calls. It uses **OpenAI Whisper** to transcribe speech to text and **GPT-4** to perform behavioral analysis on the management team.

## Workflow Logic
1.  **Input:** User provides a link to the earnings call MP3 (e.g., `https://ir.tesla.com/q4.mp3`).
2.  **Transcription:** The `OpenAI Whisper` node converts the audio into a high-fidelity text transcript.
3.  **Analysis:** The text is fed into an LLM with a specific prompt to detect:
    * **Hesitation/Doubt:** (e.g., "Um, we hope to, uh, maybe reach targets.")
    * **Evasion:** (e.g., Answering a different question than was asked.)
4.  **Output:** A "Confidence Score" (0-10) is generated. A low score indicates management is hiding bad news, potentially triggering a "Short" signal.

## Why this is Alpha
Most algorithms only read the press release numbers (EPS/Revenue). This workflow analyzes the *human element*, giving you an edge over purely quantitative systems.