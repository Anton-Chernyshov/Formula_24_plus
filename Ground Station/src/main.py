from flask import Flask, render_template, jsonify, send_from_directory
import random
import time

app = Flask(__name__)

# Initialize an empty list to store our "real-time" data points
myData = []

@app.route("/")
def homepage():
    return render_template("index.html"), 200

@app.route("/download/<fileName>")
def download(fileName): 
    print(fileName)
    return send_from_directory("data/", fileName, as_attachment=True), 200

@app.route("/update")
def update():
    # Add new data point with timestamp
    new_data = {"time": time.time() * 1000, "y": random.randint(0, 100)}
    myData.append(new_data)
    
    # Limit the amount of data to keep the chart readable
    if len(myData) > 50:
        myData.pop(0)  # Remove the oldest data point if we have more than 50 points
    
    return jsonify(myData), 200

if __name__ == "__main__":
    app.run("0.0.0.0", "80", debug=True)
