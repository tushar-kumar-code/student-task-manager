from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "1234":

        return """
        <h1>✅ Login Successful</h1>

        <h2>Welcome Admin</h2>
        """

    else:

        return """
        <h1>❌ Invalid Username or Password</h1>

        <a href="/">Try Again</a>
        """


if __name__ == "__main__":
    app.run(debug=True)