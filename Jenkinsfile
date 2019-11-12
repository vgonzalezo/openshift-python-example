pipeline{
  agent any
  
  stages{
    stage ('Checkout codigo fuente'){
      steps{
        checkout scm
      }
    }

    stage ('Desplegar contenedor') {
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
  }
}