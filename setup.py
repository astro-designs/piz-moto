#!/usr/bin/env python

from distutils.core import setup,Extension
setup(
    name = "piz_moto",
    version = "0.1.1",
    author = "Mark Cantrill",
    author_email = "mark@astro-designs.com",
    description = ("Code library for the PiZ-Moto motor driver add-on board for the Raspberry Pi Zero"),
    license = "MIT",
    keywords = "raspberry pi rpi motor driver L293D piz-moto pizmoto",
    url = "https://github.com/astro-designs/piz-moto.git",
    packages=['piz_moto'],
)
