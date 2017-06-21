import RPi.GPIO as GPIO # Import the GPIO Library
import time


from .motors import Stop
from .motors import Forwards
from .motors import Backwards
from .motors import SpinLeft
from .motors import SpinRight
from .motors import FLeft
from .motors import FRight
from .motors import BLeft
from .motors import BRight

__all__ = ['Servo1', 'Servo2', 'Servo3', 'Servo4', 'Stop', 'Forwards', 'Backwards', 'SpinLeft', 'SpinRight', 'FLeft', 'FRight', 'BLeft', 'BRight']

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 7
pinMotorBBackwards = 8

pinMotorCForwards = 24
pinMotorCBackwards = 27
pinMotorDForwards = 22
pinMotorDBackwards = 23

# Set variables for the line detector GPIO pin
pinLineFollower = 25
pinLineFollower2 = 4

# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18
pinTrigger2 = 19
pinEcho2 = 16

# Set variable for the LED pin
pinServo1 = 5
pinServo2 = 6
pinServo3 = 12
pinServo4 = 13

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
GPIO.setup(pinMotorCForwards, GPIO.OUT)
GPIO.setup(pinMotorCBackwards, GPIO.OUT)
GPIO.setup(pinMotorDForwards, GPIO.OUT)
GPIO.setup(pinMotorDBackwards, GPIO.OUT)

GPIO.setup(pinServo1, GPIO.OUT)
GPIO.setup(pinServo2, GPIO.OUT)
GPIO.setup(pinServo3, GPIO.OUT)
GPIO.setup(pinServo4, GPIO.OUT)

pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)
pwmMotorCForwards = GPIO.PWM(pinMotorCForwards, Frequency)
pwmMotorCBackwards = GPIO.PWM(pinMotorCBackwards, Frequency)
pwmMotorDForwards = GPIO.PWM(pinMotorDForwards, Frequency)
pwmMotorDBackwards = GPIO.PWM(pinMotorDBackwards, Frequency)

pwmServo1 = GPIO.PWM(pinServo1, Frequency)
pwmServo2 = GPIO.PWM(pinServo2, Frequency)
pwmServo3 = GPIO.PWM(pinServo3, Frequency)
pwmServo4 = GPIO.PWM(pinServo4, Frequency)

pwmMotorAForwards.start(0)
pwmMotorABackwards.start(0)
pwmMotorBForwards.start(0)
pwmMotorBBackwards.start(0)
pwmMotorCForwards.start(0)
pwmMotorCBackwards.start(0)
pwmMotorDForwards.start(0)
pwmMotorDBackwards.start(0)

def Servo1(pwm):
	#if pwm > 0.2: pwm = 0.2
	#elif pwm < 0.1: pwm = 0.1
	pwmServo1.ChangeDutyCycle(100 * pwm)
	time.sleep(0.1)
	pwmServo1.ChangeDutyCycle(0)

def Servo1Angle(angle):
	if angle < -90: angle = -90
	if angle > 90: angle = 90
	angle = angle + 4
	pulse = 1.36 + (angle * (1.9 - 0.92)/90)
	pwm = (pulse/1000) / (0.02)
	Servo1(pwm)

def Servo2(pwm):
	#if pwm > 0.2: pwm = 0.2
	#elif pwm < 0.1: pwm = 0.1
	pwmServo2.ChangeDutyCycle(100 * pwm)
	time.sleep(0.1)
	pwmServo2.ChangeDutyCycle(0)

def Servo2Angle(angle):
	if angle < -90: angle = -90
	if angle > 90: angle = 90
	angle = angle + 1
	pulse = 1.36 + (angle * (1.9 - 0.92)/90)
	pwm = (pulse/1000) / (0.02)
	Servo2(pwm)

def Servo3(pwm):
	#if pwm > 0.2: pwm = 0.2
	#elif pwm < 0.1: pwm = 0.1
	pwmServo3.ChangeDutyCycle(100 * pwm)
	time.sleep(0.1)
	pwmServo3.ChangeDutyCycle(0)

def Servo3Angle(angle):
	if angle < -90: angle = -90
	if angle > 90: angle = 90
	angle = angle - 0 #13
	pulse = 1.36 + (angle * (1.9 - 0.92)/90)
	pwm = (pulse/1000) / (0.02)
	Servo3(pwm)

def Servo4(pwm):
	#if pwm > 0.2: pwm = 0.2
	#elif pwm < 0.1: pwm = 0.1
	pwmServo4.ChangeDutyCycle(100 * pwm)
	time.sleep(0.1)
	pwmServo4.ChangeDutyCycle(0)

