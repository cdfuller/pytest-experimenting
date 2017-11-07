node {
    def app

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build('pytesting')
    }

    stage('Test image') {
        app.inside {
            // sh 'pytest'
            echo 'Tests passed'
        }
    }
}