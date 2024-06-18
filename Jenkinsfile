pipeline {
    agent {
        node {
            label 'docker-agent-python'
        }
    }
    triggers {
        pollSCM('* * * * *') // This will trigger every minute
    }
    stages {
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
     
                pip install --user pytest
                
                pip install --user selenium
                
                pip install --user webdriver_manager
                pip install --user pymysql
                
                
                export PATH=$PATH:$HOME/.local/bin
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
