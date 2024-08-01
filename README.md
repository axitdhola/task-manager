# FastAPI Task Manager
This project allows users to log in, create tasks, and perform CRUD (Create, Read, Update, Delete) operations on tasks. When a task is created, an email is sent asynchronously using Celery.

## Prerequisites

This project requires that you have the following dependencies

- Python >= 3.10
- PostgreSQL
- Redis

## Run Locally
Clone the project

```bash
  git clone https://github.com/axitdhola/task-manager.git
```

Enter your project
```bash
  cd task-manager
```

Activate the virtualenv with
```bash
  source env/bin/activate
```

Install all project dependencies with
```bash
  pip install -r requirements.txt
```
All environment variable are located in this [file](https://github.com/axitdhola/task-manager/blob/main/.env.example), so it is important you add them in a .env file before you run the server. \
Start FastAPI Server
```bash
  uvicorn app.main:app --reload
```

Open another terminal within your virtualenv and run a celery worker
```bash
  celery -A app.worker.celery_app worker
```