#!/usr/bin/env python2.7
# CamJam EduKit 3 - Robotics
# MatchBot Control
# Line-follower
# Proximity
# Added Wii Remote Interface

import RPi.GPIO as GPIO # Import the GPIO Library
import pygame
import time
import os
import sys


# Set the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 7
pinMotorBBackwards = 8

# Set additional variables for second PiZ-Moto board
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

# pygame controller constants (Rock Candy Controller)
JoyButton_Square = 0
JoyButton_X = 1
JoyButton_Circle = 2
JoyButton_Triangle = 3
JoyButton_L1 = 4
JoyButton_R1 = 5
JoyButton_L2 = 6
JoyButton_R2 = 7
JoyButton_Select = 8
JoyButton_Start = 9
JoyButton_L3 = 10
JoyButton_R3 = 11
JoyButton_Home = 12
axisUpDown = 1                          # Joystick axis to read for up / down position
axisUpDownInverted = False              # Set this to True if up and down appear to be swapped
axisLeftRight = 0                       # Joystick axis to read for left / right position
axisLeftRightInverted = False           # Set this to True if left and right appear to be swapped

# pygame controller constants (ShanWan PC/PS3/Android)
JoyButton_A = 0
JoyButton_B = 1
JoyButton_X = 3
JoyButton_Y = 4
JoyButton_R1 = 7
JoyButton_L1 = 6
JoyButton_R2 = 9
JoyButton_L2 = 8
JoyButton_Select = 10
JoyButton_Start = 11
JoyButton_L3 = 13
JoyButton_R3 = 14
axisUpDown = 1                          # Joystick axis to read for up / down position
axisUpDownInverted = False              # Set this to True if up and down appear to be swapped
axisLeftRight = 0                       # Joystick axis to read for left / right position
axisLeftRightInverted = False           # Set this to True if left and right appear to be swapped
JoyButton_Circle = 999                  # Not supported on this controller
JoyButton_Home = 999                    # Not supported on this controller

interval = 0.00                         # Time between keyboard updates in seconds, smaller responds faster but uses more processor time


# Setup pygame and key states
global hadEvent
global LeftStickUp
global LeftStickDown
global LeftStickLeft
global LeftStickRight
global RightStickUp
global RightStickDown
global RightStickLeft
global RightStickRight
global HatStickUp
global HatStickDown
global HatStickLeft
global HatStickRight
global TriangleButton
global SquareButton
global CircleButton
global XButton
global HomeButton
global StartButton
global SelectButton
global R1Button
global R2Button
global R3Button
global L1Button
global L2Button
global L3Button
global moveQuit
hadEvent = True
LeftStickUp = False
LeftStickDown = False
LeftStickLeft = False
LeftStickRight = False
RightStickUp = False
RightStickDown = False
RightStickLeft = False
RightStickRight = False
HatStickUp = False
HatStickDown = False
HatStickLeft = False
HatStickRight = False
TriangleButton = False
SquareButton = False
CircleButton = False
XButton = False
HomeButton = False
StartButton = False
SelectButton = False
R1Button = False
R2Button = False
R3Button = False
L1Button = False
L2Button = False
L3Button = False
moveQuit = False

# Needed to allow PyGame to work without a monitor
os.environ["SDL_VIDEODRIVER"]= "dummy"

#Initialise pygame & controller(s)
pygame.init()
print 'Waiting for joystick... (press CTRL+C to abort)'
while True:
    try:
        try:
            pygame.joystick.init()
            # Attempt to setup the joystick
            if pygame.joystick.get_count() < 1:
                # No joystick attached, toggle the LED
                #ZB.SetLed(not ZB.GetLed())
                pygame.joystick.quit()
                time.sleep(0.1)
            else:
                # We have a joystick, attempt to initialise it!
                joystick = pygame.joystick.Joystick(0)
                break
        except pygame.error:
            # Failed to connect to the joystick, toggle the LED
            #ZB.SetLed(not ZB.GetLed())
            pygame.joystick.quit()
            time.sleep(0.1)
    except KeyboardInterrupt:
        # CTRL+C exit, give up
        print '\nUser aborted'
        #ZB.SetLed(True)
        sys.exit()
