#Libraries
from machine import Pin
import time
import utime

try:
    while True:
        #set GPIO Pins
        GPIO_TRIGGER = Pin(12, Pin.OUT)
        GPIO_ECHO = Pin(14, Pin.IN)
        GPIO_TRIGGER.value(0)
        time.sleep(2)
        GPIO_TRIGGER.value(1)
        time.sleep(0.0001)
        GPIO_TRIGGER.value(0)

        # save StartTime
        while GPIO_ECHO.value() == 0:
            uStartTime = utime.ticks_us()
        # save time of arrival
        while GPIO_ECHO.value() == 1:
            uStopTime = utime.ticks_us()
        
        # time difference between start and arrival
        uTimeElapsed = uStopTime - uStartTime
        print('TimeElapsed',uTimeElapsed)
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        udistance = ((uTimeElapsed/ 1000000) *34300)/2
        print ("Measured Distance = %.1f cm" % udistance)
    # Reset by pressing CTRL + C
except KeyboardInterrupt:
    print("Measurement stopped by User")
 

    