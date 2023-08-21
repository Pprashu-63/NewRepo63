pipeline
 {
    agent any {
      stage('SCM') {
        git 'https://github.com/Pprashu-63/NewRepo63.git'
      }
      stage('SonarQube Analysis')
       {
        withSonarQubeEnv()
        {
          sh "./gradlew sonar"
        }
      }
    }
    }

