#!/usr/bin/env python2.7
# Simple candle simulator.
# Uses a motor driver to drive a small 6V filament bulb using pulse width modulation to control the lamp brightness
# and modulates the pwm modulation with a sequence derived from measuring the flicker of a real candle
# Compatible with the Edukit 3 motor driver and the PiZ-Moto / PiZ-Moto+

import RPi.GPIO as GPIO # Import the GPIO Library
import time

# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinLampPositive = 10
pinLampNegative = 11

# How many times to turn the pin on and off each second
Frequency = 50

# Define a sequence of values that defines how the lamp will be modulated
lamp_modulation = [ 10,  10,  20,  30,  30,  30,  40,  50,
                    60,  70,  80,  70,  70,  60,  60,  50,
                    50,  50,  60,  70,  80,  90, 100, 120,
                    140, 160, 240, 250, 100, 150, 250, 250,
                    140, 240, 230, 220, 100,  80,  70,  70,
                    70,  80,  80, 140, 130, 120, 110, 200,
                    210, 220, 220, 100,  90,  40,  30,  30,
                    30,  20,  20,  10,  10,  10,  20,  10]


# Set the GPIO Pin mode to be Output
GPIO.setup(pinLampPositive, GPIO.OUT)
GPIO.setup(pinLampNegative, GPIO.OUT)

# Turn lamp off
def LampOff():

    pwmLampPositive.ChangeDutyCycle(0)
    pwmLampNegative.ChangeDutyCycle(0)
	
# Turn lamp on
def LampOn():

    for i in lamp_modulation:
        pwmLampPositive.ChangeDutyCycle(100*i/255)
        pwmLampNegative.ChangeDutyCycle(0)
        print i
        time.sleep(0.01)
    
    for i in lamp_modulation:
        pwmLampPositive.ChangeDutyCycle(100*i/255)
        pwmLampNegative.ChangeDutyCycle(0)
        print i
        time.sleep(0.01)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmLampPositive = GPIO.PWM(pinLampPositive, Frequency)
pwmLampNegative = GPIO.PWM(pinLampNegative, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. off)
pwmLampPositive.start(0)
pwmLampNegative.start(0)


try:
	
    # Repeat the next indented block forever
    while True:

        # Turn the lamp on and run a single cycle
        LampOn()

	
# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()
			
