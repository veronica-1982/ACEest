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

**Project Structure**
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



**Pipeline Triggered on:**
- Push to main
- PR merge to main
