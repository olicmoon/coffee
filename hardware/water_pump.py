#!/usr/bin/python

import sys
import time
from threading import Thread

import RPi.GPIO as GPIO

class WaterPump():
    def __init__(self, pwm):
        self.debug = False
        self.pin_pwd = pwm
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_pwd, GPIO.OUT)
        self.pt = GPIO.PWM(self.pin_pwd, 32)
        self.pt.start(0)

    # speed range: 10 ~ 100
    def set_speed(self, speed):
        if speed <= 15:
            hz = 16
        elif speed <= 20:
            hz = 32
        else:
            hz = 512

        self.pt.ChangeDutyCycle(speed)
        self.pt.ChangeFrequency(hz)

    def destroy(self):
        self.speed = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.output(self.pin_pwd, GPIO.LOW)


# w = WaterPump(int(sys.argv[1]))
# w.debug = True
# w.set_speed(float(sys.argv[2]))
#
# time.sleep(3)
#
# w.set_speed(0)
