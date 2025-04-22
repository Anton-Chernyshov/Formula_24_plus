import serial

# Open the serial port (update to your correct port, e.g., '/dev/ttyUSB0' or '/dev/ttyAMA0')
ser = serial.Serial('COM7', baudrate=9600, timeout=2)#, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,  xonxoff=True, rtscts=True, dsrdtr=True)


# Print out the settings to confirm
print(f"Serial Port opened: {ser.name}")
print(f"Baudrate: {ser.baudrate}")

# Receive data in a loop
try:
    while True:
        if ser.in_waiting > 0:
            data = ser.read(ser.in_waiting)  # Read available data
            print(data.decode('utf-8', errors='ignore'))  # Print the received data
except KeyboardInterrupt:
    print("Program interrupted by user.")
finally:
    ser.close()  # Close the serial port when done
