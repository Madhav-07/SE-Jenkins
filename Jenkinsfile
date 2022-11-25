pipeline {
agent any
    stages {
        stage('Clone Git') {
            steps {
                git "https://github.com/Madhav-07/SE-Jenkins.git"
            }
        }
        stage('Show Files') {
            steps {
                sh "ls"
            }
        }
        stage('Run Code') {
            steps {
                sh "/usr/bin/python3 program.py"
            }
        }
        stage('Test Code') {
            steps {
                sh "/usr/bin/python3 test.py"
            }
        }
    }
}
