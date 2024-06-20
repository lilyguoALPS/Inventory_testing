pipeline {
    agent any
    
    environment {
        VENV_DIR = 'venv'
    }
    
    stages {
        stage('Setup Virtual Environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python3 -m venv ${VENV_DIR}
                        '''
                    } else {
                        bat '''
                            python -m venv ${VENV_DIR}
                        '''
                    }
                }
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            source ${VENV_DIR}/bin/activate
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            ${VENV_DIR}\\Scripts\\activate
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            source ${VENV_DIR}/bin/activate
                            cd testCases
                            pytest test_add_new_material.py
                        '''
                    } else {
                        bat '''
                            ${VENV_DIR}\\Scripts\\activate
                            cd testCases
                            pytest test_add_new_material.py
                        '''
                    }
                }
            }
        }
        
        stage('Clean Up') {
            steps {
                echo "Cleaning up..."
                script {
                    if (isUnix()) {
                        sh 'deactivate'
                    } else {
                        bat '${VENV_DIR}\\Scripts\\deactivate.bat'
                    }
                }
            }
        }
    }
}
