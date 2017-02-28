#!/usr/bin/env python2.7
# PiZ-Moto Motor Control Functions

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
