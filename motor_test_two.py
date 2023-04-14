from gpiozero import Robot
from time import sleep

motorPi = Robot(left=(7,8), right=(9,10)) #numbers are the GPIO pins controlling the R or L motor

try:
    motorPi.forward(0.5)
    motorPi.stop()
except Exception as e:
    print(e)
finally:
    motorPi.stop()
