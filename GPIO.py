
# import RPi._GPIO as GPIO

TAG = "[GPIO] "

BCM = 50

OUT = 1

HIGH = 1
DOWN = 0

def setmode(mode):
    print(TAG + "setmode [%d]" % mode);
    return None


def cleanup():
    print(TAG + "cleanup");


def setup(pin, mode, initial):
    print(TAG + "setup [pin:", pin, "] [mode:", mode, "] [initial:", initial, "]");
    return None


def output(pin, val):
    print(TAG + "output [pin", pin, "] [val:", val, "]");
    return None