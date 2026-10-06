import json
from datetime import datetime
from pathlib import Path

from flask import Flask, render_template
from app.scanner import scan_directory
from app.ai_remediator import analyze_finding

app = Flask(__name__)


@app.route("/")
def dashboard():
    findings = scan_directory()
    enhanced_findings = []

    for finding in findings:
        ai_result = analyze_finding(finding)
        enhanced_findings.append({**finding, **ai_result})

    report = {
        "generated_at": datetime.now().strftime("%d %B %Y, %I:%M %p"),
        "total_findings": len(enhanced_findings),
        "findings": enhanced_findings
    }

    Path("reports").mkdir(exist_ok=True)
    Path("reports/security_report.json").write_text(
        json.dumps(report, indent=2),
        encoding="utf-8"
    )

    return render_template(
        "index.html",
        findings=enhanced_findings,
        total=len(enhanced_findings)
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)