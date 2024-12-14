from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)

# Function to retrieve tasks
def get_tasks():
    return tasks

@app.route('/')
def index():
    return render_template('index.html', tasks=get_tasks())

@app.route('/add-task', methods=['POST'])
def add_task_route():
    task_description = request.form.get('task')
    if task_description:
        add_task(task_description)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
