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

__all__ = ['Stop', 'Forwards', 'Backwards', 'SpinLeft', 'SpinRight', 'FLeft', 'FRight', 'BLeft', 'BRight']

global pinMotorAForwards, pinMotorABackwards

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

# Set variable for the LED pin
pinLED1 = 5
pinLED2 = 6

# How many times to turn the pin on and off each second
Frequency = 50

# How long the pin stays on each cycle, as a percent
DCA = 100
DCB = 100

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

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

def Motor1(SpeedAndDirection, duration=0):
	motors.Motor1(SpeedAndDirection, pwmMotorAForwards, pwmMotorABackwards)
	if duration > 0:
		time.sleep(duration)
		motors.Motor1(0, pwmMotorAForwards, pwmMotorABackwards)
	
def Motor2(SpeedAndDirection, duration=0):
	motors.Motor2(SpeedAndDirection, pwmMotorBForwards, pwmMotorBBackwards)
	if duration > 0:
		time.sleep(duration)
		motors.Motor2(0, pwmMotorBForwards, pwmMotorBBackwards)

def Stop():
	motors.Stop(pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards)

def Backwards(Speed, duration):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

def Forwards(Speed, duration):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.Forwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Forwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

	
def SRight(Speed, duration):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.SpinRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.SpinRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

def BLeft(Speed, duration):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.BLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.BLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

def FLeft(Speed, duration):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.FLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.FLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

def SLeft(Speed, duration):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.SpinLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.SpinLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

def BRight(Speed, duration):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.BRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.BRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

def FRight(Speed, duration):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.FRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.FRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, 0)

