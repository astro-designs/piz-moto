#!/usr/bin/env python2.7
# CamJam EduKit 3 - Robotics
# MatchBot Control
# Line-follower
# Proximity
# Added Wii Remote Interface

import RPi.GPIO as GPIO # Import the GPIO Library
import cwiid
import time
import os


# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 7
pinMotorBBackwards = 8

# Set additional variables to support L293D bodge
pinMotorA1 = 4
pinMotorA2 = 27
pinMotorB2 = 22
pinMotorB1 = 23

# Set variables for the line detector GPIO pin
pinLineFollower = 25

# Define GPIO pins to use on the Pi
pinTrigger = 17
pinEcho = 18

# Set variable for the LED pin
pinLED1 = 5
pinLED2 = 6

# How many times to turn the pin on and off each second
Frequency = 20
# How long the pin stays on each cycle, as a percent
DutyCycleA = 100
DutyCycleB = 100
# Setting the duty cycle to 0 means the motors will not turn
Stop = 0

# Define a global variable to define a slower speed for turning
TurnDC = 0.4

# Define a global variable to control limit initial acceleration
SpeedRamp = 0.5

# Set the GPIO Pin mode to be Output
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

GPIO.setup(pinMotorA1, GPIO.OUT)
GPIO.setup(pinMotorA2, GPIO.OUT)
GPIO.setup(pinMotorB1, GPIO.OUT)
GPIO.setup(pinMotorB2, GPIO.OUT)

GPIO.output(pinMotorA1, False)
GPIO.output(pinMotorA2, False)
GPIO.output(pinMotorB1, False)
GPIO.output(pinMotorB2, False)

# Set the pinLineFollower pin as an input so its value can be read
GPIO.setup(pinLineFollower, GPIO.IN)

# Turn all motors off
def StopMotors():
	global SpeedRamp

	SpeedRamp = 0.5

	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
	GPIO.output(pinLED1, False)
	GPIO.output(pinLED2, False)

	GPIO.output(pinMotorA1, False)
	GPIO.output(pinMotorA2, False)
	GPIO.output(pinMotorB1, False)
	GPIO.output(pinMotorB2, False)
	
# Turn both motors backwards
def Backwards():
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
	GPIO.output(pinLED1, False)
	GPIO.output(pinLED2, False)
	
	GPIO.output(pinMotorA1, False)
	GPIO.output(pinMotorA2, True)
	GPIO.output(pinMotorB1, False)
	GPIO.output(pinMotorB2, True)

# Turn both motors forwards
def Forwards():
	global SpeedRamp
	
	#SpeedStep = 0.1

	#while SpeedAB < 1:
		#SpeedAB = SpeedAB + SpeedStep
		#if SpeedAB > 1:
		#	SpeedAB = 1
		#	print("Speed", SpeedAB)

	#pwmMotorAForwards.ChangeDutyCycle(Stop)
	#pwmMotorABackwards.ChangeDutyCycle(DutyCycleA * SpeedRamp)
	#pwmMotorBForwards.ChangeDutyCycle(Stop)
	#pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB * SpeedRamp)
	#time.sleep(0.5)
	#SpeedRamp = 1
	
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA * SpeedRamp)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB * SpeedRamp)
	GPIO.output(pinLED1, True)
	GPIO.output(pinLED2, True)
	
	GPIO.output(pinMotorA1, True)
	GPIO.output(pinMotorA2, False)
	GPIO.output(pinMotorB1, True)
	GPIO.output(pinMotorB2, False)

# Turn Right
def Right():
	global TurnDC
	
	print("Right")
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA * TurnDC)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB * TurnDC)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
	GPIO.output(pinLED1, True)
	GPIO.output(pinLED2, False)
	
	GPIO.output(pinMotorA1, True)
	GPIO.output(pinMotorA2, False)
	GPIO.output(pinMotorB1, False)
	GPIO.output(pinMotorB2, True)

