// pipeline
// {
//     agent any
//
//     stages
//     {
//         stage('Checkout')
//         {
//             steps
//             {
//                 git 'https://github.com/Pprashu-63/NewRepo63.git'
//             }
//         }
//
//         stage('Build')
//          {
//             steps
//             {
//                 mvn 'clean'
//             }
//         }
//
//           stage('SonarQube Analysis')
//           {
//               withSonarQubeEnv()
//               {
//                   sh "./gradlew sonar"
//               }
//            }
//         }
//      }


node {
  stage('SCM') {
    git 'https://github.com/Pprashu-63/NewRepo63.git'
  }
  stage('SonarQube Analysis') {
    withSonarQubeEnv() {
      sh "./gradlew sonar"
    }
  }
}
