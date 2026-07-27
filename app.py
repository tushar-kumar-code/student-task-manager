from flask import Flask, render_template, request, redirect, url_for, session
import database

app = Flask(__name__)

# Secret Key (Required for Session)
app.secret_key = "student-task-manager-secret"

# Create Database
database.create_database()


@app.route("/")
def home():

    # Agar user already login hai to seedha dashboard bhej do
    if "user" in session:
        return redirect(url_for("dashboard"))

    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "1234":

        # Session Start
        session["user"] = username

        return redirect(url_for("dashboard"))

    else:

        return """
        <h1>❌ Invalid Username or Password</h1>
        <br>
        <a href="/">Try Again</a>
        """


@app.route("/dashboard")
def dashboard():

    # Login check
    if "user" not in session:
        return redirect(url_for("home"))

    tasks = database.get_tasks()

    return render_template(
        "dashboard.html",
        tasks=tasks,
        username=session["user"]
    )


@app.route("/add-task", methods=["POST"])
def add_task():

    if "user" not in session:
        return redirect(url_for("home"))

    task = request.form["task"]

    if task.strip() != "":
        database.add_task(task)

    return redirect(url_for("dashboard"))


@app.route("/delete-task/<int:task_id>")
def delete_task(task_id):

    if "user" not in session:
        return redirect(url_for("home"))

    database.delete_task(task_id)

    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)