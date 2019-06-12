#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Rotary Dial Parser
# Expects the following hardware rules:
# 1 is 1 pulse
# 9 is 9 pulses
# 0 is 10 pulses

import RPi.GPIO as GPIO
from threading import Timer
import time

class RotaryDial:
   # global current_digit
    # We'll be reading BCM GPIO 4 (pin 7 on board)
    pin_rotary = 4


    # After 900ms, we assume the rotation is done and we get
    # the final digit. 
    digit_timeout = 0.5

    # We keep a counter to count each pulse.
    current_digit = 0
    # Simple timer for handling the number callback
    number_timeout = None
    last_input = 0

    def __init__(self):
	
	current_digit = 0
         # Set GPIO mode to Broadcom SOC numbering
        GPIO.setmode(GPIO.BCM)

        # Listen for rotary movements
        GPIO.setup(self.pin_rotary, GPIO.IN)
        GPIO.add_event_detect(self.pin_rotary, GPIO.BOTH, callback = self.NumberCounter)
               

    # Handle counting of rotary movements and respond with digit after timeout
    def NumberCounter(self, channel):
        input = GPIO.input(self.pin_rotary)
        #print "[INPUT] %s (%s)" % (input, channel)
        if input and not self.last_input:
            self.current_digit += 1

            if self.number_timeout is not None:
                self.number_timeout.cancel()

            self.number_timeout = Timer(self.digit_timeout, self.FoundNumber)
            self.number_timeout.start()
        self.last_input = input
        time.sleep(0.02)

   

    # When the rotary movement has timed out, we callback with the final digit
    def FoundNumber(self):
        #if self.current_digit == 10:
           # self.current_digit = 0
        self.NumberCallback(self.current_digit)
        self.current_digit = 0
        print("current_digit:", self.current_digit)

    def Lecture(self):
        if self.StartSon == 1:
            self.current_digit = 0
            self.StartSonCallback()

    # Handles the callbacks we're supplying
    def RegisterCallback(self, NumberCallback, StartSonCallback):
        self.NumberCallback = NumberCallback
        self.StartSonCallback = StartSonCallback
       
