pipeline {
  agent {
    dockerfile true
  }
  stages {
    stage('Test image') {
      parallel {
        stage('Test image') {
          steps {
            sh 'pytest --junitxml=results.xml'
          }
        }
        stage('') {
          steps {
            sh 'pytest --junitxml=results.xml integration'
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
      junit 'results.xml'
      
    }
    
  }
}