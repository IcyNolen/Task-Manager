# 📝 FastAPI Task Manager

A full-stack application built using **Python FastAPI**. It allows users to securely sign in and manage their personal tasks — including creating, retrieving, and marking tasks as complete.

## 🚀 Technologies Used

- **FastAPI** – Core backend framework for API routing
- **PostgreSQL** – Database for storing user credentials and to-do task data
- **Alembic** – Handles database schema migrations
- **JWT & OAuth2** – Authentication and authorization
- **SQLAlchemy** – ORM to define and interact with DB models
- **PyTest** – For writing unit and integration tests
- **Bootstrap + JavaScript** – For building the frontend UI

## ⚙️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

2. **Set Up a PostgreSQL Database**

Update the `SQLALCHEMY_DATABASE_URL` in `TodoApp/database.py` with your connection string:

```bash
postgresql://:@localhost/
```

3. **Create and Activate a Virtual Environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

4. **Install Dependencies**

Install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

5. **Start the Server**

Start your FastAPI development server using Uvicorn:

```bash
uvicorn TodoAPP.main:app --reload
```

6. **Visit the Swagger API Docs**

Once the server is running, you can explore and test all the API endpoints using the built-in Swagger UI.

Open your browser and navigate to:

```
http://127.0.0.1:8000/auth/login-page
```
OR

```
http://127.0.0.1:8000/docs
```

## ✅ Features

- 🔐 User registration & login using JWT + OAuth2
- 🔄 Token-based authentication with access token expiry
- 📝 Create, retrieve, update, and delete tasks (CRUD)
- 🗂️ User-specific task isolation (no shared tasks)
- 🧬 Alembic-based database schema migrations
- 📚 Interactive API documentation via Swagger and ReDoc
- 🧪 PyTest test suite for endpoints and internal logic
- 💡 Modular FastAPI structure (routers, services, models)
- 🎨 Simple responsive frontend using Bootstrap + custom JavaScript
