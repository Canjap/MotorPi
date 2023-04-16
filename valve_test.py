from gpiozero import OutputDevice
from time import sleep
relay = OutputDevice(26, active_high = False, initial_value = False)
relay.off()
try:
    for x in range(3):
        sleep(4)
        relay.on()
        sleep(4)
        relay.off()
except Exception as e:
    print(e)
finally:
    relay.off()
