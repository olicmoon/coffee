#!/usr/bin/python

import threading
from water_pump import WaterPump
from head_motor import HeadMotor

# 29 gallon per hour (== 30ml per sec)
# GPIO pin assignment for PWM/IN1/IN2
water_pump = WaterPump(30, 20, 21, 22)
water_pump.setup()

# GPIO pin assignment for AIN1/AIN2/BIN1/BIN2
head_motor = HeadMotor(10, 11, 12, 13)
head_motor.setup()

TAG = "[Main] "
while True:
    n = raw_input("milliliter per second:")
    try:
        print(TAG + "input: " + n)

        head_motor.set_speed(int(n))
        water_pump.set_speed(float(n))
    except ValueError:
        head_motor.set_speed(0)
        water_pump.set_speed(0)
        break

print("Bye")

