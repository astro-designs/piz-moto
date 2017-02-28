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

__all__ = ['Stop', 'Forwards', 'Backwards', 'SpinLeft', 'SpinRight', 'FLeft', 'FRight', 'BLeft', 'BRight']

global pinMotorAForwards, pinMotorABackwards

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 7
pinMotorBBackwards = 8

# Set variables for the line detector GPIO pin
pinLineFollower = 25

#Global Direction variable - tracks the turn direction to speed up line seek
Direction = True

# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18

# Set variable for the LED pin
pinLED1 = 5
pinLED2 = 6

# Define a global variable to control limit initial acceleration
SpeedRamp = 0.5

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

# Set the pinLineFollower pin as an input so its value can be read
GPIO.setup(pinLineFollower, GPIO.IN)

# Set range sensor pins as output and input
GPIO.setup(pinTrigger, GPIO.OUT) # Trigger
GPIO.setup(pinEcho, GPIO.IN) # Echo

# Set trigger to False (Low)
GPIO.output(pinTrigger, False)

# Set the LED Pins mode to be Outputs
GPIO.setup(pinLED1, GPIO.OUT)
GPIO.setup(pinLED2, GPIO.OUT)

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

# Return True if the line detector is over a black line
def IsOverBlack():
	if GPIO.input(pinLineFollower) == 0:
		return True
	else:
		return False

# Search for the black line
def SeekLine():
	global Direction
	print("Seeking the line")
	# The direction the robot will turn - True = Left
	#Direction = True
	
	TurnSpeed = 0.3
	
	SeekSize = 0.3 # Turn for 0.25s
	SeekCount = 1 # A count of times the robot has looked for the line 
	MaxSeekCount = 5 # The maximum time to seek the line in one direction
	# Turn the robot left and right until it finds the line
	# Or it has been searched for long enough
	while SeekCount <= MaxSeekCount:
		# Set the seek time
		SeekTime = SeekSize * SeekCount
		
		# Start the motors turning in a direction
		if Direction:
			print("Looking left")
			SLeft(TurnSpeed, 0)
		else:
			print("Looking Right")
			SRight(TurnSpeed, 0)
		
		# Save the time it is now
		StartTime = time.time()
		
		# While the robot is turning for SeekTime seconds,
		# check to see whether the line detector is over black
		while time.time()-StartTime <= SeekTime:
			if IsOverBlack():
				Stop()
				# Exit the SeekLine() function returning
				# True - the line was found
				return True
				
		# The robot has not found the black line yet, so stop
		Stop()
		# Turn the LED off
		GPIO.output(pinLED1, False)

		
		# Increase the seek count
		SeekCount += 1
		
		# Change direction
		Direction = not Direction
		
	# The line wasn't found, so return False
	return False

def FollowLine():
	global SpeedRamp
	MaxSpeed = 0.4
	#repeat the next indented block forever
	print("Following the line")
	KeepTrying = True
	while KeepTrying == True:
		# If the sensor is Low (=0), it's above the black line
		if IsOverBlack():
			SpeedRamp = SpeedRamp + 0.01
			if SpeedRamp > MaxSpeed:
				SpeedRamp = MaxSpeed
			Forwards(SpeedRamp,0)
			#Forwards(0.5,0)
			time.sleep(0.2)
			# If not (else), print the following
		else:
			Stop()
			if SeekLine() == False:
				Stop()
				print("The robot has lost the line")
				KeepTrying = False
			else:
				print("Following the line")
	print("Exiting the line-following routine")
	Stop()

def MeasureDistance(NumReadings):

	FirstRun = 1
	Readings = 0
	Distance = 100
	
	while Readings < NumReadings:

		# Small delay to ensure read frequency never exceeds 40Hz
		time.sleep(0.050) #0.25

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
				print("Too far away to measure!")
				StopTime = StartTime
				break
		
		# Remember previous measurement for running average calculation
		if FirstRun == 0:
			OldDistance = Distance

		# Calculate pulse length
		ElapsedTime = StopTime - StartTime
		# Distance pulse travelled in that time is
		# time multiplied by the speed of sound (cm/s)
		Distance = ElapsedTime * 34326

		# That was the distance there and back so halve the value
		Distance = Distance / 2
		
		if FirstRun == 0:
			# Calculate running average
			Distance = Distance + OldDistance
			Distance = Distance / 2
		else:
			FirstRun = 0
			
		Readings = Readings + 1
		
	print("Distance : %.1f" % Distance)

	return Distance
	
def SeekPath():
	print("Seeking a clear path")
	# The direction the robot will turn - True = Left
	Direction = True
	
	TurnSpeed = 0.6
	
	SeekSize = 0.5 # Turn for 0.25s
	SeekCount = 1 # A count of times the robot has looked for a clear path 
	MaxSeekCount = 5 # The maximum time to seek a clear path in one direction
	# Turn the robot left and right until it finds a path
	# Or it has been searched for long enough
	while SeekCount <= MaxSeekCount:
		# Set the seek time
		SeekTime = SeekSize * SeekCount
		
		# Start the motors turning in a direction
		if Direction:
			print("Looking left")
			SLeft(TurnSpeed, 0)
		else:
			print("Looking Right")
			SRight(TurnSpeed, 0)
		
		# Save the time it is now
		SeekStartTime = time.time()
		
		# While the robot is turning for SeekTime seconds,
		# check to see whether the line detector is over black
		print("Seek Count",SeekCount)
		while time.time()-SeekStartTime <= SeekTime:
			print("Checking Distance")
			if MeasureDistance(2) > 30:
				Stop()
				print("Found a clear path")
				# Exit the SeekPath() function returning
				# True - a clear path was found
				return True
				
		# The robot has not found a clear path yet, so stop
		Stop()
		# Turn the LED off
		GPIO.output(pinLED1, False)

		
		# Increase the seek count
		SeekCount += 1
		
		# Change direction
		Direction = not Direction
		
	# A clear path wasn't found, so return False
	return False

def Avoidance():
	global SpeedRamp
	MaxSpeed = 0.4
	#repeat the next indented block forever
	print("Following the line")
	KeepTrying = True
	while KeepTrying == True:
		# If the sensor is Low (=0), it's above the black line
		if MeasureDistance(2) > 20:
			SpeedRamp = SpeedRamp + 0.01
			if SpeedRamp > MaxSpeed:
				SpeedRamp = MaxSpeed
			Forwards(SpeedRamp,0)
			#Forwards(0.5,0)
			time.sleep(0.2)
			# If not (else), print the following
		else:
			Stop()
			if SeekPath() == False:
				Stop()
				print("The robot has lost the line")
				KeepTrying = False
			else:
				print("Following the line")
	print("Exiting the line-following routine")
	Stop()
