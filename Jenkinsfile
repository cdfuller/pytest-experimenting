pipeline {
  agent {
    docker { image golang:1.9 }
  }
  stages {
    stage('Test image') {
      steps {
        sh 'go version'
      }
    }
  }
}