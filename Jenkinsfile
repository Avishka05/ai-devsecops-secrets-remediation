pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Baseline Secret Scan') {
            steps {
                bat 'python -c "from app.scanner import scan_directory; print(scan_directory())"'
            }
        }

        stage('AI Contextual Analysis') {
            steps {
                bat 'python -c "from app.scanner import scan_directory; from app.ai_remediator import analyze_finding; [print(analyze_finding(item)) for item in scan_directory()]"'
            }
        }

        stage('Security Gate') {
            steps {
                bat 'python -c "from app.scanner import scan_directory; findings = scan_directory(); print(f\"Security Gate completed: {len(findings)} findings reviewed\")"'
            }
        }
    }
}