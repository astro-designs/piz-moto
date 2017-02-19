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


