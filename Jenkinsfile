pipeline {
    agent any

    stages {
        stage('Prepare Environment') {
            steps {
                bat 'set'
                git(url:'https://github.com/lilyguoALPS/Inventory_testing',branch:'main')
                }
        }
        stage('Activate Virtual Environment') {
            steps {
                // Execute Windows batch commands to activate the virtual environment and run tests
                bat '''
                    cd %WORKSPACE%
                    call venv\\Scripts\\activate
                '''
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                    cd %WORKSPACE%\\testCases
                    pytest test_add_new_material.py
                '''
            }
        }
    }
    post {
        always {
            // Archive test results
            archiveArtifacts artifacts: 'testCases/**/*.xml', allowEmptyArchive: true
            // Publish test results
            junit 'testCases/**/*.xml'
        }
    }
}
