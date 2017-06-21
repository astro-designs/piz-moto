#!/usr/bin/env python2.7
# PiZ-Moto Motor Control Functions

# First some basic motor control functions to control each motor separately
# SpeedAndDirection can be a number between +100 & -100
# +100 or any value greater than zero spins the motor forwards
# -100 or any value less than zero spins the motor backwards
# 100 or -100 (100% duty-cycle) spins the motor at full speed
# 50 or -50 (50% duty-cycle) spins the motor at half speed

#Motor 1
def Motor1(SpeedAndDirection, pwmMotorAForwards, pwmMotorABackwards):

	if SpeedAndDirection > 100:
		SpeedAndDirection = 100
		
	if SpeedAndDirection < -100:
		SpeedAndDirection = -100
		
	if(SpeedAndDirection < 0):
		SpeedAndDirection = SpeedAndDirection * -1
		pwmMotorAForwards.ChangeDutyCycle(0)
		pwmMotorABackwards.ChangeDutyCycle(SpeedAndDirection)
	else: # Forwards...
		pwmMotorAForwards.ChangeDutyCycle(SpeedAndDirection)
		pwmMotorABackwards.ChangeDutyCycle(0)
	
#Motor 2
def Motor2(SpeedAndDirection, pwmMotorBForwards, pwmMotorBBackwards):

	if SpeedAndDirection > 100:
		SpeedAndDirection = 100
		
	if SpeedAndDirection < -100:
		SpeedAndDirection = -100
		
	if(SpeedAndDirection < 0): # Backwards...
		SpeedAndDirection = SpeedAndDirection * -1
		pwmMotorBForwards.ChangeDutyCycle(0)
		pwmMotorBBackwards.ChangeDutyCycle(SpeedAndDirection)
	else: # Forwards...
		pwmMotorBForwards.ChangeDutyCycle(SpeedAndDirection)
		pwmMotorBBackwards.ChangeDutyCycle(0)



# Next, some functions to control both motors for driving a two motor, two-wheeled robot...
		
# Function to turn all motors off
def Stop(pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards):

	#print("Stop")
	pwmMotorAForwards.ChangeDutyCycle(0)
	pwmMotorABackwards.ChangeDutyCycle(0)
	pwmMotorBForwards.ChangeDutyCycle(0)
	pwmMotorBBackwards.ChangeDutyCycle(0)
	
# Turn both motors backwards
def Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed):

	#print("Backwards")
	pwmMotorAForwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorABackwards.ChangeDutyCycle(0)
	pwmMotorBForwards.ChangeDutyCycle(DCB * Speed)
	pwmMotorBBackwards.ChangeDutyCycle(0)

# Turn both motors forwards
def Forwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed):
	
	#print("Forwards")
	pwmMotorAForwards.ChangeDutyCycle(0)
	pwmMotorABackwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorBForwards.ChangeDutyCycle(0)
	pwmMotorBBackwards.ChangeDutyCycle(DCB * Speed)
	
# Spin Right
def SpinRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed):
	
	#print("Spin Right")
	pwmMotorAForwards.ChangeDutyCycle(0)
	pwmMotorABackwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorBForwards.ChangeDutyCycle(DCB * Speed)
	pwmMotorBBackwards.ChangeDutyCycle(0)
	
def BLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed):
	
	#print("Back Left")
	pwmMotorAForwards.ChangeDutyCycle(DCA * Speed * 0.5)
	pwmMotorABackwards.ChangeDutyCycle(0)
	pwmMotorBForwards.ChangeDutyCycle(DCB * Speed)
	pwmMotorBBackwards.ChangeDutyCycle(0)
	
def FLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed):
	
	#print("Forwards Left")
	pwmMotorAForwards.ChangeDutyCycle(0)
	pwmMotorABackwards.ChangeDutyCycle(DCA * Speed * 0.5)
	pwmMotorBForwards.ChangeDutyCycle(0)
	pwmMotorBBackwards.ChangeDutyCycle(DCB * Speed)
	
# Spin left
def SpinLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed):
	
	#print("Spin Left")
	pwmMotorAForwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorABackwards.ChangeDutyCycle(0)
	pwmMotorBForwards.ChangeDutyCycle(0)
	pwmMotorBBackwards.ChangeDutyCycle(DCB * Speed)
	
def BRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed):
	
	#print("Back Right")
	pwmMotorAForwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorABackwards.ChangeDutyCycle(0)
	pwmMotorBForwards.ChangeDutyCycle(DCB * Speed * 0.5)
	pwmMotorBBackwards.ChangeDutyCycle(0)
	
def FRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, Speed):
	
	#print("Forwards Right")
	pwmMotorAForwards.ChangeDutyCycle(0)
	pwmMotorABackwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorBForwards.ChangeDutyCycle(0)
	pwmMotorBBackwards.ChangeDutyCycle(DCB * Speed * 0.5)
