import gphoto2 as gp

def capture_image():
    # Create a new camera instance
    camera = gp.Camera()

    # Initialize the camera
    camera.init()

    # Capture an image
    file_path = camera.capture(gp.GP_CAPTURE_IMAGE)
    print('Image captured:', file_path)

    # Close the camera
    camera.exit()

# Call the function to capture an image
capture_image()
