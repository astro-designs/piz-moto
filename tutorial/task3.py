#!/usr/bin/env python2.7
# PiZ-Moto tutorial task #1
# A program to make a two wheeled robot travel forwards for 5 seconds
# and then travel backwards for 5 seconds

# Import the piz-moto package
import piz_moto
import time

# Initialise the speed, setting it to zero for the acceleration function
speed = 0

# Move forwards...
# Note that one motor must spin in the opposite direction to the other
# because it's on the opposite side of the robot
print("First we're accelerating forwards over 5 seconds...")
while speed <100:
	piz_moto.Motor1(speed)
	piz_moto.Motor2(speed * -1)
	speed = speed + 20
	time.sleep(1)

# wait 5 seconds
time.sleep(5)

# Turn left...
# Here we make one wheel turn one way as if the robot was moving forwards and 
# make the other wheel turn the opposite way as if the robot was moving backwards.
# Make the left wheel run backwards and the right wheel run forwards should
# make the robot spin to the left (or anti-clockwise)
# But don't forget that the motors are on opposite sides...
print("Now we're turning left...")
piz_moto.Motor1(100)
piz_moto.Motor2(100)

# wait 1 seconds
time.sleep(1)

# Move backwards...
# Note that one motor must spin in the opposite direction to the other
# because it's on the opposite side of the robot
print("Now we're moving backwards...")
piz_moto.Motor1(-100)
piz_moto.Motor2(100)

# wait 5 seconds
time.sleep(5)

# This is the really important bit - we need to stop the motors when finished...
piz_moto.Motor1(0)
piz_moto.Motor2(0)

# Important delay - for some reason if this delay isn't here
# the motors don't stop.
# I suspect the program needs a cleaner exit
time.sleep(1)




