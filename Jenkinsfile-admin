pipeline {
    agent any
    environment {
        GITHUB_CREDENTIALS = 'github-credentials'    // Your GitHub credentials in Jenkins
        EC2_CREDENTIALS = 'server-username-password' // Jenkins credentials ID for EC2 username/password
        REPO_URL = 'https://github.com/richest/code-store-admin.git'  // GitHub repo URL
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "Checking out admin repository"
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: "*/master"]],
                        userRemoteConfigs: [[url: REPO_URL, credentialsId: GITHUB_CREDENTIALS]]
                    ])
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    echo "Building admin"
                    // Replace with your admin build commands (e.g., npm install, npm run build)
                    sh 'npm install'
                    sh 'npm run build'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo "Deploying admin to EC2"
                    // Extract the username and password from Jenkins credentials
                    withCredentials([usernamePassword(credentialsId: EC2_CREDENTIALS, passwordVariable: 'SSH_PASSWORD', usernameVariable: 'SSH_USER')]) {
                        // Use sshpass with username and password for the ssh connection
                        sh """
                        sshpass -p \${SSH_PASSWORD} ssh -o StrictHostKeyChecking=no \${SSH_USER}@24.144.64.148 '
                            cd /var/www/html/codestoretest/admin && git pull origin main && npm install && npm run build
                            sudo systemctl restart admin-service
                        '
                        """
                    }
                }
            }
        }

        stage('Post-Deployment Check') {
            steps {
                script {
                    echo "Performing post-deployment health check"
                    // Replace with the admin health check URL
                    sh 'curl -f http://24.144.64.148/admin/healthcheck || exit 1'
                }
            }
        }
    }
    post {
        failure {
            echo "Deployment failed for admin"
            // Optional: Trigger a Jira issue if deployment fails
        }
        success {
            echo "Admin deployment completed successfully"
        }
    }
}
