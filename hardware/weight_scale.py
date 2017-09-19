#!/usr/bin/python

import GPIO
import time
from threading import Thread
from hx711 import HX711

calibration_factor = 100 # TODO: for test only

TAG = "[WeightScale] "
class WeightScale():
    def __init__(self, dout, sck):
        self.hx711 = HX711(dout, sck)
        self.thread = None

    def main(self):
        self.setup()

        print(TAG + "started")
        while True:
            val = self.hx711.get_value(3)
            print val

        self.thread = None

    def setup(self):
        print(TAG + "setup")
        self.hx711.power_up()
        self.hx711.tare()
        self.hx711.set_reading_format("LSB", "MSB")
        self.hx711.set_calibration_factor(calibration_factor)

    def start(self):
        if self.thread == None:
            print(TAG + "creating thread..")
            self.thread = Thread(target=self.main)
        if not self.thread.isAlive():
            print(TAG + "starting thread..")
            self.thread.start()
        else:
            print(TAG + "thread is alive")

    def destroy(self):
        self.hx711.power_down()
        GPIO.cleanup()

