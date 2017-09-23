#!/usr/bin/python

import time
from threading import Thread

import RPi.GPIO as GPIO

class WaterPump():
    def __init__(self, max_mlps, pwm, in2):
        self.max_mlps = max_mlps
        self.pin_pwd = pwm
        self.pin_in2 = in2
        self.mlps = 0.0
        self.thread = None
        self.divider = 100
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_pwd, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.pin_in2, GPIO.OUT, initial=GPIO.HIGH)

    def pump(self):
        while self.mlps > 0:
            motor_delay = (1.0 / self.max_mlps) * (self.max_mlps - self.mlps)
            if motor_delay == 0:
                break

            for i in range(0, self.divider, 1):
                if self.mlps == 0:
                    GPIO.output(self.pin_pwd, GPIO.LOW)
                    break;
                GPIO.output(self.pin_pwd, GPIO.HIGH)
                time.sleep(((motor_delay / 2) / self.divider))
                GPIO.output(self.pin_pwd, GPIO.LOW)
                time.sleep(((motor_delay / 2) / self.divider))

        self.thread = None

    def set_speed(self, gpm):
        if self.thread == None:
            self.thread = Thread(target=self.pump)

        self.mlps = gpm

        if gpm > 0:
            if not self.thread.isAlive():
                self.thread.start()

    def destroy(self):
        self.mlps = 0
        GPIO.output(self.pin_in2, GPIO.LOW)
        GPIO.output(self.pin_pwd, GPIO.LOW)