def BLeft():
	global TurnDC
	
	print("Right")
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA * TurnDC)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
	GPIO.output(pinLED1, True)
	
	GPIO.output(pinMotorA1, True)
	GPIO.output(pinMotorA2, False)
	GPIO.output(pinMotorB1, False)
	GPIO.output(pinMotorB2, True)

def FLeft():
	global TurnDC
	
	print("Right")
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA * TurnDC)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
	GPIO.output(pinLED1, True)
	
	GPIO.output(pinMotorA1, True)
	GPIO.output(pinMotorA2, False)
	GPIO.output(pinMotorB1, False)
	GPIO.output(pinMotorB2, True)

# Turn left
def Left():
	global TurnDC
	
	print("Left")
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA * TurnDC)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB * TurnDC)
	GPIO.output(pinLED1, False)
	GPIO.output(pinLED2, True)
	
	GPIO.output(pinMotorA1, False)
	GPIO.output(pinMotorA2, True)
	GPIO.output(pinMotorB1, True)
	GPIO.output(pinMotorB2, False)

def BRight():
	global TurnDC
	
	print("Left")
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB * TurnDC)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
	GPIO.output(pinLED1, False)
	
	GPIO.output(pinMotorA1, False)
	GPIO.output(pinMotorA2, True)
	GPIO.output(pinMotorB1, True)
	GPIO.output(pinMotorB2, False)

def FRight():
	global TurnDC
	
	print("Left")
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB * TurnDC)
	GPIO.output(pinLED1, False)
	
	GPIO.output(pinMotorA1, False)
	GPIO.output(pinMotorA2, True)
	GPIO.output(pinMotorB1, True)
	GPIO.output(pinMotorB2, False)

# Return True if the line detector is over a black line
def IsOverBlack():
	if GPIO.input(pinLineFollower) == 0:
		return True
	else:
		return False

# Search for the black line
def SeekLine():
	print("Seeking the line")
	# The direction the robot will turn - True = Left
	Direction = True
	
	SeekSize = 0.25 # Turn for 0.25s
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
			Left()
		else:
			print("Looking Right")
			Right()
		
		# Save the time it is now
		StartTime = time.time()
		
		# While the robot is turning for SeekTime seconds,
		# check to see whether the line detector is over black
		while time.time()-StartTime <= SeekTime:
			if IsOverBlack():
				StopMotors()
				# Exit the SeekLine() function returning
				# True - the line was found
				return True
				
		# The robot has not found the black line yet, so stop
		StopMotors()
		# Turn the LED off
		GPIO.output(pinLED1, False)

		
		# Increase the seek count
		SeekCount += 1
		
		# Change direction
		Direction = not Direction
		
	# The line wasn't found, so return False
	return False


def do_linefollower():
	global SpeedRamp

	#repeat the next indented block forever
	print("Following the line")
	KeepTrying = True
	while KeepTrying == True:
		# If the sensor is Low (=0), it's above the black line
		if IsOverBlack():
			SpeedRamp = SpeedRamp + 0.05
			if SpeedRamp > 1:
				SpeedRamp = 1
			Forwards()
			time.sleep(0.2)
			# If not (else), print the following
		else:
			StopMotors()
			if SeekLine() == False:
				StopMotors()
				print("The robot has lost the line")
				KeepTrying = False
			else:
				print("Following the line")
	print("Exiting the line-following routine")
	StopMotors()


def do_proximity():
	print("Looking for a wall...")
	#Initialise Distance variable for first average calculation
	Distance = 100
	
	# Repeat the next indented block forever
	while Distance > 2.7:

		# Start going forwards...
		Forwards()
	
		# Small delay to ensure read frequency never exceeds 40Hz
		time.sleep(0.025)

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
		OldDistance = Distance

		# Calculate pulse length
		ElapsedTime = StopTime - StartTime
		# Distance pulse travelled in that time is
		# time multiplied by the speed of sound (cm/s)
		Distance = ElapsedTime * 34326
		
		# That was the distance there and back so halve the value
		Distance = Distance / 2
		
		# Calculate running average
		Distance = Distance + OldDistance
		Distance = Distance / 2
		
		print("Distance : %.1f" % Distance)

	# Exit while loop
	StopMotors()