print 'Joystick found'
joystick.init()

print 'Initialised Joystick : %s' % joystick.get_name()

# Check number of joysticks in use...
joystick_count = pygame.joystick.get_count()
print("joystick_count")
print(joystick_count)
print("--------------")

# Check number of axes on joystick...
numaxes = joystick.get_numaxes()
print("numaxes")
print(numaxes)
print("--------------")

# Check number of buttons on joystick...
numbuttons = joystick.get_numbuttons()
print("numbuttons")
print(numbuttons)

# Pause for a moment...
time.sleep(2)


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
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)
    GPIO.output(pinLED1, True)
    GPIO.output(pinLED2, True)
    
    GPIO.output(pinMotorA1, True)
    GPIO.output(pinMotorA2, False)
    GPIO.output(pinMotorB1, True)
    GPIO.output(pinMotorB2, False)

# Turn Right
def Right():
    global TurnDC
    
    #print("Right")
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
    
    #print("Right")
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
    
    #print("Right")
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
    
    #print("Left")
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
    
    #print("Left")
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
    
    #print("Left")
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

def PygameHandler(events):
    # Variables accessible outside this function
    global hadEvent
    global LeftStickUp
    global LeftStickDown
    global LeftStickLeft
    global LeftStickRight
    global RightStickUp
    global RightStickDown
    global RightStickLeft
    global RightStickRight
    global HatStickUp
    global HatStickDown
    global HatStickLeft
    global HatStickRight
    global TriangleButton
    global SquareButton
    global CircleButton
    global XButton
    global HomeButton
    global StartButton
    global SelectButton
    global R1Button
    global R2Button
    global R3Button
    global L1Button
    global L2Button
    global L3Button
    global moveQuit

    # Handle each event individually
    for event in events:
        #print ("Event: ", event)
        if event.type == pygame.QUIT:
            print ("QUIT")
            # User exit
            hadEvent = True
            moveQuit = True
        elif event.type == pygame.JOYHATMOTION:
            # A key has been pressed, see if it is one we want
            hadEvent = True
            #print ("Hat Motion: ", event.value)
            hat = joystick.get_hat(0)
            # Hat up/down
            if hat[0] == -1:
                HatStickLeft = True
            elif hat[0] == 1:
                HatStickRight = True
            else:
                HatStickLeft = False
                HatStickRight = False
            # Hat left/right
            if hat[1] == -1:
                HatStickDown = True
            elif hat[1] == 1:
                HatStickUp = True
            else:
                HatStickDown = False
                HatStickUp = False
            
        elif event.type == pygame.JOYBUTTONDOWN:
            # A key has been pressed, see if it is one we want
            hadEvent = True
            print ("Button Down: ", event.button)
            if event.button == JoyButton_Square:
                SquareButton = True
            elif event.button == JoyButton_X:
                XButton = True
            elif event.button == JoyButton_Circle:
                CircleButton = True
            elif event.button == JoyButton_Triangle:
                TriangleButton = True
            elif event.button == JoyButton_L1:
                L1Button = True
            elif event.button == JoyButton_R1:
                R1Button = True
            elif event.button == JoyButton_L2:
                L2Button = True
            elif event.button == JoyButton_R2:
                R2Button = True
            elif event.button == JoyButton_L3:
                L3Button = True
            elif event.button == JoyButton_R3:
                R3Button = True
            elif event.button == JoyButton_Select:
                SelectButton = True
            elif event.button == JoyButton_Start:
                StartButton = True
            elif event.button == JoyButton_Home:
                HomeButton = True
        elif event.type == pygame.JOYBUTTONUP:
            # A key has been released, see if it is one we want
            hadEvent = True
            #print ("Button Up: ", event.button)
            if event.button == JoyButton_Square:
                SquareButton = False
            elif event.button == JoyButton_X:
                XButton = False
            elif event.button == JoyButton_Circle:
                CircleButton = False
            elif event.button == JoyButton_Triangle:
                TriangleButton = False
            elif event.button == JoyButton_L1:
                L1Button = False
            elif event.button == JoyButton_R1:
                R1Button = False
            elif event.button == JoyButton_L2:
                L2Button = False
            elif event.button == JoyButton_R2:
                R2Button = False
            elif event.button == JoyButton_L3:
                L3Button = False
            elif event.button == JoyButton_R3:
                R3Button = False
            elif event.button == JoyButton_Select:
                SelectButton = False
            elif event.button == JoyButton_Start:
                StartButton = False
            elif event.button == JoyButton_Home:
                HomeButton = False
        elif event.type == pygame.JOYAXISMOTION:
            # A joystick has been moved, read axis positions (-1 to +1)
            hadEvent = True
            upDown = joystick.get_axis(axisUpDown)
            leftRight = joystick.get_axis(axisLeftRight)
            # Invert any axes which are incorrect
            if axisUpDownInverted:
                upDown = -upDown
            if axisLeftRightInverted:
                leftRight = -leftRight
            # Determine Up / Down values
            if upDown < -0.1:
                print ("LeftStickUp")
                LeftStickUp = True
                LeftStickDown = False
            elif upDown > 0.1:
                print ("LeftStickDown")
                LeftStickUp = False
                LeftStickDown = True
            else:
                LeftStickUp = False
                LeftStickDown = False
            # Determine Left / Right values
            if leftRight < -0.1:
                print ("LeftStickLeft")
                LeftStickLeft = True
                LeftStickRight = False
            elif leftRight > 0.1:
                print ("LeftStickRight")
                LeftStickLeft = False
                LeftStickRight = True
            else:
                LeftStickLeft = False
                LeftStickRight = False

        
