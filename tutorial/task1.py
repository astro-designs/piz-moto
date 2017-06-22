#!/usr/bin/env python2.7
# PiZ-Moto tutorial task #1
# A program to make a two wheeled robot travel forwards for 5 seconds
# and then travel backwards for 5 seconds

# Import the piz-moto package
import piz_moto
import time


# Move forwards...
# Note that one motor must spin in the opposite direction to the other
# because it's on the opposite side of the robot
print("First we're moving forwards...")
piz_moto.Motor1(100)
piz_moto.Motor2(-100)

# wait 5 seconds
time.sleep(5)

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




