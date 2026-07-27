from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

database.create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "1234":
        return redirect(url_for("dashboard"))

    else:
        return """
        <h1>❌ Invalid Username or Password</h1>

        <a href="/">Try Again</a>
        """


@app.route("/dashboard")
def dashboard():

    tasks = database.get_tasks()

    return render_template("dashboard.html", tasks=tasks)


@app.route("/add-task", methods=["POST"])
def add_task():

    task = request.form["task"]

    database.add_task(task)

    return redirect(url_for("dashboard"))


@app.route("/delete-task/<int:task_id>")
def delete_task(task_id):

    database.delete_task(task_id)

    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(debug=True)