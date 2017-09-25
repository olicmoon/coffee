import time
import sys
import datetime
import RPi.GPIO as GPIO


def tonet(hz,d):
    pt = GPIO.PWM(pin, hz)
    pt.start(d)        # duty cycle
    time.sleep(3)

    pt = GPIO.PWM(pin, 16)
    pt.stop
    GPIO.output(pin, GPIO.LOW)  # good house keeping
    return


# Pin Definitons:
pin = int(sys.argv[1])

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(pin, GPIO.OUT) #  pin set as output

print 'start pwm'

tonet(float(sys.argv[2]), float(sys.argv[3]))

GPIO.cleanup()