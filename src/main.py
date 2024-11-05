
from flask import Flask,  redirect, render_template, jsonify
import random
#import serial
app = Flask(__name__)

voltage: float = 0.0
amperage: float = 0.0
motorTemp: float = 0.0
rpm: int = 0

#serialConnection = serial.Serial("/dev/ttyUSB0", 9600)


@app.route("/") 
def homepage():

    templateData = {
        "voltage":f"{voltage}",
        "amperage":f"{amperage}",
        "motorTemp":f"{motorTemp}",
        "rpm":f"{rpm}"
        }
    return render_template("main.html", **templateData), 202

def getData():
    try:
        #line = serialConnection.readline().decode("utf-8").strip()
        line = f"{random.randint(0, 999)},{random.randint(0, 999)},{random.randint(0, 999)},{random.randint(0, 999)}"
        values = line.split(",")
        voltage = values[0]
        amperage = values[1]
        motorTemp = values[2]
        rpm = values[3]
    except Exception as e:
        print(str(e))
    return [voltage, amperage, motorTemp, rpm]


@app.route("/update")
def update():
    try:
        data = getData()
        #return data as jsons
        return jsonify(voltage = str(data[0]), amperage = data[1], motorTemp = data[2], rpm = data[3] ), 200
    except Exception as e:
        return jsonify(error=str(e), voltage = "null", amperage = "null", motorTemp = "null", rpm = "null"), 500
if __name__ == "__main__":
    app.run("0.0.0.0", "80", debug=True)