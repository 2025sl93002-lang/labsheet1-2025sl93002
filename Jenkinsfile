pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/<username>/<repo-name>.git'
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
