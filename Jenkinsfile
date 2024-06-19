pipeline{
    agent any
    triggers {
        pollSCM('* * * * *') // This will trigger every minute
    }
    stages {
        stage('Install Dependenccies') {
            steps {
                sh '''
                echo " install"
                '''
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
