import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

app = Flask(__name__)

# --- CONFIGURATION ---
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'dev-secret-key-12345'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Handle Vercel's read-only filesystem
if os.environ.get('VERCEL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:////tmp/app.db'
else:
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

db = SQLAlchemy(app)

# --- MODELS ---
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, description=None, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

# Initialize tables
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"Initial DB creation failed: {e}")

# --- ROUTES ---
@app.route('/')
def index():
    filter_type = request.args.get('filter', 'all')
    
    # Final safety check for Serverless environments: try the query, rebuild if table missing
    try:
        query = Task.query.order_by(Task.created_at.desc())
    except Exception:
        db.create_all()
        query = Task.query.order_by(Task.created_at.desc())

    if filter_type == 'completed':
        tasks = query.filter_by(completed=True).all()
    elif filter_type == 'pending':
        tasks = query.filter_by(completed=False).all()
    else:
        tasks = query.all()
        
    return render_template('index.html', tasks=tasks, current_filter=filter_type)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    
    if not title:
        flash('Title is required!', 'danger')
        return redirect(url_for('index'))
        
    new_task = Task(title=title, description=description)
    db.session.add(new_task)
    db.session.commit()
    flash('Task added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.completed = not task.completed
    db.session.commit()
    status = "completed" if task.completed else "pending"
    flash(f'Task marked as {status}!', 'info')
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        db.session.commit()
        flash('Task updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted!', 'warning')
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
