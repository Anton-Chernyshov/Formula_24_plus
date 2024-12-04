import serial


arduinoDataIn = serial.Serial("/dev/ttyACM0",9600)

def getData(serialPath: serial.Serial) -> list[str]:
    data = serialPath.readline().decode("utf-8").split(",")
    return data

 
arduinoDataIn.close()














