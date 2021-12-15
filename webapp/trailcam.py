from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
count = 0
image = f'static/img/{count}'
while True:
    pir.wait_for_motion(timeout=5)
    with PiCamera() as camera:
        camera.hflip = True
        camera.capture(image)
        count += 1
