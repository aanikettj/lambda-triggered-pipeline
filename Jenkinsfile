pipeline {
    agent any

    environment {
        IMAGE_NAME = "s3-lambda-app"
        CONTAINER_NAME = "s3-lambda-container"
    }

    stages {

        stage('Clean Workspace') {
            steps {
                echo "Cleaning workspace"
                deleteDir()
            }
        }

        stage('Clone Repository') {
            steps {
                echo "Cloning GitHub repo"
                git branch: 'main', url: 'https://github.com/YOUR_USERNAME/s3-lambda-jenkins-cicd.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image"
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Deploy Container') {
            steps {
                echo "Deploying container"
                sh 'docker run -d -p 80:80 --name $CONTAINER_NAME $IMAGE_NAME'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

