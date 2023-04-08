from gpiozero import Robot #library and class that controls the motors; works similarly to RPi.GPIO, but with less explciit pin control
from gpiozero import OutputDevice #controls the Relay HAT

'''
sets the Relay HAT as an OutputDevice #(a more general class in gpiozero) and controls pin 26 (BCM, 37 on BOARD).
active_high = True: if the on() method is called, pin 26 wil be set to HIGH. If this were False, then on() would set the the pin to LOW
initial_value = False: the Relay HAT is initially off 
'''
relay = OutputDevice(26, active_high = True, initial_value = False)  
'''
controls the motors, which are controlled by a L298N motor driver board and a 6V battery. 
Robot class: a gpiozero class that provides functions that control DC motors
left=(7,8): controls the GPIO 7 and 8 pins 
right=(9,10): controls the GPIO 9 and 10 pins
'''
motorPi = Robot(left=(7,8), right=(9,10)) #numbers are the GPIO pins controlling the R or L motor

try:
    motorPi.forward() #motors roll forward
    relay.on() #solenoid opens
except Exception as e:
    print(e) #prints any errors
finally: 
    motorPi.stop() #stops the motors
    relay.off() #turns off the solenoid valve
    #gpiozero automatically cleans up the pins after the script ends
