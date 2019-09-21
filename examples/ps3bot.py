#!/usr/bin/env python2.7
# A program to control a two wheeled robot using a wireless PS3 controller
# Compatible with CamJam EduKit 3 - Robotics
# Line-follower example
# Proximity sensor example

# Note LED flashes to indicate status
# 2 short flashes: Starting
# 3 short flashes: Joystick found
# 4 short flashes: Setting up joystick
# 5 short flashes: Starting control loop
# 10 short flashes: Exiting program
# 10 rapid flashes: Shutting down


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

# Set additional variables for optional second motor controller board
# Note: Not present on the Edukit3
pinMotorCForwards = 4
pinMotorCBackwards = 27
pinMotorDForwards = 22
pinMotorDBackwards = 23

# Options to switch motors around...
# In case wires get swapped...
# Work in progress, not yet working
SwapMotors = False
ReverseLeftMotor = False
ReverseRightMotor = False

# Set variables for the line detector GPIO pin
# Edukit3 compatible
pinLineFollower = 25

# Set variable for the proximity sensor interface
# Edukit3 compatible
pinTrigger = 17
pinEcho = 18

# Set variable for the LED pin
# Note: Not present on the Edukit3
pinLED1 = 5
pinLED2 = 6

# How many times to turn the pin on and off each second
Frequency = 50
# How long the pin stays on each cycle, as a percent
DutyCycleA = 100
DutyCycleB = 100
# Setting the duty cycle to 0 means the motors will not turn
Stop = 0

# Define a global variable to define a slower speed for turning
TurnDC = 0.5

# Set the GPIO Pin mode for the motor controls to be Output
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Set the GPIO Pin mode for the LED controls to be Output
GPIO.setup(pinLED1, GPIO.OUT)
GPIO.setup(pinLED2, GPIO.OUT)

# Set the pinLineFollower pin as an input so its value can be read
GPIO.setup(pinLineFollower, GPIO.IN)

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
global YButton
global AButton
global BButton
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
YButton = False
AButton = False
BButton = False
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

global stick
stick = "Left"

# Flash the LEDs
def FlashLEDs(flashes = 1, delay = 0.25, pause = 1.00):

    for flash in range(0, flashes):
        GPIO.output(pinLED1, True)
        GPIO.output(pinLED2, True)
        time.sleep(delay)
        GPIO.output(pinLED1, False)
        GPIO.output(pinLED2, False)
        time.sleep(delay)

    time.sleep(pause)

# Flash LED twice to indicate program has started
FlashLEDs(2,0.5, 1.00)
print ("Starting...")

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
                # No joystick attached
                pygame.joystick.quit()
                time.sleep(0.1)
            else:
                # We have a joystick, attempt to initialise it!
                joystick = pygame.joystick.Joystick(0)
                break
        except pygame.error:
            # Failed to connect to the joystick
            pygame.joystick.quit()
            time.sleep(0.1)
    except KeyboardInterrupt:
        # CTRL+C exit, give up
        print '\nUser aborted'
        FlashLEDs(10,0.5,1.0)
        sys.exit()
		
# Flash LED three times to indicate joystick found
FlashLEDs(3,0.5, 1.00)
print ("Joystick found")
joystick.init()

print 'Initialised Joystick : %s' % joystick.get_name()

if "Rock Candy" in joystick.get_name():
    FlashLEDs(4,0.5, 1.00)
    print ("Found Rock Candy Wireless PS3 controller")
    # pygame controller constants (Rock Candy Controller)
    JoyButton_Square = 0
    JoyButton_Circle = 2
    JoyButton_Triangle = 3
    JoyButton_X = 1
    JoyButton_Y = 999                       # Not supported on this controller
    JoyButton_A = 999                       # Not supported on this controller
    JoyButton_B = 999                       # Not supported on this controller
    JoyButton_L1 = 4
    JoyButton_R1 = 5
    JoyButton_L2 = 6
    JoyButton_R2 = 7
    JoyButton_L3 = 10
    JoyButton_R3 = 11
    JoyButton_Select = 8
    JoyButton_Start = 9
    JoyButton_Analog = 999                  # Not supported on this controller
    JoyButton_Home = 12
    axisUpDown = 1                          # Joystick axis to read for up / down position
    RightaxisUpDown = 3                     # Joystick axis to read for up / down position
    axisUpDownInverted = False              # Set this to True if up and down appear to be swapped
    axisLeftRight = 0                       # Joystick axis to read for left / right position
    RightaxisLeftRight = 2                  # Joystick axis to read for left / right position
    axisLeftRightInverted = False           # Set this to True if left and right appear to be swapped
    axisPosThreshold = 0.7                  # Controls the sensitivity of the joystick
    axisNegThreshold = -0.7                 # Controls the sensitivity of the joystick

