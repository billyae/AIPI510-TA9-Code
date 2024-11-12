### Decision Tree Classification Demo      

A decision tree classification demo using streamlit as frontend and Flask as backend.   
It can be deployed to Google Kubernetes Engine with dockerfile. Before you deploy the frontend, you should change the API_URL in the ML_demo_frontend.py.
    
Author: TeamName ( Zihao Yang, Tony Wang)       

### Usage       

#### Backend:       
cd backend    
docker build -t us-central1-docker.pkg.dev/teamname-ta8/ml-docker-repo/backend:v1 .       
docker run --rm -p 5000:5000 us-central1-docker.pkg.dev/teamname-ta8/ml-docker-repo/backend:v1      

#### Frontend:    
cd frontend    
docker build -t us-central1-docker.pkg.dev/teamname-ta8/ml-docker-repo/frontend:v1 .     
docker run --rm -p 8501:8501 us-central1-docker.pkg.dev/teamname-ta8/ml-docker-repo/frontend:v1     


