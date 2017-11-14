#!/usr/bin/env groovy

pipeline {
    agent { dockerfile true }

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