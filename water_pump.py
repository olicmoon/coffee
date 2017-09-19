#!/usr/bin/python

import GPIO
import time
from threading import Thread

TAG = "[WaterPump] "
class WaterPump():
    def __init__(self, max_mlps, pwm, in2):
        self.max_mlps = max_mlps
        self.pin_pwd = pwm
        self.pin_in2 = in2
        self.mlps = 0.0
        self.thread = None
        self.divider = 100

    def pump(self):
        print(TAG + "started")
        while self.mlps > 0:
            print(TAG + "mililiter_per_sec: ", self.mlps)
            motor_delay = (1.0 / self.max_mlps) * (self.max_mlps - self.mlps)
            print(TAG + "motor_delay: ", motor_delay)
            if motor_delay == 0:
                break

            for i in range(0, self.divider, 1):
                GPIO.output(self.pin_pwd, GPIO.HIGH)
                time.sleep(((motor_delay / 2) / self.divider))
                GPIO.output(self.pin_pwd, GPIO.DOWN)
                time.sleep(((motor_delay / 2) / self.divider))

        print(TAG + "stopped")
        self.thread = None

    def setup(self):
        print(TAG + "setup")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_pwd, GPIO.OUT, initial=GPIO.DOWN)
        GPIO.setup(self.pin_in2, GPIO.OUT, initial=GPIO.DOWN)

    def set_speed(self, gpm):
        self.mlps = gpm
        if gpm > 0:
            if self.thread == None:
                print(TAG + "creating thread..")
                self.thread = Thread(target=self.pump)
            if not self.thread.isAlive():
                print(TAG + "starting thread..")
                self.thread.start()
            else:
                print(TAG + "thread is alive")

    def destroy(self):
        GPIO.output(self.pin_pwd, GPIO.DOWN)
        GPIO.cleanup()

