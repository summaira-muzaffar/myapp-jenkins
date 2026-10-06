pipeline {
  agent any
  stages {
    stage('Install') { steps { sh 'python3 -m venv venv && . venv/bin/activate && pip install -r requirements.txt' } }
    stage('Test')    { steps { sh '. venv/bin/activate && pytest' } }
    stage('Build')   { steps { sh 'docker build -t myapp:${BUILD_NUMBER} .' } }
    stage('Deploy')  { steps { sh 'docker rm -f myapp || true; docker run -d --name myapp -p 5000:5000 myapp:${BUILD_NUMBER}' } }
  }
}