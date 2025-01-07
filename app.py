from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Настройка базы данных SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Модель для задач
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Создание базы данных (выполняется один раз)
with app.app_context():
    db.create_all()
@app.route("/")
def index():
    # Получение всех задач из базы данных
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    # Добавление новой задачи
    task_name = request.form.get("task")
    if task_name:
        new_task = Task(name=task_name)
        db.session.add(new_task)
        db.session.commit()
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    # Удаление задачи
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect("/")

@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    # Переключение состояния задачи (выполнено/не выполнено)
    task = Task.query.get(task_id)
    if task:
        task.done = not task.done
        db.session.commit()
    return redirect("/")
    from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
