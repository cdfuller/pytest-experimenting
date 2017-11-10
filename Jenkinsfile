#!/usr/bin/env groovy

pipeline {
    agent { dockerfile true }

    stage('Clone repository') {
        steps {
            checkout scm
        }
    }

    // stage('Build image') {
    //     steps {
    //         app = docker.build('pytesting')
    //     }
    // }

    stage('Test image') {
        steps {
            sh 'pytest --junitxml=results.xml'
        }
    }
    
    post {
        always {
            junit 'results.xml'
        }
    }
}