pipeline {
    agent any

    environment {
        PYTHON_EXE = 'C:\\Users\\Avishka\\Documents\\ai-devsecops-secrets-remediation\\.venv\\Scripts\\python.exe'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON_EXE%" -m pip install -r requirements.txt'
            }
        }

        stage('Baseline Secret Scan') {
            steps {
                bat '"%PYTHON_EXE%" -c "from app.scanner import scan_directory; print(scan_directory())"'
            }
        }

        stage('AI Contextual Analysis') {
            steps {
                bat '"%PYTHON_EXE%" -c "from app.scanner import scan_directory; from app.ai_remediator import analyze_finding; [print(analyze_finding(item)) for item in scan_directory()]"'
            }
        }

        stage('Security Gate') {
            steps {
                bat '''"%PYTHON_EXE%" -c "from app.scanner import scan_directory; print('Security Gate completed: ' + str(len(scan_directory())) + ' findings reviewed')"'''
            }
        }
    }
}