elif "ShanWan" in joystick.get_name():
    FlashLEDs(4,0.5, 1.00)
    print ("Found ShanWan PS3 controller clone")
    # pygame controller constants (ShanWan PC/PS3/Android)
    JoyButton_Square = 999                  # Not supported on this controller
    JoyButton_Circle = 999                  # Not supported on this controller
    JoyButton_Triangle = 999                # Not supported on this controller
    JoyButton_A = 0
    JoyButton_B = 1
    JoyButton_X = 3
    JoyButton_Y = 4
    JoyButton_R1 = 7
    JoyButton_L1 = 6
    JoyButton_R2 = 9
    JoyButton_L2 = 8
    JoyButton_L3 = 13
    JoyButton_R3 = 14
    JoyButton_Select = 10
    JoyButton_Start = 11
    JoyButton_Analog = 999                  # Not supported on this controller
    JoyButton_Home = 999                    # Not supported on this controller
    axisUpDown = 1                          # Joystick axis to read for up / down position
    RightaxisUpDown = 3                     # Joystick axis to read for up / down position
    axisUpDownInverted = False              # Set this to True if up and down appear to be swapped
    axisLeftRight = 0                       # Joystick axis to read for left / right position
    RightaxisLeftRight = 2                  # Joystick axis to read for left / right position
    axisLeftRightInverted = False           # Set this to True if left and right appear to be swapped
    axisPosThreshold = 0.7                  # Controls the sensitivity of the joystick
    axisNegThreshold = -0.7                 # Controls the sensitivity of the joystick

elif "hongjingda" in joystick.get_name():
    FlashLEDs(4,0.5, 1.00)
    print ("Found PiHut PS3 controller clone")
    # pygame controller constants (hongjingda HJD-X)
    JoyButton_Square = 3
    JoyButton_Circle = 1
    JoyButton_Triangle = 4
    JoyButton_X = 0
    JoyButton_A = 999                       # Not supported on this controller
    JoyButton_B = 999                       # Not supported on this controller
    JoyButton_Y = 999                       # Not supported on this controller
    JoyButton_R1 = 7
    JoyButton_L1 = 6
    JoyButton_R2 = 9
    JoyButton_L2 = 8
    JoyButton_L3 = 13
    JoyButton_R3 = 14
    JoyButton_Select = 10
    JoyButton_Start = 11
    JoyButton_Analog = 12
    JoyButton_Home = 999                    # Not supported on this controller
    axisUpDown = 1                          # Joystick axis to read for up / down position
    RightaxisUpDown = 3                     # Joystick axis to read for up / down position
    axisUpDownInverted = False              # Set this to True if up and down appear to be swapped
    axisLeftRight = 0                       # Joystick axis to read for left / right position
    RightaxisLeftRight = 2                  # Joystick axis to read for left / right position
    axisLeftRightInverted = False           # Set this to True if left and right appear to be swapped
    axisPosThreshold = 0.7                  # Controls the sensitivity of the joystick
    axisNegThreshold = -0.7                 # Controls the sensitivity of the joystick
    # These buttons do not exist for this controller...

else:
    FlashLEDs(4,0.5, 1.00)
    print ("Found UNKNOWN Wireless PS3 controller")
    # pygame controller constants (Not Recognised - assuming it's a simple PS3 clone...)
    JoyButton_Square = 999                  # Not supported on this controller
    JoyButton_Circle = 999                  # Not supported on this controller
    JoyButton_Triangle = 999                # Not supported on this controller
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
    JoyButton_Analog = 999
    JoyButton_Home = 999                    # Not supported on this controller
    JoyButton_L3 = 13
    JoyButton_R3 = 14
    axisUpDown = 1                          # Joystick axis to read for up / down position
    RightaxisUpDown = 3                     # Joystick axis to read for up / down position
    axisUpDownInverted = False              # Set this to True if up and down appear to be swapped
    axisLeftRight = 0                       # Joystick axis to read for left / right position
    RightaxisLeftRight = 2                  # Joystick axis to read for left / right position
    axisLeftRightInverted = False           # Set this to True if left and right appear to be swapped
    axisPosThreshold = 0.7                  # Controls the sensitivity of the joystick
    axisNegThreshold = -0.7                 # Controls the sensitivity of the joystick


