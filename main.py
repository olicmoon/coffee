#!/usr/bin/python
from command_ui import CommandUI
from hardware.head_motor import HeadMotor
from hardware.water_pump import WaterPump
from hardware.weight_scale import WeightScale

DEFAULT_CALIBRATION_FACTOR = 200

class Brewer():
    def main(self):
        self.water_pump = WaterPump(20)

        # GPIO pin assignment for AIN1/AIN2/BIN1/BIN2
        self.head_motor = HeadMotor(6, 13, 19, 26)

        self.weight_scale = WeightScale(23, 24)
        self.weight_scale.setup()
        self.weight_scale. set_calibration_factor(DEFAULT_CALIBRATION_FACTOR)

        ui = CommandUI(self)
        ui.start()

    def set_calibration_unit(self, calibration_unit):
        self.weight_scale.set_calibration_factor(calibration_unit)

    def get_weight(self):
        return self.weight_scale.get()

    def tare_weight(self):
        self.weight_scale.tare()

    def set_pump_speed(self, ml_per_sec):
        self.water_pump.set_speed(ml_per_sec)

    def set_head_speed(self, speed):
        self.head_motor.set_speed(speed)

    def shutdown(self):
        self.head_motor.destroy()
        self.water_pump.destroy()
        self.weight_scale.destroy()


b = Brewer()
b.main()


