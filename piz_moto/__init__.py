# PiZ-Moto+ library
# Supports all the basic functions offered by the PiZ-Moto+ motor driver board:
# Motor1
# Motor2
# Line Sensor
# Range Sensor
# Servo1
# Servo2
# LED

import RPi.GPIO as GPIO # Import the GPIO Library
import time

from .motors import Motor1
from .motors import Motor2
from .motors import Stop
from .motors import Forwards
from .motors import Backwards
from .motors import SpinLeft
from .motors import SpinRight
from .motors import FLeft
from .motors import FRight
from .motors import BLeft
from .motors import BRight

__all__ = ['LED', 'LED1', 'LED2', 'Servo1', 'Servo2', 'ReadLineSensor', 'ReadRangeSensor', 'Stop', 'Forwards', 'Backwards', 'SpinLeft', 'SpinRight', 'FLeft', 'FRight', 'BLeft', 'BRight']

global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 7
pinMotorBBackwards = 8

# Set variables for the line detector GPIO pin
pinLineFollower = 25

# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18

# Set variable for the LED pins
# Only supported on PiZ-Moto (1.0)
pinLED1 = 5
pinLED2 = 6

# Set variable for the LED pin
# Only supported on PiZ-Moto+ (2.0)
pinLED = 6

# Set variable for General-Purpose I/O
# Only supported on PiZ-Moto+ (2.0)
pinGPIO1 = 16
pinGPIO2 = 19

# How many times to turn the pin on and off each second
Frequency = 50

# How many times to turn the pin on and off each second
ServoFrequency = 50

# How long the pin stays on each cycle, as a percent
DCA = 100
DCB = 100

# Setup GPIO to BCM mode & disable warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# **********************************************************#    
# Main functions                                            #
# **********************************************************#

# Setup I/O for motor control pins
def SetupMotors():
    global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards
    GPIO.setup(pinMotorAForwards, GPIO.OUT)
    GPIO.setup(pinMotorABackwards, GPIO.OUT)
    GPIO.setup(pinMotorBForwards, GPIO.OUT)
    GPIO.setup(pinMotorBBackwards, GPIO.OUT)
    pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
    pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
    pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
    pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)
    pwmMotorAForwards.start(0)
    pwmMotorABackwards.start(0)
    pwmMotorBForwards.start(0)
    pwmMotorBBackwards.start(0)

# Setup I/O for Servo ports
def SetupServos():
    GPIO.setup(pinGPIO1, GPIO.OUT)
    GPIO.setup(pinGPIO2, GPIO.OUT)
    pwmServo1 = GPIO.PWM(pinGPIO1, ServoFrequency)
    pwmServo2 = GPIO.PWM(pinGPIO2, ServoFrequency)
    pwmServo1.start(0)
    pwmServo2.start(0)

# Setup I/O for LineSensor
def SetupLineSensor():
    GPIO.setup(pinLineFollower, GPIO.IN)

# Setup I/O for RangeSensor
def SetupRangeSensor():
    GPIO.setup(pinTrigger, GPIO.OUT)
    GPIO.setup(pinEcho, GPIO.IN)

# Setup I/O for LED
def SetupLED(Version=2.0):
    if Version == 1.0:
        GPIO.setup(pinLED1, GPIO.OUT)
        GPIO.setup(pinLED2, GPIO.OUT)
    else:
        GPIO.setup(pinLED, GPIO.OUT)

# Function to control speed & direction of Motor 1/A
def Motor1(SpeedAndDirection, duration=0):
	global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards
	motors.Motor1(SpeedAndDirection, pwmMotorAForwards, pwmMotorABackwards)
	if duration > 0:
		time.sleep(duration)
		motors.Motor1(0, pwmMotorAForwards, pwmMotorABackwards)
	
# Function to control speed & direction of Motor 2/B
def Motor2(SpeedAndDirection, duration=0):
	global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards
	motors.Motor2(SpeedAndDirection, pwmMotorBForwards, pwmMotorBBackwards)
	if duration > 0:
		time.sleep(duration)
		motors.Motor2(0, pwmMotorBForwards, pwmMotorBBackwards)

# Function to control the LED (D2)
def LED(LED_State):
    GPIO.output(pinLED,LED_State)
    
# Function to set GPIO port / LED1
# PiZ-Moto V1.0 only
def LED1():
    GPIO.output(pinLED1,LED_State)

# Function to set GPIO port LED2
# PiZ-Moto V1.0 only
def LED2():
    GPIO.output(pinLED2,LED_State)

# Function to read the line sensor (J7)
def ReadLineSensor():
    LineSensor = GPIO.input(pinLineFollower)
    return LineSensor
    
# Function to read the Range Sensor (J8)
def ReadRangeSensor(Readings=3):
    global Distance

    # Check the number of readings requested...
    # max = 10, min = 1
    if Readings < 1:
        Readings = 1
    if Readings > 100:
        Readings = 100
        
    for Reading in range (0,Readings):

        # Send 10us pulse to trigger
        GPIO.output(pinTrigger, True)
        time.sleep(0.00001)
        GPIO.output(pinTrigger, False)
        
        # Start the timer
        StartTime = time.time()
        
        # The start time is reset until the Echo pin is taken high (==1)
        while GPIO.input(pinEcho)==0:
            StartTime = time.time()
        
        # Stop when the Echo pin is no longer high - the end time
        while GPIO.input(pinEcho)==1:
            StopTime = time.time()
            # If the sensor is too close to an object, the Pi cannot
            # see the echo quickly enough, so it has to detect that
            # problem and say what has happened
            if StopTime-StartTime >= 0.04:
                print("Hold on there! You're too close for me to see.")
                StopTime = StartTime
                break
        
        # Remember previous measurement for running average calculation
        if Reading > 0:
            PrevDistance = Distance

        # Calculate pulse length
        ElapsedTime = StopTime - StartTime
        # Distance pulse traveled in that time is
        # time multiplied by the speed of sound (cm/s)
        Distance = ElapsedTime * 34326
        
        # That was the distance there and back so halve the value
        Distance = Distance / 2
        
        # Calculate running average
        # but not if it's the first reading!
        if Reading > 0:
            Distance = Distance + PrevDistance
            Distance = Distance / 2

        # Small delay to ensure read frequency never exceeds 40Hz
        time.sleep(0.025)

    return Distance
    
# Function to control Servo1 (J5)
def Servo1(Angle):
	pwmServo1.ChangeDutyCycle(Angle)

# Function to control Servo2 (J6)
def Servo2(Angle):
	pwmServo2.ChangeDutyCycle(Angle)



# **********************************************************#    
# A few extra functions to support a simple 2-wheeled robot #
# **********************************************************#

# Function to stop both motors
def Stop():
	global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards
	motors.Stop(pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards)

# Backwards...
def Backwards(Speed, duration):
	global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

# Forwards...
def Forwards(Speed, duration):
	global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.Forwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Forwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

# Spin left
def SLeft(Speed, duration):
	global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.SpinLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.SpinLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

# Backwards and left a bit
def BLeft(Speed, duration):
	global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.BLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.BLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

# Forwards and left a bit
def FLeft(Speed, duration):
	global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.FLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.FLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

# Spin right
def SRight(Speed, duration):
	global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.SpinRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.SpinRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

# Backwards and right a bit
def BRight(Speed, duration):
	global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.BRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.BRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

# Forwards and right a bit
def FRight(Speed, duration):
	global pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.FRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.FRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

