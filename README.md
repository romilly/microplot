# microplot

## A (very) simple pure MicroPython plotting package.

The current version runs on the Raspberry Pi Pico with the Pimoroni Pico Explorer base.

It only does line plots in monochrome at the moment.

Some code was copied from https://www.instructables.com/Raspberry-Pi-Pico-Pico-Explorer-Workout/
- Tony Goodhew's great introduction to the Pico Explorer.

The line drawing uses code from https://github.com/encukou/bresenham
Copyright © 2016 Petr Viktorin

## Installation

You need to have the Pimoroni uf2 version 0.0.7 or later installed on your Pico.
Copy explorer.py, plots.py and demo.py to your Pico using Thonny or ampy.

Then run `demo.py`

![Sample Plot](docs/img/sine3.jpg)