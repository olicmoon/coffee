import threading
from water_pump import WaterPump

# 29 gallon per hour (== 30ml per sec)
water_pump = WaterPump(30, 20, 21, 22)
water_pump.setup()

TAG = "[Main] "
while True:
    n = raw_input("gallon per minute:")
    try:
        print(TAG + "input: %c" % n)
        water_pump.set_speed(float(n))
    except ValueError:
        water_pump.set_speed(0)
        break

print("Bye")

