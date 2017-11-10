#!/usr/bin/env groovy

pipeline {
    agent { dockerfile true }

    stage('Clone repository') {
        steps {
            checkout scm
        }
    }

    stage('Build image') {
        steps {
            app = docker.build('pytesting')
        }
    }

    stage('Test image') {
        steps {
            app.inside {
                // echo 'Tests passed'
                // sh 'pytest'
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