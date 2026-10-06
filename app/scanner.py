import re
from pathlib import Path

RULES = {
    "Hardcoded Password": r'(?i)(password|passwd)\s*=\s*["\'][^"\']+["\']',
    "API Key": r'(?i)(api_key|apikey)\s*=\s*["\'][^"\']+["\']',
    "GitHub Token": r'ghp_[A-Za-z0-9_]+',
}

def scan_directory(directory="sample_code"):
    findings = []

    for file_path in Path(directory).rglob("*"):
        if not file_path.is_file():
            continue

        try:
            lines = file_path.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue

        for line_number, line in enumerate(lines, start=1):
            for rule_name, pattern in RULES.items():
                if re.search(pattern, line):
                    findings.append({
                        "file": str(file_path),
                        "line": line_number,
                        "rule": rule_name,
                        "snippet": "[REDACTED FOR SAFE ANALYSIS]"
                    })

    return findings