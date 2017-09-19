#!/usr/bin/python

from hardware.head_motor import HeadMotor
from hardware.water_pump import WaterPump

water_pump = WaterPump(30, 20, 21)
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

