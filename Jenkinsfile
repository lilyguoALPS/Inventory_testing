pipeline{
    agent{
        any
    }
    triggers{
        pollSCM '*  *  *  *  *'
    }
    stages{
        stage('Build'){
            steps{
                echo "Building..."
                sh '''                
                echo "end of Building"
                '''
            }
            }
        stage('Test'){
            steps{
                echo "Testing..."
                sh '''
                . venv/Scripts/activate
                cd testCases
                pytest test_add_new_material.py
                '''
            }
        }
        stage('Deliver'){
            steps{
                echo 'Deliver...'
                sh '''
                echo "end of Delivery
                '''
            }
            
        }
    }
}