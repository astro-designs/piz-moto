PiZMoto
=======
A code library for the PiZ-Moto / PiZ-Moto+ add-on board for the Raspberry Pi Zero
with assembly instructions, examples for both Python & Scratch, tutorials,
and a 3D printable design for a Raspberry Pi Zero powered MicroPiNoon compatible balloon-popping 'bot!


The PiZ-Moto is a self-assembly simple 2-channel motor controller with extras...
   * On-board 5V power supply to power the Raspberry Pi Zero from the motor power supply
   * 3-pin connector for adding an infra-red reflective 'Line Follower' sensor
   * 4-pin connector for adding a HC-SR04 ultra-sonic distance sensor
   * 2 x 3-pin servo-compatible connectors usable as inputs or outputs (for LEDs, servos, etc.)
   * on-board GPIO driven LED
   * Expansion header bringing out some spare GPIO
   * Compatible with the CamJam EduKit-3 available from www.thepihut.com
  

Installation instructions for the Raspberry Pi
**********************************************

These instructions assume you are using the latest version of Raspbian and have logged in as user "pi"
Last tested with Raspbian Stretch 2017-09-07

1) Run git clone to clone the piz-moto folder to users/pi

   cd ~
   
   git clone https://github.com/astro-designs/piz-moto.git
   
2) Run the setup program

   sudo python setup.py install
   
This completes the basic installation.

Using a PS3-compatible wireless controller
******************************************

These setup notes are based on: https://www.piborg.org/blog/rpi-ps3-help

sudo apt-get update

sudo apt-get -y install libusb-dev joystick python-pygame

cd ~

wget http://www.pabr.org/sixlinux/sixpair.c

gcc -o sixpair sixpair.c -lusb


Tested with a Rock Candy wireless PS3 controller and one other ultra-cheap wireless PS3 controller found on ebay.

If you're looking for a wireless PS3 controller, this is also worth a look, available from The PiHut although i've not tested it myself...
https://thepihut.com/products/raspberry-pi-compatible-wireless-gamepad-controller


Documentation
*************

Assembly instructions: 
                     docs/PiZ-Moto+ Instructions.pdf (Instructions for PiZ-Moto+ (black)
                     docs/PiZ-Moto Instructions.pdf (Instructions for PiZ-Moto (green)


Example Code
************
examples/ps3bot.py - Simple 2-wheeled robot controller using a wireless PS3 controller

examples/wiibot.py - Simple 2-wheeled robot controller using a Bluetooth WiiMote controller
                     Includes routines to follow lines using an infra-red reflective sensor
                     and avoid objects using a HC-SR04 range sensor
                     
examples/candle.py - Using a PiZ-Moto motor driver to drive a lamp to simulate a flickering candle
                     
examples/Scratch/EduKitRobot.sb - Scratch based example,
                     Ideal for getting to grips with motor control using Scratch on the Raspberry Pi
                     VNC into your Raspberry Pi & PiZ-Moto and run Scratch over VNC to control your robot
                     instead of using a PS3 or Wii controller

Tutorials
*********

These tutorials were written for a simple motor control tutorial held at the Cotswold Raspberry Jam
in June 2017. The tutorial worksheet can be downloaded from:
http://cotswoldjam.org/downloads/2017-06/motor-control-worksheet.pdf

tutorial/task1.py
tutorial/task2.py
tutorial/task3.py


3D Printable MicroPiNoon 'Bot
*****************************

We've included all files, including STL files and the Sketchup model for our 3D-printed MicroPiNoon
MicroPiNoon compatible balloon-popping robots. These are a regular feature at the Cotswold Raspberry Jam

MicroPiNoon/3D_Printing         - stl files
MicroPiNoon/Bot4.jpg            - Simple render of the completed robot
MicroPiNoon/Instructions.txt    - Assembly instructions
MicroPiNoon/PartsList.txt       - List of parts needed for the robot