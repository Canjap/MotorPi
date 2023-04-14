while True:
        data = conn.recv(1024) #change to "action" when configuring w mycroftPi
        if not data:
            break
        print(data)
        for x in range(data): #how to make it move in a sq path -> from raspberry pi robot buggy tutorial 
            motorPi.forward()
            sleep(3)
            motorPi.stop()
            # SOLENOID DROP CODE
            motorPi.right()
            sleep(1)
            motorPi.stop()
        motorPi.forward()