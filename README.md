# Phishing Email Analyser

An AI-powered tool that analyzes emails for phishing indicators using the Groq API (Llama 3.3 70B model).

## What it does
- Accepts pasted email content (multi-line supported)
- Checks sender domain legitimacy
- Detects psychological manipulation tactics (urgency, authority, curiosity)
- Flags suspicious links
- Returns a structured verdict: PHISHING / LEGITIMATE / SUSPICIOUS

## How to run it
1. Clone this repo
2. Install dependencies: `pip install groq`
3. Get a free API key from console.groq.com
4. Set it as an environment variable named `GROQ_API_KEY`
5. Run: `python phishing_analyzer.py`

## Built with
- Python
- Groq API (Llama 3.3 70B)
