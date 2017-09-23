#!/usr/bin/python

from os import system
import curses

class CommandUI():
    def __init__(self, b):
        self.brewer = b

    def get_param(self, prompt_string):
        self.screen.clear()
        self.screen.border(0)
        self.screen.addstr(2, 2, prompt_string)
        self.screen.refresh()
        input = self.screen.getstr(10, 10, 60)
        return input

    def execute_cmd(cmd_string):
        system("clear")
        a = system(cmd_string)
        print ""
        if a == 0:
            print "Command executed correctly"
        else:
            print "Command terminated with error"
        raw_input("Press enter")
        print ""

    def start(self):
        x = 0
        pump_speed = 0
        progress_col = 20
        while x != ord('4'):
            screen = curses.initscr()

            screen.border(0)
            screen.addstr(1, 2, "[s] start [t] tare scale [o] + pump speed [p] - pump speed")
            screen.addstr(3, 4, "Water pump speed: " + `pump_speed`)
            screen.addstr(4, 4, "Weight: " + `self.brewer.weight_scale.get()`)
            screen.refresh()

            screen.nodelay(1)
            x = screen.getch()

            if x == ord('s'):
                pump_speed = 5
                screen.addstr(progress_col, 4, "Starting..")
                self.brewer.tare_weight()
                self.brewer.set_pump_speed(pump_speed)
                curses.endwin()
            if x == ord('o'):
                if pump_speed < 29:
                    pump_speed += 1
                self.brewer.set_pump_speed(pump_speed)
            if x == ord('p'):
                if pump_speed > 3:
                    pump_speed -= 1
                self.brewer.set_pump_speed(pump_speed)
            if x == ord('t'):
                self.brewer.tare_weight()
                curses.endwin()
            if x == ord('1'):
                curses.endwin()

        self.brewer.shutdown()
        curses.endwin()