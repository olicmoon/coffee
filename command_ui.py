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

    def start_brewing(self, head_speed, pump_speed, taret_weight):
        self.head_speed = head_speed
        self.pump_speed = pump_speed
        self.target_weight = taret_weight
        self.brewer.tare_weight()
        self.brewer.set_pump_speed(self.pump_speed)
        self.brewer.set_head_speed(self.head_speed)

    def update(self, progress):
        if progress < 10:
            self.pump_speed = 10
        elif progress < 20:
            self.pump_speed = 20
        elif progress < 50:
            self.pump_speed = 80
        elif progress < 80:
            self.pump_speed = 20
        elif progress < 90:
            self.pump_speed = 15
        else:
            self.pump_speed = 10

        self.brewer.set_pump_speed(self.pump_speed)

    def finish_brewing(self):
        self.head_speed = 0
        self.pump_speed = 0
        self.brewer.set_pump_speed(self.pump_speed)
        self.brewer.set_head_speed(self.head_speed)

    def start(self):
        x = 0
        self.target_weight = 0
        self.head_speed = 0
        self.pump_speed = 0
        progress = -1

        while x != ord('q'):
            screen = curses.initscr()

            weight = self.brewer.weight_scale.get()
            if weight > self.target_weight:
                self.finish_brewing()

            screen.border(0)
            screen.addstr(1, 2, "[q] shutdown [s] start brewing [f] finish brewing", curses.A_UNDERLINE)
            screen.addstr(2, 2, "[t] tare scale", curses.A_UNDERLINE)
            screen.addstr(3, 2, "[o] inc pump speed [p] dec pump speed [k] inc head speed [l] dec head speed", curses.A_UNDERLINE)
            screen.addstr(5, 4, "Water pump speed [10 - 100]: " + str(self.pump_speed).zfill(3), curses.COLOR_CYAN)
            screen.addstr(6, 4, "Head motor speed: " + str(self.head_speed).zfill(2), curses.COLOR_CYAN)
            screen.addstr(7, 4, "Weight: " + str(weight).zfill(4), curses.COLOR_CYAN)
            screen.refresh()

            screen.nodelay(1)
            x = screen.getch()
            time.sleep(0.5)

            if progress != -1:
                progress = (weight * 100) / self.target_weight
                screen.addstr(14, 4, "Progress " + str(`progress`).zfill(4) + "%", curses.COLOR_RED)
                self.update(progress)

            if x == ord('s'):
                screen.addstr(15, 4, "Starting..", curses.COLOR_RED)
                self.start_brewing(8, 15, 150)
                progress = 0
                curses.endwin()
            if x == ord('f'):
                progress = -1
                screen.addstr(15, 4, "Finished..", curses.COLOR_RED)
                self.finish_brewing()
                curses.endwin()
            if x == ord('o'):
                if self.pump_speed < 100:
                    self.pump_speed += 10
                self.brewer.set_pump_speed(self.pump_speed)
            if x == ord('p'):
                self.pump_speed -= 10
                if self.pump_speed < 0:
                    self.pump_speed = 0
                self.brewer.set_pump_speed(self.pump_speed)
            if x == ord('k'):
                if self.head_speed < 10:
                    self.head_speed += 1
                self.brewer.set_head_speed(self.head_speed)
            if x == ord('l'):
                self.head_speed -= 1
                if self.head_speed < 0:
                    self.head_speed = 0
                self.brewer.set_head_speed(self.head_speed)
            if x == ord('t'):
                self.brewer.tare_weight()
                curses.endwin()
            if x == ord('1'):
                curses.endwin()

        self.brewer.shutdown()
        curses.endwin()