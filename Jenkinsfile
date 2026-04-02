pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        REPO_URL = "https://github.com/veronica-1982/ACEest.git"
        BRANCH = "main"
    }

    stages {

        stage('Checkout') {
            steps {
                git url: "${REPO_URL}", branch: "${BRANCH}"
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 --version

                python3 -m venv $VENV_DIR
                . $VENV_DIR/bin/activate

                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                . $VENV_DIR/bin/activate
                pip install flake8
                flake8 . --max-line-length=120 --exit-zero
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . $VENV_DIR/bin/activate
                pytest -v
                '''
            }
        }

        stage('Run App') {
            steps {
                sh '''
                . $VENV_DIR/bin/activate
                nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }

        stage('Health Check') {
            steps {
                sleep time: 5, unit: 'SECONDS'
                sh 'curl --fail http://localhost:5000'
            }
        }
    }

    post {
        always {
            echo " Cleaning up..."
            sh '''
            pkill -f "python3 app.py" || true
            '''
        }

        success {
            echo "Build + Test + App Run Successful"
        }

        failure {
            echo "Pipeline Failed"
        }
    }
}
