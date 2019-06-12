#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#lecteur de mp3 piloté par tel à cadran socotel s63
import os
import Queue
import threading
import signal
import sys
#import yaml
import RPi.GPIO as GPIO
import time
from s63.RotaryDial import RotaryDial
from wradio import wradio

callback_queue = Queue.Queue()

class TelephonDaemon:

    last = 0
    dial_number = 0
    RotaryDial = None
    #Sons = None
    def __init__(self):
        print("[STARTUP]")
        self.RotaryDial = RotaryDial()
        self.RotaryDial.RegisterCallback(NumberCallback = self.GotDigit, StartSonCallback = self.StartSon)

        #self.Sons()
        input("Waiting.\n")

    def GotDigit(self, digit):
        print "[DIGIT] Got digit: %s" % digit
        self.dial_number = digit
        #self.dial_number = digit - self.last 
        print "[NUMBER] We have: %s" % self.dial_number
        self.dial_number = 0
        Sons(digit)
        digit = 0
        #self.dial_number = self.last
        self.dial_number = 0

    def StartSon(self):
        print("play")
        self.StartSon = True
        self.dial_number = 0

def main():
    TDaemon = TelephonDaemon()

if __name__ == "__main__":
    main()

