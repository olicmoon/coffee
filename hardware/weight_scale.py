#!/usr/bin/python

from threading import Thread
from hx711 import HX711

calibration_factor = 100 # TODO: for test only

class WeightScale():
    def __init__(self, dout, sck):
        self.hx711 = HX711(dout, sck)
        self.thread = None
        self.run = True

    def main(self):
        self.setup()

        while self.run:
            val = self.hx711.get_value(3)
            print val

        self.thread = None

    def get(self):
        return self.hx711.get_value(3)

    def reset(self):
        self.hx711.reset()

    def tare(self):
        self.hx711.tare()

    def setup(self):
        self.hx711.power_up()
        self.hx711.tare()
        self.hx711.set_reading_format("LSB", "MSB")
        self.hx711.set_calibration_factor(calibration_factor)

    def start(self):
        if self.thread == None:
            self.thread = Thread(target=self.main)
        if not self.thread.isAlive():
            self.thread.start()

    def destroy(self):
        self.run = False
        self.hx711.power_down()

