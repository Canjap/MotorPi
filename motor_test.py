from gpiozero import Robot
from gpiozero import OutputDevice

relay = OutputDevice(26, active_high = True, initial_value = False)

motorPi = Robot(left=(7,8), right=(9,10)) #numbers are the GPIO pins controlling the R or L motor
print(motorPi.pin_factory)
relay.off()
try:
    motorPi.forward()
    relay.on()
except Exception as e:
    print(e)
finally:
    motorPi.stop()
    relay.off()