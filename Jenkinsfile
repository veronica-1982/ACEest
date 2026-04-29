pipeline {

    agent any

    environment {

        APP_NAME = "aceest"

        IMAGE_NAME = "2024tm93552/aceest"

        DOCKER_CREDS = credentials('dockerhub-creds')

        SONAR_TOKEN = credentials('sonar-token')

        SONAR_HOST_URL = "http://YOUR_SONAR_HOST:9000"

        KUBECONFIG = "$HOME/.kube/config"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/veronica-1982/ACEest.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv

                . venv/bin/activate

                pip install --upgrade pip

                pip install -r requirements.txt
                '''
            }
        }

        stage('Lint') {
            steps {
                sh '''
                . venv/bin/activate

                pip install flake8

                flake8 . --max-line-length=120
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate

                pip install pytest

                pytest -v
                '''
            }
        }

        stage('SonarQube Scan') {
            steps {
                sh '''
                sonar-scanner \
                  -Dsonar.projectKey=aceest \
                  -Dsonar.sources=. \
                  -Dsonar.host.url=$SONAR_HOST_URL \
                  -Dsonar.token=$SONAR_TOKEN
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME:latest .
                '''
            }
        }

        stage('DockerHub Login') {
            steps {
                sh '''
                echo $DOCKER_CREDS_PSW | docker login -u $DOCKER_CREDS_USR --password-stdin
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                docker push $IMAGE_NAME:latest
                '''
            }
        }

        stage('Deploy to Minikube') {
            steps {
                sh '''
                sed -i "s|YOUR_DOCKERHUB_USERNAME/aceest:latest|$IMAGE_NAME:latest|g" deployment.yaml

                kubectl apply -f deployment.yaml

                kubectl apply -f service.yaml
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                kubectl get pods

                kubectl get svc

                minikube service aceest-service --url
                '''
            }
        }
    }

    post {

        success {
            echo "Application successfully deployed to Minikube"
        }

        failure {
            echo "Pipeline failed"
        }
    }
}
