import serial

# Open the serial port (update to your correct port, e.g., '/dev/ttyUSB0' or '/dev/ttyAMA0')
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=2)#, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,  xonxoff=True, rtscts=True, dsrdtr=True)


# Print out the settings to confirm
print(f"Serial Port opened: {ser.name}")
print(f"Baudrate: {ser.baudrate}")
buffer = ""
# Receive data in a loop
try:
    while True:
        if ser.in_waiting > 0:

            data = ser.read(ser.in_waiting) .decode('utf-8', errors='ignore') # Read available data
            buffer += data

            while ";" in buffer:
                # Split the buffer at the first semicolon
                message, buffer = buffer.split(";", 1)
                # Process the message (for example, print it)
                print(f"Received: {message}")
                # Here you can add code to handle the message as needed
except KeyboardInterrupt:
    print("Program interrupted by user.")
finally:
    ser.close()  # Close the serial port when done
