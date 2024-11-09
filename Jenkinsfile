pipeline {
    agent any

    // triggers {
    //     pollSCM('* * * * *')  // Polls the repository every minute
    // }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // Fetch current date and timestamp
                    def timestamp = new Date().format("yyyyMMdd_HHmmss")

                    // Use withCredentials to bind the token
                    withCredentials([string(credentialsId: 'github_token', variable: 'GITHUB_TOKEN')]) {
                        // Clone the repository using HTTPS and the personal access token
                        sh "git clone https://${GITHUB_TOKEN}@github.com/HimanshuGupta08/test-repo.git repo_${timestamp}"
                    }
                }
            }
        }
    }
}