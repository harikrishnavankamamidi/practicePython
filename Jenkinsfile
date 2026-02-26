pipeline{
    agent any
    
    stages{

        stage('Checkout'){
            steps{
                git branch: 'main', url:'https://github.com/harikrishnavankamamidi/practicePython'
            }
        }

        stage("Install dependencies"){
            steps{
                sh 'python -m pip install --upgrade'
                sh 'pip install -r requirements.txt'
            }
        stage('Run Tests'){
            steps{
                sh 'pytest'
            }
        }

        }
    }
}