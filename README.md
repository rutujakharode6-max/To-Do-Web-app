# 🚀 TaskFlow | Smart To-Do Application

A premium, responsive Flask application for managing your daily tasks with ease.

[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen)](https://your-app-link.render.com)

## ✨ Features
- **Modern UI**: Built with Bootstrap 5, Inter font, and custom animations.
- **Full CRUD**: Create, Read, Update (Task & Title/Description), and Delete.
- **Live Filtering**: Sort tasks by All, Pending, or Completed.
- **Mobile Optimized**: Includes a Floating Action Button (FAB) for mobile productivity.
- **Persistent Storage**: Powered by SQLite & SQLAlchemy.
- **Migrations**: Database versioning via Flask-Migrate.

## 🛠️ Tech Stack
- **Backend**: Flask
- **Database**: SQLite / SQLAlchemy
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Deployment**: Render / Gunicorn

---

## 💻 Local Setup

1. **Clone & Navigate:**
   ```bash
   cd flask-todo-app
   ```
2. **Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: .\venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Initialize Database:**
   ```bash
   flask db init
   flask db migrate -m "Initial setup"
   flask db upgrade
   ```
5. **Launch:**
   ```bash
   python app.py
   ```

---

## 🌐 Deployment Instructions (Render)

1. **Create a GitHub Repository**: Push your code to a new GitHub repo.
2. **Account Setup**: Log in to [Render](https://render.com).
3. **New Web Service**:
   - Select **New +** > **Web Service**.
   - Connect your GitHub repository.
4. **Configure Service**:
   - **Name**: `taskflow-todo`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && flask db upgrade`
   - **Start Command**: `gunicorn app:app`
5. **Environment Variables**:
   Under the "Environment" tab, add:
   - `SECRET_KEY`: `your-random-secret-key`
   - `PYTHON_VERSION`: `3.11.5`
   - `DATABASE_URL`: `sqlite:///app.db` (For production, consider switching to Render Postgres)

## 🐍 Deployment Instructions (PythonAnywhere)

1. **Upload Files**: Zip your project and upload it via the "Files" tab.
2. **Virtualenv**: Use the terminal to create a venv and `pip install -r requirements.txt`.
3. **Web Tab**:
   - Create a new web app.
   - Set the `WSGI configuration file` to point to your `app.py`.
   - Set the path to your Virtualenv.
4. **Database**: Run `flask db upgrade` in the console.

---

## 📄 License
MIT License. Feel free to use this for your own projects!
