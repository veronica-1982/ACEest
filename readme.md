**🏋️ ACEest Fitness App**

**A lightweight Flask-based fitness management application that allows users to:**
- Add and manage client fitness data
- Generate workout and diet plans
- Calculate calories based on fitness programs
- Track BMI and health metrics

Built with Flask, SQLite, Docker, and Pytest, and integrated with CI/CD pipelines.
<img width="1781" height="922" alt="image" src="https://github.com/user-attachments/assets/9470babe-4365-4391-80f2-df7688aff225" />


**Features**
- Add & update client details
- Program-based workout & diet recommendations
- Automatic calorie calculation
- BMI calculation API
- SQLite database (local + Docker persistence)
- REST APIs for frontend interaction
- Pytest-based testing
- Dockerized for easy deployment
- GitHub Actions CI pipeline (Lint + Test + Build)

## Project Structure

ACEest/
│
├── app.py                 # Flask entry point  
├── routes.py              # API routes  
├── models.py              # Database models  
├── database.py            # DB initialization  
├── utils.py               # Business logic (programs, BMI)  
│
├── templates/             # HTML UI  
├── static/                # CSS / JS  
├── instance/              # SQLite DB (auto-created)  
│
├── tests/                 # Pytest test cases  
│   ├── conftest.py  
│   └── test_routes.py  
│
├── Dockerfile             # Container config  
├── requirements.txt       # Dependencies  
└── .github/workflows/     # CI/CD pipeline  

**Setup & Run (Local)**

1. Clone the repository
git clone <repo-url>
cd ACEest

3. Install dependencies
pip install -r requirements.txt

5. Run the application
python app.py

 **Open: http://localhost:5000**

**Run with Docker**
- Build image
- docker build -t fitness-app .
- Run container
- docker run -p 5000:5000 -v $(pwd)/instance:/app/instance fitness-app

 Access: http://localhost:5000


 **Jenkins Build:**
 1. Build Custom Jenkins image using docker file https://github.com/veronica-1982/ACEest/blob/main/Jenkins.Dockerfile
 2. Run the Jenkins container docker run -d `  -p 8080:8080 -p 50000:50000 `    --network bridge --name jenkins3 `  jenkinspython
    <img width="1600" height="948" alt="image" src="https://github.com/user-attachments/assets/7660667e-ae5b-491c-8dc6-af97499d7053" />

 3. Create a Pipeline App, Here is the jenkins file content https://github.com/veronica-1982/ACEest/blob/main/Jenkinsfile
 <img width="1600" height="604" alt="image" src="https://github.com/user-attachments/assets/8d2e0573-fd82-4b58-9306-9a730d53985f" />
 4. Trigger the build
 <img width="1312" height="716" alt="image" src="https://github.com/user-attachments/assets/56313564-499f-4525-9af8-5123f2aa5b1b" />
<img width="1600" height="531" alt="image" src="https://github.com/user-attachments/assets/11fcf51d-b448-450b-ac34-723b4353b2f5" />
<img width="1600" height="921" alt="image" src="https://github.com/user-attachments/assets/211084ba-7d3c-4bcb-93a8-60b5f74ec5a0" />
<img width="1600" height="880" alt="image" src="https://github.com/user-attachments/assets/10817158-55e7-4f5b-ad16-3f5444cda7a7" />
<img width="1600" height="880" alt="image" src="https://github.com/user-attachments/assets/ada6cec0-ee08-4027-81f7-5662b82c7879" />
<img width="1600" height="888" alt="image" src="https://github.com/user-attachments/assets/cfe8c7ca-2e3e-4b72-998d-5557d72dc951" />
<img width="1600" height="929" alt="image" src="https://github.com/user-attachments/assets/07cee462-c1c8-49da-8690-7eb127a5b811" />
<img width="1600" height="882" alt="image" src="https://github.com/user-attachments/assets/f6621908-3a58-42ee-863c-c7e0befa04d7" />
5. Here is the build log https://github.com/veronica-1982/ACEest/blob/main/Jenkins_Build.logs



**GitHub Action Pipeline Triggered on:** https://github.com/veronica-1982/ACEest/actions
- Push to main
- PR merge to main

**Job 1: Lint**
- Runs flake8 for code quality checks
- Detects syntax errors and style issues
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --max-line-length=120 --exit-zero --statistics

**Job 2: Build & Test**
- Runs only if lint passes.

Steps:
- Build Docker image
- Run unit tests using pytest
- Start container
- Perform health check using curl
docker build -t fitness-app .
docker run --rm fitness-app pytest -v
docker run -d -p 5000:5000 --name test_container fitness-app
curl http://localhost:5000
<img width="1702" height="961" alt="image" src="https://github.com/user-attachments/assets/06a59434-18c0-4c07-90de-9bb1e34c9c67" />
<img width="1570" height="918" alt="image" src="https://github.com/user-attachments/assets/07149dd6-6581-4c1f-b339-8f2e6571be93" />
<img width="1561" height="946" alt="image" src="https://github.com/user-attachments/assets/91c00030-b2a3-4e0f-9171-2884d7aab35f" />



