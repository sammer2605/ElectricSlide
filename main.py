# Import gphoto2 as gp
import gphoto2 as gp
# Import time for waiting between shots
import time
# Import serial for communication with Arduino
import serial
# Import logging for debugging
import logging
# Import subprocess for calling shell commands
import subprocess
# capture_image() function
def capture_image(range):
    logging.basicConfig(format='%(levelname)s: %(name)s: %(message)s', level=logging.WARNING)
    # enable logging
    callback_obj = gp.check_result(gp.use_python_logging())
    # Set capture target to camera's memory card
    subprocess.call(["gphoto2", "--set-config", "capturetarget=1"])
    # Create new camera object
    camera = gp.Camera()
    # Initiate camera
    camera.init()
    print('Capturing image!')
    # Capture & Save image
    if range > 0:
        # Capture image
        file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
    camera.exit
    

# Function to communicate with Arduino
def comms(range):
    # Set up Serial variables
    ser = serial.Serial('COM11', 9600) # Replace with different directory if needed
    # Wait for Arduino to be ready
    response = ser.readline().decode().strip()
    # Print response
    print(response)
    # Send move command to Arduino
    if range > 0:
        ser.write("1".encode())
    time.sleep(0.5)
    print("sleep")
    ser.close()

''' Main Program '''
frames = int(input("Enter the number of frames: "))
pre_delay = int(input("Enter the delay before starting: "))
delay = int(input("Enter the delay between frames: "))
# Pre-delay to allow user to get into position
time.sleep(pre_delay)
# Loop to take pictures
for i in range(frames):
    # Capture image
    capture_image()
    # Send move command to Arduino
    comms(frames)
    # Wait for delay
    time.sleep(delay)