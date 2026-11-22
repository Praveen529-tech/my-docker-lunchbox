pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-first-app:${BUILD_NUMBER} .'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'docker run --rm my-first-app:${BUILD_NUMBER} pytest -v'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker run --rm my-first-app:${BUILD_NUMBER}'
            }
        }
    }
    post {
        always {
            sh 'docker rmi my-first-app:${BUILD_NUMBER} || true'
        }
    }
}