def Servo4Angle(angle):
	if angle < -90: angle = -90
	if angle > 90: angle = 90
	angle = angle + 0
	pulse = 1.36 + (angle * (1.9 - 0.92)/90)
	pwm = (pulse/1000) / (0.02)
	Servo4(pwm)
		
pwmServo1.start(0)
Servo1Angle(0)
pwmServo2.start(0)
Servo2Angle(0)
pwmServo3.start(0)
Servo3Angle(0)
pwmServo4.start(0)
Servo4Angle(0)

def GetAngle_i(radius):

	if radius >= 100000: angle = 0
	elif radius >= 10000: angle = 0.288
	elif radius >= 5000: angle = 0.579
	elif radius >= 2000: angle = 1.469
	elif radius >= 1000: angle = 3.013
	elif radius >= 750: angle = 4.086
	elif radius >= 500: angle = 6.34
	elif radius >= 250: angle = 14
	elif radius >= 200: angle = 18
	elif radius >= 150: angle = 27
	else: angle = 45
	return angle
		
def GetAngle_o(radius):

	if radius >= 100000: angle = 0
	elif radius >= 10000: angle = 0.285
	elif radius >= 5000: angle = 0.567
	elif radius >= 2000: angle = 1.397
	elif radius >= 1000: angle = 2.73
	elif radius >= 750: angle = 3.58
	elif radius >= 500: angle = 5.19
	elif radius >= 250: angle = 9.46
	elif radius >= 200: angle = 11.3
	elif radius >= 150: angle = 14
	else: angle = 18
	return angle

def GetSpeed_i(radius):

	if radius >= 100000: speed = 1
	elif radius >= 10000: speed = 0.99
	elif radius >= 5000: speed = 0.98
	elif radius >= 2000: speed = 0.95
	elif radius >= 1000: speed = 0.905
	elif radius >= 750: speed = 0.876
	elif radius >= 500: speed = 0.820
	elif radius >= 250: speed = 0.678
	elif radius >= 200: speed = 0.620
	elif radius >= 150: speed = 0.542
	else: speed = 0.447
	return speed

def GetSpeed_o(radius):
	return 1


def HomePos():
	Servo1Angle(0)
	Servo2Angle(0)
	Servo3Angle(0)
	Servo4Angle(0)

	motors.Stop(pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards)

def Stop():

	motors.Stop(pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards)

def Backwards(Speed, duration=0):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0

	Servo1Angle(0)
	Servo2Angle(0)
	Servo3Angle(0)
	Servo4Angle(0)

	motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, 0)

def Forwards(Speed, duration=0):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0

	Servo1Angle(0)
	Servo2Angle(0)
	Servo3Angle(0)
	Servo4Angle(0)
	
	motors.Forwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, 0)

def FLeftR(Speed, duration, radius):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0

	Angle_i = GetAngle_i(radius)
	Angle_o = GetAngle_o(radius)
	Speed_i = GetSpeed_i(radius)
	Speed_o = GetSpeed_o(radius)
	
	Servo1Angle(Angle_i)
	Servo2Angle(Angle_o)
	Servo3Angle(-Angle_i)
	Servo4Angle(Angle_o)
	
	pwmMotorAForwards.ChangeDutyCycle(0)
	pwmMotorABackwards.ChangeDutyCycle(DCA * Speed * Speed_i)
	pwmMotorBForwards.ChangeDutyCycle(0)
	pwmMotorBBackwards.ChangeDutyCycle(DCB * Speed * Speed_o)
	pwmMotorCForwards.ChangeDutyCycle(0)
	pwmMotorCBackwards.ChangeDutyCycle(DCA * Speed * Speed_i)
	pwmMotorDForwards.ChangeDutyCycle(0)
	pwmMotorDBackwards.ChangeDutyCycle(DCB * Speed * Speed_o)

	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, 0)

