#!/usr/bin/env python2.7
# PiZ-Moto Motor Control Functions

import RPi.GPIO as GPIO # Import the GPIO Library
import time

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 7
pinMotorBBackwards = 8

# How many times to turn the pin on and off each second
Frequency = 20

# How long the pin stays on each cycle, as a percent
DutyCycleA = 100
DutyCycleB = 100

# Setting the duty cycle to 0 means the motors will not turn
Stop = 0

# Function to turn all motors off
def Stop():

	#print("Stop")
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
	
# Turn both motors backwards
def Backwards(Speed):

	#print("Backwards")
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA * Speed)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB * Speed)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors forwards
def Forwards(Speed):
	
	#print("Forwards")
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA * Speed)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB * Speed)
	
# Spin Right
def SpinRight(Speed):
	
	#print("Spin Right")
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA * Speed)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB * Speed)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
	
def BLeft(Speed):
	
	#print("Back Left")
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA * Speed * 0.5)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB * Speed)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
	
def FLeft(Speed):
	
	#print("Forwards Left")
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA * Speed * 0.5)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB * Speed)
	
# Spin left
def SpinLeft(Speed):
	
	#print("Spin Left")
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA * Speed)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB * Speed)
	
def BRight(Speed):
	
	#print("Back Right")
	pwmMotorAForwards.ChangeDutyCycle(DutyCycleA * Speed)
	pwmMotorABackwards.ChangeDutyCycle(Stop)
	pwmMotorBForwards.ChangeDutyCycle(DutyCycleB * Speed * 0.5)
	pwmMotorBBackwards.ChangeDutyCycle(Stop)
	
def FRight(Speed):
	
	#print("Forwards Right")
	pwmMotorAForwards.ChangeDutyCycle(Stop)
	pwmMotorABackwards.ChangeDutyCycle(DutyCycleA * Speed)
	pwmMotorBForwards.ChangeDutyCycle(Stop)
	pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB * Speed * 0.5)
