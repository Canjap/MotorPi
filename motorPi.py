import socket 
from gpiozero import Robot 
from gpiozero import OutputDevice
from time import sleep

HOST = "192.168.1.204" #IP address of the server/MotorPi
PORT = 8181 #the specific port to link to

'''
controls the motors, which are controlled by a L298N motor driver board and a 6V battery. 
Robot class: a gpiozero class that provides functions that control DC motors
left=(7,8): controls the GPIO 7 and 8 pins 
right=(9,10): controls the GPIO 9 and 10 pins
'''

motorPi = Robot(
        left=(7,8), right=(9,10)
        )
'''
sets the Relay HAT as an OutputDevice #(a more general class in gpiozero) and controls pin 26 (BCM, 37 on BOARD).
active_high = True: if the on() method is called, pin 26 wil be set to HIGH. If this were False, then on() would set the the pin to LOW
initial_value = False: the Relay HAT is initially off 
'''
relay = OutputDevice(26,
                     active_high = False,
                     initial_value = False
                     )  
try:
    '''
    binds to this RPi's IP address and port 8181,
    listens for a connection,
    and saves the values from the server.accept() call into the conn and addr variables
    '''
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
        )
    server.bind((HOST, PORT))
    server.listen(2)
    conn, addr = server.accept() 
    print("connected by {}".format(addr))
    numseeds = conn.recv(1024).decode('utf-8') #saves numseeds as whatever value the server gets from the client/Mycroft Pi
    numseeds = int(numseeds)
    for x in range(numseeds):
        relay.on()
        sleep(4)
        relay.off()
        motorPi.forward(0.6) #moves forward, can be changed from 0-1
        sleep(2)
        motorPi.stop() 
    sleep(2)#waits three seconds 
except Exception as e:
    print(e)
finally:
    motorPi.stop() #stops the motors
    relay.off()
    print ("finished")

    #gpiozero automatically cleans up the GPIO pins