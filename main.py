
from flask import Flask, make_response, redirect

app = Flask(__name__)



if __name__ == "__main__":
    app.run("0.0.0.0", "80" debug=True)