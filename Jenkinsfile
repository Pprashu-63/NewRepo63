pipeline {
  agent any
  
  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/Pprashu-63/NewRepo63.git'
      }
    }
    
    stage('Build') {
      steps {
        sh 'mvn clean ' 
      }
    }
    
    stage('Deploy') {
      steps {
        
        sh 'kubectl apply -f Deployment.yaml'
      }
    }
  }
}
