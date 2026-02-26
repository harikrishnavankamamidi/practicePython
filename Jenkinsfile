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
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests'){
            steps{
                bat 'pytest'
            }
        }

        }
    }