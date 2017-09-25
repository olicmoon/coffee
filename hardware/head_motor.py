#!/usr/bin/python

import time
from threading import Thread

import RPi.GPIO as GPIO

class HeadMotor():
    def __init__(self, ain1, ain2, bin1, bin2):
        self.step_pins = [ain1, ain2, bin1, bin2]
        self.delay = 0
        self.thread = None
        GPIO.setmode(GPIO.BCM)
        for pin in self.step_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        self.seq = [[1, 0, 1, 0],
               [0, 1, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 0, 1]]

    def spin(self):
        counter = 0
        while self.speed > 0:
            for pin in range(0, 4):
                xpin = self.step_pins[pin]  # Get GPIO
                # print "counter:" + `counter` + " xpin:" + `xpin` + ", " + `self.seq[counter][pin]`
                if self.seq[counter][pin] != 0:
                    GPIO.output(xpin, GPIO.HIGH)
                else:
                    GPIO.output(xpin, GPIO.LOW)
            counter += 1
            if counter > 3:
                counter = 0

            if self.speed == 0:
                break
            # print "delay" + `(0.001 * float(10 - self.speed))`
            time.sleep(0.001 * float(11 - self.speed))

        for pin in self.step_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

        self.thread = None

    def set_speed(self, speed):
        if speed > 10:
            speed = 10
        self.speed = speed

        if self.thread == None:
            self.thread = Thread(target=self.spin)

        if self.speed > 0:
            if not self.thread.isAlive():
                self.thread.start()

    def destroy(self):
        self.speed = 0
        GPIO.setmode(GPIO.BCM)
        for pin in self.step_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
# h = HeadMotor(6, 13, 19, 26)
# h.set_speed(10)