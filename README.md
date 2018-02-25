PiZMoto
=======
A code library for the PiZMoto add-on board for the Raspberry Pi Zero

A simple 2-channel motor controller with extras...
   On-board 5V power supply to power the Raspberry Pi from the motor power supply
   3-pin connector for infra-red reflective sensor
   4-pin connector design to connect a HC-SR04 ultra-sonic range sensor
   2 general purpose outputs (for LEDs, servos etc.), also usable as inputs
   100% compatible with the CamJam EduKit-3 available from www.thepihut.com
  

Installation instructions for the Raspberry Pi
**********************************************

(Assumes you are using the latest version of Raspbian and have logged in as user pi)
Last tested with Raspbian Stretch 2017-09-07

1) Run git clone to clone the piz-moto folder to users/pi

   cd ~
   git clone https://github.com/astro-designs/piz-moto.git
   
2) Run the setup program

   sudo python setup.py install
   
This completes the basic installation.

Using a PS3 controller
**********************
(Apologies for missing this bit out previously)

Based on: https://www.piborg.org/blog/rpi-ps3-help

sudo apt-get -y install libusb-dev joystick python-pygame
cd ~
wget http://www.pabr.org/sixlinux/sixpair.c
gcc -o sixpair sixpair.c -lusb

I think that's it... I need to test this.


Documentation
*************

What's in the kit: PiZ-Moto Kit_v002.pdf
Assembly instructions: docs/PiZ-Moto Instructions.pdf


Example Code
************
examples/ps3bot.py - Simple 2-wheeled robot controller using a wireless PS3 controller

examples/wiibot.py - Simple 2-wheeled robot controller using a Bluetooth WiiMote controller
                     Includes routines to follow lines using an infra-red reflective sensor
                     and avoid objects using a HC-SR04 range sensor


