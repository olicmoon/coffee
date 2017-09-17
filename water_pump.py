#!/usr/bin/python

import GPIO
import time
from threading import Thread

TAG = "[WaterPump] "
class WaterPump():
    def __init__(self, max_mlps, pwm, in1, in2):
        self.max_mlps = max_mlps;
        self.pin_pwd = pwm;
        self.pin_in1 = in1;
        self.pin_in2 = in2;
        self.mililiter_per_sec = 0;
        self.thread = Thread(target=self.pump)

    def pump(self):
        print(TAG + "started")
        while self.mililiter_per_sec > 0:
            print(TAG + "mililiter_per_sec: ", self.mililiter_per_sec)
            delay = (1.0 / self.max_mlps) * self.mililiter_per_sec
            print(TAG + "delay: ", delay)
            GPIO.output(self.pin_pwd, GPIO.HIGH)
            time.sleep(delay/2)
            GPIO.output(self.pin_pwd, GPIO.OUT)
            time.sleep(delay/2)
        print(TAG + "stopped")

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_pwd, GPIO.OUT, initial=GPIO.DOWN)
        GPIO.setup(self.pin_in1, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(self.pin_in2, GPIO.OUT, initial=GPIO.DOWN)

    def set_speed(self, gpm):
        self.mililiter_per_sec = gpm
        if not self.thread.isAlive():
            self.thread.start()

    def destroy(self):
        GPIO.output(self.pin_pwd, GPIO.DOWN)
        GPIO.cleanup()

