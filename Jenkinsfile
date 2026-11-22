pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my-first-app:${BUILD_NUMBER} .'
            }
        }
        stage('Run Container') {
            steps {
                sh 'docker run --rm my-first-app:${BUILD_NUMBER}'
            }
        }
    }
}
