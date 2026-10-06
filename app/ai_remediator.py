import os
from google import genai


def analyze_finding(finding):
    api_key = os.getenv("GEMINI_API_KEY")

    # The project still works without an API key.
    # This is your safe fallback for the demo.
    if not api_key:
        return {
            "severity": "High",
            "explanation": (
                f"A possible {finding['rule']} was detected in "
                f"{finding['file']} at line {finding['line']}."
            ),
            "remediation": (
                "Remove the hardcoded value, rotate the affected credential, "
                "store it as an environment variable or in a secret manager, "
                "and prevent future commits using CI secret scanning."
            ),
            "source": "Safe local fallback"
        }

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are an AI assistant in a DevSecOps CI/CD pipeline.

Analyze this redacted secret-scanning finding:
Rule: {finding['rule']}
File: {finding['file']}
Line: {finding['line']}
Detected value: REDACTED

Give a concise response in this format:
Severity: Low, Medium, High, or Critical
Risk: one short sentence
Remediation: two practical steps

Never request, expose, or infer the actual secret value.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "severity": "AI Reviewed",
        "explanation": response.text,
        "remediation": "Follow the Gemini-generated remediation above.",
        "source": "Gemini AI"
    }