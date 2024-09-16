
from flask import Flask,  redirect, render_template

app = Flask(__name__)

voltage: float = 0.0
amperage: float = 0.0
motorTemp: float = 0.0
rpm: int = 0

@app.route("/")
def homepage():

    templateData = {
        "voltage":f"{voltage}",
        "amperage":f"{amperage}",
        "motorTemp":f"{motorTemp}",
        "rpm":f"{rpm}"
        }
    return render_template("main.html", **templateData)


if __name__ == "__main__":
    app.run("0.0.0.0", "80", debug=True)