def do_WiiRemote():
	global speed, SpeedRamp, DutyCycleA, DutyCycleB

	#connecting to the wiimote. This allows several attempts
	# as first few often fail.
	print 'Press 1+2 on your Wiimote now...'
	GPIO.output(pinLED2, True)
	GPIO.output(pinLED1, True)
	wm = None
	i=1
	while not wm:
		
		try:
			#FlashCount = 20
			#while FlashCount > 0:
				# Turn the LED on
			#	GPIO.output(pinLED1, True)
			#	time.sleep(0.1)
			#	GPIO.output(pinLED1, False)
			#	time.sleep(0.1)
			#	FlashCount = FlashCount - 1
			for x in range(0,i):
				GPIO.output(pinLED1, False)
				time.sleep(0.5)
				GPIO.output(pinLED1, True)
				time.sleep(0.5)
			GPIO.output(pinLED1,False)
			print "Bluetooth pairing attempt " + str(i)

			wm=cwiid.Wiimote()
		except RuntimeError:
			if (i>10):
				print("cannot create connection")
				quit()
			print "Error opening wiimote connection"
			i +=1

	GPIO.output(pinLED1, True)
	GPIO.output(pinLED2, True)

	#set wiimote to report button presses and accelerometer state
	wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC

	#turn on led to show connected
	wm.led = 1

	buttons = wm.state['buttons']
	speed = 100
	DutyCycleA = speed
	DutyCycleB = speed
	moving = False

	while not(buttons == 140):
		buttons = wm.state['buttons']
		print("Buttons: " + str(buttons))
		if (buttons == 13): # Halt
			wm.led = 2
			print ("Halting Raspberry Pi...")
			GPIO.cleanup()
			bashCommand = ("sudo halt")
			print "echo:"+bashCommand
			os.system(bashCommand)
		elif (buttons == 6): # B + 1: LineFollower
			print("Starting Line-follower")
			do_linefollower()
		elif (buttons == 5): # B + 2: Proximity
			print("Starting Line-follower")
			do_proximity()
		elif (buttons & cwiid.BTN_1):
			print("BTN_1")
		elif (buttons & cwiid.BTN_2):
			print("BTN_2")
		elif (buttons & cwiid.BTN_A): # Shoot!!! :o)
			print("BTN_A")
			StopMotors()
		elif (buttons & cwiid.BTN_B): # Fire Missile!!! :o) 
			print("BTN_B")
		elif (buttons == 2048): # Forwards
			print("BTN_UP")
			#wm.led = 2
			SpeedRamp = SpeedRamp + 0.05
			if SpeedRamp > 1:
				SpeedRamp = 1
			Forwards()
			moving = True
		elif (buttons == 1024): # Backwards
			print("BTN_DOWN")
			#wm.led = 4
			Backwards()
			moving = True
		elif (buttons == 256): # Left
			print("BTN_LEFT")
			#wm.led = 8
			Left()
			moving = True
		elif (buttons == 512): # Right
			print("BTN_RIGHT")
			#wm.led = 15
			Right()
			moving = True
		elif (buttons == 2560): # FRight 2048 + 512
			FRight()
			moving = True
		elif (buttons == 2304): # FLeft 2048 + 256
			FLeft()
			moving = True
		elif (buttons == 1536): # BRight 1024 + 512
			BRight()
			moving = True
		elif (buttons == 1280): # BLeft 1024 + 256
			BLeft()
			moving = True
		elif (buttons & cwiid.BTN_PLUS): # Speed-up
			print("BTN_PLUS")
			if speed <= 90:
				speed = speed + 10
			else:
				speed = 100
			print("Speed: " + str(speed))
			DutyCycleA = speed
			DutyCycleB = speed
		elif (buttons & cwiid.BTN_MINUS): # Slow-down
			print("BTN_MINUS")
			if speed >= 10:
				speed = speed - 10
			else:
				speed = 0
			print("Speed: " + str(speed))
			DutyCycleA = speed
			DutyCycleB = speed
		elif (buttons & cwiid.NUNCHUK_BTN_C): # 
			print("NUNCHUK_BTN_C")
		elif (buttons & cwiid.NUNCHUK_BTN_Z): # 
			print("NUNCHUK_BTN_Z")
		else:
			print("Nothing...")
			if moving == True:
				moving = False
				StopMotors()

		time.sleep(0.2)

	GPIO.cleanup()

		
