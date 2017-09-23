#!/usr/bin/python

from os import system
import curses

import time


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
        head_speed = 0
        pump_speed = 0
        progress_col = 20
        while x != ord('q'):
            screen = curses.initscr()

            screen.border(0)
            screen.addstr(1, 2, "[q] shutdown [s] start [t] tare scale", curses.A_UNDERLINE)
            screen.addstr(2, 2, "[o] inc pump speed [p] dec pump speed [k] inc head speed [l] dec head speed", curses.A_UNDERLINE)
            screen.addstr(4, 4, "Water pump speed: " + `pump_speed`, curses.COLOR_CYAN)
            screen.addstr(5, 4, "Head motor speed: " + `head_speed`, curses.COLOR_CYAN)
            screen.addstr(6, 4, "Weight: " + `self.brewer.weight_scale.get()`, curses.COLOR_CYAN)
            screen.refresh()

            screen.nodelay(1)
            x = screen.getch()
            time.sleep(0.5)

            if x == ord('s'):
                head_speed = 8
                pump_speed = 5
                screen.addstr(progress_col, 4, "Starting..")
                self.brewer.tare_weight()
                self.brewer.set_pump_speed(pump_speed)
                self.brewer.set_head_speed(head_speed)
                curses.endwin()
            if x == ord('o'):
                if pump_speed < 29:
                    pump_speed += 1
                self.brewer.set_pump_speed(pump_speed)
            if x == ord('p'):
                pump_speed -= 1
                if pump_speed < 0:
                    pump_speed = 0
                self.brewer.set_pump_speed(pump_speed)
            if x == ord('k'):
                if head_speed < 10:
                    head_speed += 1
                self.brewer.set_head_speed(head_speed)
            if x == ord('l'):
                head_speed -= 1
                if head_speed < 0:
                    head_speed = 0
                self.brewer.set_head_speed(head_speed)
            if x == ord('t'):
                self.brewer.tare_weight()
                curses.endwin()
            if x == ord('1'):
                curses.endwin()

        self.brewer.shutdown()
        curses.endwin()