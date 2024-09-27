pipeline {
    agent any
    stages {
        stage ("GIT Checkout") {
            steps {
                git branch: 'develop', url: 'https://github.com/TresAgile/sample-python-app.git'
            }
        }
        stage ("SonarQube Analysis") {
           steps {
               script {
                   def scannerHome = tool 'sonar-scanner';
                   withSonarQubeEnv("Sonarqube") {
                       sh "${scannerHome}/sonar-scanner"
                   }
               }
           }
        }
        stage("Quality Gate") {
            steps {
                timeout(time: 1, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        stage ("Print") {
            steps {
                echo "Quality gate got success"
            }
        }
    }
    post {
        success {
            emailext body: 'Hey your $JOB_NAME got $BUILD_STATUS', recipientProviders: [requestor()], subject: '$JOB_NAME - $BUILD_NUMBER - $BUILD_STATUS', to: 'test@gmail.com'
        }
        failure {
            emailext body: 'Hey your $JOB_NAME got $BUILD_STATUS', recipientProviders: [requestor()], subject: '$JOB_NAME - $BUILD_NUMBER - $BUILD_STATUS', to: 'test@gmail.com'
        }
    }    
}
