pipeline{
  agent { 
    node {
      label 'maven'
    } 
  }
  stages{
    stage ('Checkout codigo fuente'){
      steps{
        checkout scm
      }
    }

    stage ('Registrar Docker') {
      steps{
        script {
          openshift.withCluster() {
            openshift.withProject('poc') {
              openshift.selector("bc", "python-example").startBuild("--from-dir=./", "--wait=true", "--follow", "--loglevel=8")
            }
          }
        }
      }
    }

    stage('Desplegar') {
      steps {
        script {
          openshift.withCluster() {
            openshift.withProject('poc') {
              openshift.selector("dc", "python-example").rollout().latest();
            }
          }
        }
      }
    } 

  }
}