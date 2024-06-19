pipeline{
    agent{
        node{
            label "docker-agent-python"
        }
        }
    triggers {
        pollSCM('* * * * *') // This will trigger every minute
    }
    stages {
        stage('Install Dependenccies') {
            agentP
            {
                docker{
                    image 'pytho:3-alpine'
                }
            }
            steps {
                sh '''
                pip install -r requirements.tx
                sh '''
            }
        }
        stage('Build') {
            steps {
                echo "Building..."
                sh '''       
                echo "end of Building"
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing..."
                sh '''

                cd testCases
                pytest test_add_new_material.py
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver...'
                sh '''
                echo "end of Delivery"
                '''
            }
        }
    }
}
