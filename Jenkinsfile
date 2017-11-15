#!/usr/bin/env groovy

pipeline {
    agent { dockerfile true }

    environment {
        TEST_ENV = 'Mars'
    }

    stages {
        stage('Test image') {
            steps {
                sh 'pytest --junitxml=results.xml'
            }
        }
    }
    
    post {
        always {
            junit 'results.xml'
        }
    }
}