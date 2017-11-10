#!/usr/bin/env groovy

pipeline {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build('pytesting')
    }

    stage('Test image') {
        app.inside {
            // echo 'Tests passed'
            // sh 'pytest'
            sh 'pytest --junitxml=results.xml'
        }
    }
    
    post {
        always {
            junit 'results.xml'
        }
    }
}