print("Starting PS3Bot - entering control loop...")

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
    print 'Press [ESC] to quit'
    # Loop indefinitely
    while True:
        # Get the currently pressed keys on the keyboard
        PygameHandler(pygame.event.get())
        if hadEvent:
            # Keys have changed, generate the command list based on keys
            hadEvent = False
            if moveQuit:
                break
            elif HomeButton and CircleButton: # Shutdown
                print ("Halting Raspberry Pi...")
                GPIO.cleanup()
                bashCommand = ("sudo halt")
                os.system(bashCommand)
                break
            elif HomeButton and XButton: # Exit
                break
            elif StartButton and CircleButton: 
                print ("Start Line-follower")
                #do_linefollower()
            elif StartButton and SquareButton: 
                print ("Start Proximity")
                #do_proximity()
            elif StartButton and XButton: 
                print ("Start Avoidance")
                #do_proximity()
            elif SelectButton:
                print ("Select")
            elif SquareButton:
                print ("Square")
            elif XButton:
                print ("X")
            elif CircleButton:
                print ("Circle")
            elif TriangleButton:
                print ("Triangle")
            elif L1Button:
                print ("L1")
            elif R1Button:
                print ("R1")
            elif L2Button:
                print ("L2")
            elif R2Button:
                print ("R2")
            elif L3Button:
                print ("L3")
            elif R3Button:
                print ("R3")
            elif LeftStickLeft:
                Left()
            elif LeftStickRight:
                Right()
            elif LeftStickUp:
                Forwards()
            elif LeftStickDown:
                Backwards()
            elif RightStickLeft:
                print ("Right Stick Left")
            elif RightStickRight:
                print ("Right Stick Right")
            elif RightStickUp:
                print ("Right Stick Up")
            elif RightStickDown:
                print ("Right Stick Down")
            elif HatStickLeft:
                print ("Hat Left")
            elif HatStickRight:
                print ("Hat Right")
            elif HatStickUp:
                print ("Hat Up")
            elif HatStickDown:
                print ("Hat Down")
            if not LeftStickLeft and not LeftStickRight and not LeftStickUp and not LeftStickDown:
                StopMotors()
        time.sleep(interval)
    # Disable all drives
    StopMotors()    
# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()
            
