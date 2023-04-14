from gpiozero import OutputDevice

relay = OutputDevice(26, active_high = False, initial_value = True)
relay.on()
relay.off()