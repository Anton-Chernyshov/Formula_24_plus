#import gpiozero

#from gpiozero import Button, LED
#from gpiozero.pins.pigpio import PiGPIOFactory

import math

import definitions as defs






def rpmToKph(rpm):
    """Convert Rpm to Kph based on wheel diameter""" 
    wheel_circumference = defs.WHEEL_DIAMETER * math.pi
    kph = (rpm * wheel_circumference) / 1000 * 60
    return kph * defs.AXLE_TO_WHEEL_GEAR_RATIO_CONSTANT

def kphToMph(kph):
    """Convert Kph to Mph"""
    return kph * 0.621371

