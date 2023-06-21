# Import serial
import serial
# Import time
import time

# Set the serial port and baud rate
ser = serial.Serial('COM11', 9600) # Replace COM11 as necessary

# Send message to Arduino
# message = "Hello, Arduino!"
# ser.write(message.encode())
running = True
# Read response from Arduino
while running:
    # time.sleep(1)
    response = ser.readline().decode().strip()
    print(response)
    if int(input("Enter 1 to send: ")) == 1:
        # time.sleep(1)
        ser.write("1".encode())
        # print("RPi: A")
        # time.sleep(1)
        # response = ser.readline().decode().strip()
        # print("Arduino:", response)
        # running = False
    time.sleep(0.5)
ser.close()
