from gpiozero import OutputDevice

relay = OutputDevice(26, active_high = True, initial_value = False)
relay.off()
relay.on()