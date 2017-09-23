#!/usr/bin/python

import time
from threading import Thread

import GPIO

class HeadMotor():
    def __init__(self, ain1, ain2, bin1, bin2):
        self.pin_ain1 = ain1
        self.pin_ain2 = ain2
        self.pin_bin1 = bin1
        self.pin_bin2 = bin2
        self.rps = 0 # revolutions per second
        self.thread = None

    def spin(self):
        while self.rps > 0:
            time.sleep(1)
        self.thread = None

    def set_speed(self, rps):
        self.rps = rps
        if rps > 0:
            if self.thread == None:
                self.thread = Thread(target=self.spin)
            if not self.thread.isAlive():
                self.thread.start()

    def destroy(self):
        self.rps = 0
        GPIO.cleanup()

