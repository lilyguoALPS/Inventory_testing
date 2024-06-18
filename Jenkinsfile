pipeline{
    agent{
        node{
            label 'docker-agent-python'
        }
    }
    triggers{
        pollSCM '*  *  *  *  *'
    }
    stages{
        stage('Build'){
            steps{
                echo "Building..."
                sh '''       
                python -m venv venv
                . venv/Scripts/activate
                pip install pytest
                echo "end of Building"
                '''
            }
            }
        stage('Test'){
            steps{
                echo "Testing..."
                sh '''
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
