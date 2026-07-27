from flask import Flask, render_template, request, redirect, url_for, session
import database

app = Flask(__name__)

app.secret_key = "student-task-manager-secret"

database.create_database()


@app.route("/")
def home():

    if "user" in session:
        return redirect(url_for("dashboard"))

    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "1234":

        session["user"] = username
        return redirect(url_for("dashboard"))

    return """
    <h1>❌ Invalid Username or Password</h1>
    <br>
    <a href="/">Try Again</a>
    """


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("home"))

    tasks = database.get_tasks()

    total, completed, pending = database.get_statistics()

    return render_template(
        "dashboard.html",
        username=session["user"],
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending
    )


@app.route("/add-task", methods=["POST"])
def add_task():

    if "user" not in session:
        return redirect(url_for("home"))

    task = request.form["task"]
    priority = request.form["priority"]
    due_date = request.form["due_date"]

    if task.strip():

        database.add_task(
            task,
            priority,
            due_date
        )

    return redirect(url_for("dashboard"))


@app.route("/delete-task/<int:task_id>")
def delete_task(task_id):

    if "user" not in session:
        return redirect(url_for("home"))

    database.delete_task(task_id)

    return redirect(url_for("dashboard"))


@app.route("/edit-task/<int:task_id>")
def edit_task(task_id):

    if "user" not in session:
        return redirect(url_for("home"))

    task = database.get_task(task_id)

    return render_template(
        "edit.html",
        task=task
    )


@app.route("/update-task/<int:task_id>", methods=["POST"])
def update_task(task_id):

    if "user" not in session:
        return redirect(url_for("home"))

    task = request.form["task"]
    priority = request.form["priority"]
    due_date = request.form["due_date"]

    database.update_task(
        task_id,
        task,
        priority,
        due_date
    )

    return redirect(url_for("dashboard"))


@app.route("/toggle-status/<int:task_id>")
def toggle_status(task_id):

    if "user" not in session:
        return redirect(url_for("home"))

    database.toggle_status(task_id)

    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)