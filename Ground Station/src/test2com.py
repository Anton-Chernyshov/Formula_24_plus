import serial
import time

# Open serial port
ser = serial.Serial('COM7', baudrate=9600, timeout=2)

# Enter configuration mode
ser.write(b'+++\r')
time.sleep(1)  # Wait for response

# Send the '?' command to get current settings
ser.write(b'?\r')
time.sleep(1)  # Wait for response
data = ser.read(ser.in_waiting)
print(f"Current settings:\n{data.decode()}")

# Set new values (example)
ser.write(b'R1=010101\r')
ser.write(b'R2=020202\r')
ser.write(b'R5=A1\r')

# Save and exit
ser.write(b'S\r')
ser.write(b'Q\r')

# Close serial port
ser.close()