print("MatchBot - entering control loop...")

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

# Set pins as output and input
GPIO.setup(pinTrigger, GPIO.OUT) # Trigger
GPIO.setup(pinEcho, GPIO.IN) # Echo

# Set the LED Pin mode to be Output
GPIO.setup(pinLED1, GPIO.OUT)
GPIO.setup(pinLED2, GPIO.OUT)

# Set trigger to False (Low)
GPIO.output(pinTrigger, False)
		
# Allow module to settle
time.sleep(0.5)


try:
	#Initialise Distance variable for first average calculation
	Distance = 100
	
	# Repeat the next indented block forever
	while False:

		# Small delay to ensure read frequency never exceeds 40Hz
		time.sleep(0.025)

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
		OldDistance = Distance

		# Calculate pulse length
		ElapsedTime = StopTime - StartTime
		# Distance pulse travelled in that time is
		# time multiplied by the speed of sound (cm/s)
		Distance = ElapsedTime * 34326
		
		# That was the distance there and back so halve the value
		Distance = Distance / 2
		
		# Calculate running average
		#Distance = Distance + OldDistance
		#Distance = Distance / 2
		
		print("Distance : %.1f" % Distance)
		if Distance < 5:
			#Do Nothing
			FlashCount = 100
		elif Distance < 10:
			#Halt
			FlashCount = 0
			print ("Halt")
			if not IsOverBlack():
				print ("Halting Raspberry Pi...")
				bashCommand = ("sudo halt")
				print "echo:"+bashCommand
				os.system(bashCommand)
		elif Distance < 15:
			#Exit
			FlashCount = 5
			print ("Exit")
			if not IsOverBlack():
				print ("Exiting Control Program...")
				GPIO.cleanup()
				raise SystemExit
		elif Distance < 20:
			#Wii Remote
			FlashCount = 4
			print ("Run Wii Controller")
			if not IsOverBlack():
				print ("Calling Wii Controller Routine...")
				do_WiiRemote()
		elif Distance < 25:
			#Proximity
			FlashCount = 3
			print ("Run Proximity")
			if not IsOverBlack():
				print ("Calling Proximity Routine...")
				do_proximity()
		elif Distance < 30:
			#LineFollower
			FlashCount = 2
			print ("Run Line-Follower")
			if not IsOverBlack():
				print ("Calling Line-Follower Routine...")
				do_linefollower()
		else:
			FlashCount = 1
			print ("Please select function...")
		
		if FlashCount == 0:
			GPIO.output(pinLED1, True)
		elif FlashCount == 100:
			GPIO.output(pinLED1, False)
		else:
			while FlashCount > 0:
				# Turn the LED on
				GPIO.output(pinLED1, True)
				time.sleep(0.1)
				GPIO.output(pinLED1, False)
				time.sleep(0.1)
				FlashCount = FlashCount - 1

		time.sleep(0.5)

	do_WiiRemote()
	
# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
	# Reset GPIO settings
	GPIO.cleanup()
			