# Check number of joysticks in use...
joystick_count = pygame.joystick.get_count()
print("Joystick count:")
print(joystick_count)
print("---------------")

# Check number of axes on joystick...
numaxes = joystick.get_numaxes()
print("Number of axes:")
print(numaxes)
print("---------------")

# Check number of buttons on joystick...
numbuttons = joystick.get_numbuttons()
print("Number of buttons:")
print(numbuttons)
print("---------------")

# Pause for a moment...
time.sleep(2)


# Turn all motors off
def StopMotors():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

    
# Turn both motors backwards
def Backwards():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)


# Turn both motors forwards
def Forwards():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)


# Turn Right
def Right():
    global TurnDC
    
    #print("Right")
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA * TurnDC)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB * TurnDC)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)


def BLeft():
    global TurnDC
    
    #print("Right")
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA * TurnDC)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)


def FLeft():
    global TurnDC
    
    #print("Right")
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA * TurnDC)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Turn left
def Left():
    global TurnDC
    
    #print("Left")
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA * TurnDC)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB * TurnDC)

def BRight():
    global TurnDC
    
    #print("Left")
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB * TurnDC)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

def FRight():
    global TurnDC
    
    #print("Left")
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB * TurnDC)

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
        
        # Increase the seek count
        SeekCount += 1
        
        # Change direction
        Direction = not Direction
        
    # The line wasn't found, so return False
    return False


