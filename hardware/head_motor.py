#!/usr/bin/python

import time
from threading import Thread

import GPIO

TAG = "[HeadMotor] "
class HeadMotor():
    def __init__(self, ain1, ain2, bin1, bin2):
        self.pin_ain1 = ain1
        self.pin_ain2 = ain2
        self.pin_bin1 = bin1
        self.pin_bin2 = bin2
        self.rps = 0 # revolutions per second
        self.thread = None

    def spin(self):
        print(TAG + "started")
        while self.rps > 0:
            print(TAG + "rps: ", self.rps)
            time.sleep(1)
        print(TAG + "stopped")
        self.thread = None

    def setup(self):
        print(TAG + "setup")

    def set_speed(self, rps):
        self.rps = rps
        if rps > 0:
            if self.thread == None:
                print(TAG + "creating thread..")
                self.thread = Thread(target=self.spin)
            if not self.thread.isAlive():
                print(TAG + "starting thread..")
                self.thread.start()
            else:
                print(TAG + "thread is alive")
        print(TAG + "done..")

    def destroy(self):
        GPIO.cleanup()

