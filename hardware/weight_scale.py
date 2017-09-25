#!/usr/bin/python

from threading import Thread
from hx711 import HX711

class WeightScale():
    def __init__(self, dout, sck):
        self.hx711 = HX711(dout, sck)
        self.scale_unit = 1000
        self.thread = None
        self.run = True

    def main(self):
        self.setup()

        while self.run:
            val = self.hx711.get_value(3)
            print val

        self.thread = None

    def get(self):
        v = self.hx711.get_value(3)
        if v < 0:
            return 0
        return (v / self.scale_unit)

    def reset(self):
        self.hx711.reset()

    def tare(self):
        self.hx711.tare()

    def set_calibration_factor(self, calibration_unit):
        self.hx711.set_calibration_factor(calibration_unit)

    def set_scale_unit(self, scale_unit):
        self.scale_unit = scale_unit

    def setup(self):
        self.hx711.power_up()
        self.hx711.tare()
        self.hx711.set_reading_format("LSB", "MSB")

    def start(self):
        if self.thread == None:
            self.thread = Thread(target=self.main)
        if not self.thread.isAlive():
            self.thread.start()

    def destroy(self):
        self.run = False
        self.hx711.power_down()