def FRightR(Speed, duration, radius):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0

	Angle_i = GetAngle_i(radius)
	Angle_o = GetAngle_o(radius)
	Speed_i = GetSpeed_i(radius)
	Speed_o = GetSpeed_o(radius)
	
	Servo1Angle(-Angle_o)
	Servo2Angle(-Angle_i)
	Servo3Angle(Angle_o)
	Servo4Angle(-Angle_i)
	
	pwmMotorAForwards.ChangeDutyCycle(0)
	pwmMotorABackwards.ChangeDutyCycle(DCA * Speed * Speed_o)
	pwmMotorBForwards.ChangeDutyCycle(0)
	pwmMotorBBackwards.ChangeDutyCycle(DCB * Speed * Speed_i)
	pwmMotorCForwards.ChangeDutyCycle(0)
	pwmMotorCBackwards.ChangeDutyCycle(DCA * Speed * Speed_o)
	pwmMotorDForwards.ChangeDutyCycle(0)
	pwmMotorDBackwards.ChangeDutyCycle(DCB * Speed * Speed_i)

	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, 0)

def BLeftR(Speed, duration, radius):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0

	Angle_i = GetAngle_i(radius)
	Angle_o = GetAngle_o(radius)
	Speed_i = GetSpeed_i(radius)
	Speed_o = GetSpeed_o(radius)
	
	Servo1Angle(Angle_i)
	Servo2Angle(Angle_o)
	Servo3Angle(-Angle_i)
	Servo4Angle(Angle_o)
	
	pwmMotorAForwards.ChangeDutyCycle(DCA * Speed * Speed_i)
	pwmMotorABackwards.ChangeDutyCycle(0)
	pwmMotorBForwards.ChangeDutyCycle(DCB * Speed * Speed_o)
	pwmMotorBBackwards.ChangeDutyCycle(0)
	pwmMotorCForwards.ChangeDutyCycle(DCA * Speed * Speed_i)
	pwmMotorCBackwards.ChangeDutyCycle(0)
	pwmMotorDForwards.ChangeDutyCycle(DCB * Speed * Speed_o)
	pwmMotorDBackwards.ChangeDutyCycle(0)

	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, 0)

def BRightR(Speed, duration, radius):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0

	Angle_i = GetAngle_i(radius)
	Angle_o = GetAngle_o(radius)
	Speed_i = GetSpeed_i(radius)
	Speed_o = GetSpeed_o(radius)
	
	Servo1Angle(-Angle_o)
	Servo2Angle(-Angle_i)
	Servo3Angle(Angle_o)
	Servo4Angle(-Angle_i)
	
	pwmMotorAForwards.ChangeDutyCycle(DCA * Speed * Speed_o)
	pwmMotorABackwards.ChangeDutyCycle(0)
	pwmMotorBForwards.ChangeDutyCycle(DCB * Speed * Speed_i)
	pwmMotorBBackwards.ChangeDutyCycle(0)
	pwmMotorCForwards.ChangeDutyCycle(DCA * Speed * Speed_o)
	pwmMotorCBackwards.ChangeDutyCycle(0)
	pwmMotorDForwards.ChangeDutyCycle(DCB * Speed * Speed_i)
	pwmMotorDBackwards.ChangeDutyCycle(0)

	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, 0)

def SRight(Speed=1, duration=0):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0

	Servo1Angle(-45)
	Servo2Angle(45)
	Servo3Angle(45)
	Servo4Angle(45)
	
	motors.SpinRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, 0)

def BLeft(Speed=1, duration=0):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.BLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, 0)

def FLeft(Speed=1, duration=0):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.FLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, 0)

def SLeft(Speed=1, duration=0):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0

	Servo1Angle(-45)
	Servo2Angle(45)
	Servo3Angle(45)
	Servo4Angle(45)

	motors.SpinLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, 0)

def BRight(Speed=1, duration=0):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.BRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, 0)

def FRight(Speed=1, duration=0):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0
	motors.FRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, 0)

def SlideNE(Speed=1, duration=0):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0

	Servo1Angle(-45)
	Servo2Angle(-45)
	Servo3Angle(-45)
	Servo4Angle(45)
	
	motors.Forwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Stop(pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards)

def SlideNW(Speed=1, duration=0):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0

	Servo1Angle(45)
	Servo2Angle(45)
	Servo3Angle(45)
	Servo4Angle(-45)
	
	motors.Forwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Stop(pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards)

def SlideSE(Speed=1, duration=0):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0

	Servo1Angle(45)
	Servo2Angle(45)
	Servo3Angle(45)
	Servo4Angle(-45)
	
	motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Stop(pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards)

def SlideSW(Speed=1, duration=0):
	if Speed > 1: Speed = 1
	elif Speed < 0: Speed = 0

	Servo1Angle(-45)
	Servo2Angle(-45)
	Servo3Angle(-45)
	Servo4Angle(45)
	
	motors.Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed)
	if duration > 0:
		time.sleep(duration)
		motors.Stop(pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards)

