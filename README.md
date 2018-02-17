PiZMoto
=======
A code library for the PiZMoto add-on board for the Raspberry Pi Zero

A simple 2-channel motor controller with extras...
   On-board 5V power supply to power the Raspberry Pi from the motor power supply
   100% compatible with the EduKit-3 available from www.thepihut.com
   3-pin connector for infra-red reflective sensor
   4-pin connector design to connect a HC-SR04 ultra-sonic range sensor
   2 general purpose outputs (LEDs, servos etc.)

Installation instructions for the Raspberry Pi:
(Assumes you are using the latest version of Raspbian and have logged in as user pi)
Last tested with Raspbian Stretch 2017-09-07

1) Run git clone to clone the piz-moto folder to users/pi

   cd ~
   git clone https://github.com/astro-designs/piz-moto.git
   
2) Run the setup program

   sudo python setup.py install
   
[ Installation complete! ]

