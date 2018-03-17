PiZMoto
=======
A code library for the PiZ-Moto add-on board for the Raspberry Pi Zero
with examples,
     tutorials,
     and a 3D printable design for a Raspberry Pi Zero powered MicroPiNoon compatible balloon-popping 'bot!

     
The PiZ-Moto is a simple 2-channel motor controller with extras...
   * On-board 5V power supply to power the Raspberry Pi from the motor power supply
   * 3-pin connector for adding an infra-red reflective sensor
   * 4-pin connector for adding a HC-SR04 ultra-sonic range sensor
   * 2 general purpose inputs or outputs (for LEDs, servos, etc.)
   * 100% compatible with the CamJam EduKit-3 available from www.thepihut.com
  

Installation instructions for the Raspberry Pi
**********************************************

(This assumes you are using the latest version of Raspbian and have logged in as user "pi")
Last tested with Raspbian Stretch 2017-09-07

1) Run git clone to clone the piz-moto folder to users/pi

   cd ~
   git clone https://github.com/astro-designs/piz-moto.git
   
2) Run the setup program

   sudo python setup.py install
   
This completes the basic installation.

Using a PS3-compatible wireless controller
******************************************
(Apologies for missing this bit out in previous versions)

These setup notes are based on: https://www.piborg.org/blog/rpi-ps3-help

sudo apt-get update

sudo apt-get -y install libusb-dev joystick python-pygame
cd ~
wget http://www.pabr.org/sixlinux/sixpair.c
gcc -o sixpair sixpair.c -lusb

Tested with a Rock Candy wireless PS3 controller and one other ultra-cheap wireless PS3 controller found on ebay.

This is also worth a look from the Pi Hut although i've not tested it myself...
https://thepihut.com/products/raspberry-pi-compatible-wireless-gamepad-controller


Documentation
*************

What's in the kit:     docs/PiZ-Moto Kit-List.pdf
Assembly instructions: docs/PiZ-Moto Instructions.pdf


Example Code
************
examples/ps3bot.py - Simple 2-wheeled robot controller using a wireless PS3 controller

examples/wiibot.py - Simple 2-wheeled robot controller using a Bluetooth WiiMote controller
                     Includes routines to follow lines using an infra-red reflective sensor
                     and avoid objects using a HC-SR04 range sensor

Tutorials
*********

These tutorials were written for a simple motor control tutorial held at the Cotswold Raspberry Jam
in June 2017. The tutorial worksheet can be downloaded from:
http://cotswoldjam.org/downloads/2017-06/motor-control-worksheet.pdf

tutorial/task1.py
tutorial/task2.py
tutorial/task3.py
