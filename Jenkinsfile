pipeline {
    agent any

    environment {
        DOCKER_REPO_URL = "https://hub.docker.com/r/prashanth63/newrepo"
        DOCKER_USERNAME = credentials('dockerlogin')
        DOCKER_PASSWORD = credentials('dockerlogin')
        TAG_NAME = "latest" // Replace with your desired tag name
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("$DOCKER_REPO_URL:$TAG_NAME", ".")

                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', DOCKER_USERNAME, DOCKER_PASSWORD) {
                        docker.image("$DOCKER_REPO_URL:$TAG_NAME").push()
                    }
                }
            }
        }
        stage('Deploying App to Kubernetes') {
             steps {
                 script {
                     kubernetesDeploy(configs: "deploymentservice.yml", kubeconfigId: "KUBECONFIG")
                }
           }
         }
    }
}
