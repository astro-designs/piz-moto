#!/usr/bin/env python2.7
# PiZ-Moto Motor Control Functions

# Function to turn all motors off
def Stop(pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards ):

	#print("Stop")
	pwmMotorAForwards.ChangeDutyCycle(0)
	pwmMotorABackwards.ChangeDutyCycle(0)
	pwmMotorBForwards.ChangeDutyCycle(0)
	pwmMotorBBackwards.ChangeDutyCycle(0)
	pwmMotorCForwards.ChangeDutyCycle(0)
	pwmMotorCBackwards.ChangeDutyCycle(0)
	pwmMotorDForwards.ChangeDutyCycle(0)
	pwmMotorDBackwards.ChangeDutyCycle(0)
	
# Turn both motors backwards
def Backwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed):

	#print("Backwards")
	pwmMotorAForwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorABackwards.ChangeDutyCycle(0)
	pwmMotorBForwards.ChangeDutyCycle(DCB * Speed)
	pwmMotorBBackwards.ChangeDutyCycle(0)
	pwmMotorCForwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorCBackwards.ChangeDutyCycle(0)
	pwmMotorDForwards.ChangeDutyCycle(DCB * Speed)
	pwmMotorDBackwards.ChangeDutyCycle(0)

# Turn both motors forwards
def Forwards(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed):
	
	#print("Forwards")
	pwmMotorAForwards.ChangeDutyCycle(0)
	pwmMotorABackwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorBForwards.ChangeDutyCycle(0)
	pwmMotorBBackwards.ChangeDutyCycle(DCB * Speed)
	pwmMotorCForwards.ChangeDutyCycle(0)
	pwmMotorCBackwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorDForwards.ChangeDutyCycle(0)
	pwmMotorDBackwards.ChangeDutyCycle(DCB * Speed)
	
# Spin Right
def SpinRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed):
	
	#print("Spin Right")
	pwmMotorAForwards.ChangeDutyCycle(0)
	pwmMotorABackwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorBForwards.ChangeDutyCycle(DCB * Speed)
	pwmMotorBBackwards.ChangeDutyCycle(0)
	pwmMotorCForwards.ChangeDutyCycle(0)
	pwmMotorCBackwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorDForwards.ChangeDutyCycle(DCB * Speed)
	pwmMotorDBackwards.ChangeDutyCycle(0)
	
def BLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed):
	
	#print("Back Left")
	pwmMotorAForwards.ChangeDutyCycle(DCA * Speed * 0.5)
	pwmMotorABackwards.ChangeDutyCycle(0)
	pwmMotorBForwards.ChangeDutyCycle(DCB * Speed)
	pwmMotorBBackwards.ChangeDutyCycle(0)
	pwmMotorCForwards.ChangeDutyCycle(DCA * Speed * 0.5)
	pwmMotorCBackwards.ChangeDutyCycle(0)
	pwmMotorDForwards.ChangeDutyCycle(DCB * Speed)
	pwmMotorDBackwards.ChangeDutyCycle(0)
	
def FLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed):
	
	#print("Forwards Left")
	pwmMotorAForwards.ChangeDutyCycle(0)
	pwmMotorABackwards.ChangeDutyCycle(DCA * Speed * 0.5)
	pwmMotorBForwards.ChangeDutyCycle(0)
	pwmMotorBBackwards.ChangeDutyCycle(DCB * Speed)
	pwmMotorCForwards.ChangeDutyCycle(0)
	pwmMotorCBackwards.ChangeDutyCycle(DCA * Speed * 0.5)
	pwmMotorDForwards.ChangeDutyCycle(0)
	pwmMotorDBackwards.ChangeDutyCycle(DCB * Speed)
	
# Spin left
def SpinLeft(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed):
	
	#print("Spin Left")
	pwmMotorAForwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorABackwards.ChangeDutyCycle(0)
	pwmMotorBForwards.ChangeDutyCycle(0)
	pwmMotorBBackwards.ChangeDutyCycle(DCB * Speed)
	pwmMotorCForwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorCBackwards.ChangeDutyCycle(0)
	pwmMotorDForwards.ChangeDutyCycle(0)
	pwmMotorDBackwards.ChangeDutyCycle(DCB * Speed)
	
def BRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed):
	
	#print("Back Right")
	pwmMotorAForwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorABackwards.ChangeDutyCycle(0)
	pwmMotorBForwards.ChangeDutyCycle(DCB * Speed * 0.5)
	pwmMotorBBackwards.ChangeDutyCycle(0)
	pwmMotorCForwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorCBackwards.ChangeDutyCycle(0)
	pwmMotorDForwards.ChangeDutyCycle(DCB * Speed * 0.5)
	pwmMotorDBackwards.ChangeDutyCycle(0)
	
def FRight(DCA, DCB, pwmMotorAForwards, pwmMotorABackwards, pwmMotorBForwards, pwmMotorBBackwards, pwmMotorCForwards, pwmMotorCBackwards, pwmMotorDForwards, pwmMotorDBackwards, Speed):
	
	#print("Forwards Right")
	pwmMotorAForwards.ChangeDutyCycle(0)
	pwmMotorABackwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorBForwards.ChangeDutyCycle(0)
	pwmMotorBBackwards.ChangeDutyCycle(DCB * Speed * 0.5)
	pwmMotorCForwards.ChangeDutyCycle(0)
	pwmMotorCBackwards.ChangeDutyCycle(DCA * Speed)
	pwmMotorDForwards.ChangeDutyCycle(0)
	pwmMotorDBackwards.ChangeDutyCycle(DCB * Speed * 0.5)
