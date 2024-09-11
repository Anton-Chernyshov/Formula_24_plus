
from flask import Flask,  redirect, render_template

app = Flask(__name__)
@app.route("/")
def homepage():
    return render_template("main.html")


if __name__ == "__main__":
    app.run("0.0.0.0", "80", debug=True)