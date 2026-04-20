# Flask To-Do App Project Setup

I have initialized a complete boilerplate for your Flask To-Do application. Below is a summary of the project structure and how to get started.

## Project Structure

```text
flask-todo-app/
├── static/
│   ├── css/
│   │   └── style.css      # Custom styling
│   └── js/
│       └── main.js       # Client-side logic
├── templates/
│   ├── base.html         # Base template with Bootstrap 5
│   └── index.html        # Home page template
├── app.py                # Main application file (Routing & DB Logic)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Key Files Summary

### [app.py](file:///C:/Users/rutuj/.gemini/antigravity/scratch/flask-todo-app/app.py)
This is the heart of your application. It includes:
- Flask app initialization.
- **SQLAlchemy (SQLite)** setup for the database.
- Routes for listing (`/`), adding (`/add`), updating (`/update`), and deleting (`/delete`) tasks.
- Background database creation (`db.create_all()`).

### [templates/base.html](file:///C:/Users/rutuj/.gemini/antigravity/scratch/flask-todo-app/templates/base.html)
A shared layout file that uses the **Bootstrap 5 CDN** for modern, responsive design. It provides a navigation bar and consistent styling across all pages.

### [templates/index.html](file:///C:/Users/rutuj/.gemini/antigravity/scratch/flask-todo-app/templates/index.html)
The home page template that displays the task list and an "Add Task" form.

---

## Getting Started

1. **Navigate to the project folder:**
   ```powershell
   cd flask-todo-app
   ```

2. **Set up a Virtual Environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Launch the App:**
   ```powershell
   python app.py
   ```
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
