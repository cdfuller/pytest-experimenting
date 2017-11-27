pipeline {
  agent {
    dockerfile true
  }
  stages {
    stage('Test image') {
      parallel {
        stage('Unit') {
          steps {
            sh 'pytest --junitxml=unit.xml unit'
          }
        }
        stage('Integration') {
          steps {
            sh 'pytest --junitxml=integration.xml integration'
          }
        }
        stage('INFO') {
          steps {
            sh 'python --version'
            sh 'pwd'
            sh 'ls -al'
          }
        }
      }
    }
  }
  environment {
    TEST_ENV = 'Mars'
  }
  post {
    always {
      junit 'unit.xml'
      junit 'integration.xml'
    }
  }
}