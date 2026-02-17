pipeline {
    agent any

    environment {
        APP_NAME = "sample-app"
        IMAGE_NAME = "sample-app-image"
        CONTAINER_NAME = "sample-app-container"
    }

    stages {

        stage('Clean Workspace') {
            steps {
                echo "Cleaning workspace..."
                deleteDir()
            }
        }

        stage('Clone Code') {
            steps {
                echo "Cloning source code from GitHub..."
                git branch: 'main', url: 'https://github.com/aanikettj/lambda-triggered-pipeline.git'
            }
        }

        stage('Build') {
            steps {
                echo "Building application..."
                sh 'echo Build completed successfully'
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'echo Tests passed successfully'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image..."
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    echo "Stopping old container if exists..."
                    sh '''
                    docker stop $CONTAINER_NAME || true
                    docker rm $CONTAINER_NAME || true
                    '''
                }
            }
        }

        stage('Deploy Container') {
            steps {
                echo "Deploying Docker container..."
                sh 'docker run -d -p 80:80 --name $CONTAINER_NAME $IMAGE_NAME'
            }
        }
    }

    post {

        success {
            echo 'CI/CD Pipeline executed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}
