# 350FinalProject

A Flask-based web application for task management, deployed on AWS EC2 with Docker and CI/CD pipelines.

## Setup
1. Create virtual environment: `python3 -m venv venv`
2. Activate: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run tests: `pytest tests/`
5. Build Docker image: `docker build -t 350finalproject .`
6. Run locally: `docker run -p 5000:5000 350finalproject`
7. Deploy to EC2: `terraform -chdir=infrastructure apply`

## CI/CD
- CI: GitHub Actions (`build.yml`) runs tests and builds the Docker image.
- CD: GitHub Actions (`release.yml`) deploys to EC2 and pushes to Docker Hub. 