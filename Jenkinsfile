pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/2025sl93002-lang/labsheet1-2025sl93002.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo Build Started'
                sh 'python3 --version'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 calculator.py'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo Deployment Stage'
            }
        }

    }
}