def do_linefollower():
    #repeat the next indented block forever
    print("Following the line")
    KeepTrying = True
    while KeepTrying == True:
        # If the sensor is Low (=0), it's above the black line
        if IsOverBlack():
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
    global YButton
    global AButton
    global BButton
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
            elif event.button == JoyButton_Y:
                YButton = True
            elif event.button == JoyButton_A:
                AButton = True
            elif event.button == JoyButton_B:
                BButton = True
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
            elif event.button == JoyButton_Y:
                YButton = False
            elif event.button == JoyButton_A:
                AButton = False
            elif event.button == JoyButton_B:
                BButton = False
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
            RightUpDown = joystick.get_axis(RightaxisUpDown)
            RightLeftRight = joystick.get_axis(RightaxisLeftRight)
            # Invert any axes which are incorrect
            if axisUpDownInverted:
                upDown = -upDown
            if axisLeftRightInverted:
                leftRight = -leftRight
            # Determine Up / Down values for Left Stick
            if upDown < axisNegThreshold:
                #print ("LeftStickUp")
                LeftStickUp = True
                LeftStickDown = False
            elif upDown > axisPosThreshold:
                #print ("LeftStickDown")
                LeftStickUp = False
                LeftStickDown = True
            else:
                LeftStickUp = False
                LeftStickDown = False
            # Determine Up / Down values for Right Stick
            if RightUpDown < axisNegThreshold:
                #print ("RightStickUp")
                RightStickUp = True
                RightStickDown = False
            elif RightUpDown > axisPosThreshold:
                #print ("RightStickDown")
                RightStickUp = False
                RightStickDown = True
            else:
                RightStickUp = False
                RightStickDown = False
            # Determine Left / Right values for Left Stick
            if leftRight < axisNegThreshold:
                #print ("LeftStickLeft")
                LeftStickLeft = True
                LeftStickRight = False
            elif leftRight > axisPosThreshold:
                #print ("LeftStickRight")
                LeftStickLeft = False
                LeftStickRight = True
            else:
                LeftStickLeft = False
                LeftStickRight = False
            # Determine Left / Right values for Right Stick
            if RightLeftRight < axisNegThreshold:
                #print ("RightStickLeft")
                RightStickLeft = True
                RightStickRight = False
            elif RightLeftRight > axisPosThreshold:
                #print ("RightStickRight")
                RightStickLeft = False
                RightStickRight = True
            else:
                RightStickLeft = False
                RightStickRight = False

        

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
    print("Entering control loop...")
    print 'Press Ctrl-C to quit'
    FlashLEDs(5,0.5,1.0)
    
    # Loop indefinitely
    while True:
        # Get the currently pressed keys on the keyboard
        PygameHandler(pygame.event.get())
        if hadEvent:
            # Keys have changed, generate the command list based on keys
            hadEvent = False
            if moveQuit:
                break
            elif SelectButton and CircleButton: # Shutdown
                print ("Halting Raspberry Pi...")
                GPIO.cleanup()
                bashCommand = ("sudo halt")
                os.system(bashCommand)
                break
            elif SelectButton and BButton: # Shutdown
                print ("Halting Raspberry Pi...")
                FlashLEDs(10,0.25,1.0)
                GPIO.cleanup()
                bashCommand = ("sudo halt")
                os.system(bashCommand)
                break
            elif SelectButton and TriangleButton: # Reboot
                print ("Rebooting Raspberry Pi...")
                FlashLEDs(10,0.25,1.0)
                GPIO.cleanup()
                bashCommand = ("sudo reboot now")
                os.system(bashCommand)
                break
            elif SelectButton and YButton: # Reboot
                print ("Rebooting Raspberry Pi...")
                FlashLEDs(10,0.25,1.0)
                GPIO.cleanup()
                bashCommand = ("sudo reboot now")
                os.system(bashCommand)
                break
            elif SelectButton and XButton: # Exit
                print ("Exiting program...")
                FlashLEDs(10,0.5,1.0)
                break
            elif SelectButton and AButton: # Exit
                print ("Exiting program...")
                FlashLEDs(10,0.5,1.0)
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
            elif StartButton:
                print ("Start")
            elif SquareButton:
                print ("Square")
            elif XButton:
                print ("X")
            elif CircleButton:
                print ("Circle")
            elif TriangleButton:
                print ("Triangle")
            elif YButton:
                print ("Y")
            elif AButton:
                print ("A")
            elif BButton:
                print ("B")
            elif SelectButton and L1Button:
                #print ("L1")
                if DutyCycleA < 100:
                   DutyCycleA = DutyCycleA + 10
                if DutyCycleB < 100:
                   DutyCycleB = DutyCycleB + 10
                DutyCycleA = min(DutyCycleA, 100)
                DutyCycleB = min(DutyCycleB, 100)
                print "Speed: ", DutyCycleA, DutyCycleB
            elif R1Button:
                print ("R1")
            elif SelectButton and L2Button:
                #print ("L2")
                if DutyCycleA > 0:
                   DutyCycleA = DutyCycleA - 10
                if DutyCycleB > 0:
                   DutyCycleB = DutyCycleB - 10
                DutyCycleA = max(DutyCycleA, 0)
                DutyCycleB = max(DutyCycleB, 0)
                print "Speed: ", DutyCycleA, DutyCycleB
            elif R2Button:
                print ("R2")
            elif L3Button:
                #print ("L3")
                print "Switching to Left Stick"
                stick = "Left"
            elif R3Button:
                #print ("R3")
                print "Switching to Right Stick"
                stick = "Right"
            elif LeftStickLeft and LeftStickUp and stick == "Left":
                FLeft()
            elif LeftStickLeft and LeftStickDown and stick == "Left":
                BLeft()
            elif LeftStickRight and LeftStickUp and stick == "Left":
                FRight()
            elif LeftStickRight and LeftStickDown and stick == "Left":
                BRight()
            elif LeftStickLeft and stick == "Left":
                Left()
            elif LeftStickRight and stick == "Left":
                Right()
            elif LeftStickUp and stick == "Left":
                Forwards()
            elif LeftStickDown and stick == "Left":
                Backwards()
            elif RightStickLeft and RightStickUp and stick == "Right":
                FLeft()
            elif RightStickLeft and RightStickDown and stick == "Right":
                BLeft()
            elif RightStickRight and RightStickUp and stick == "Right":
                FRight()
            elif RightStickRight and RightStickDown and stick == "Right":
                BRight()
            elif RightStickLeft and stick == "Right":
                Left()
            elif RightStickRight and stick == "Right":
                Right()
            elif RightStickUp and stick == "Right":
                Forwards()
            elif RightStickDown and stick == "Right":
                Backwards()
            
            if HatStickLeft:
                Left()
                print ("Hat Left")
            elif HatStickRight:
                Right()
                print ("Hat Right")
            elif HatStickUp:
                Forwards()
                print ("Hat Up")
            elif HatStickDown:
                print ("Hat Down")
                Backwards()
            
            if not LeftStickLeft and not LeftStickRight and not LeftStickUp and not RightStickDown and not RightStickLeft and not RightStickRight and not RightStickUp and not LeftStickDown and not HatStickLeft and not HatStickRight and not HatStickUp and not HatStickDown:
                StopMotors()
        time.sleep(interval)
    # Disable all drives
    StopMotors()
# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    # Reset GPIO settings
    FlashLEDs(10,0.5,1.0)
    GPIO.cleanup()
            
