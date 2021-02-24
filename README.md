# microplot

## A (very) simple pure MicroPython plotting package.

The current version runs on the Raspberry Pi Pico with the Pimoroni Pico Explorer base.

It does line plots at the moment.

Some code was copied from https://www.instructables.com/Raspberry-Pi-Pico-Pico-Explorer-Workout/
- Tony Goodhew's great introduction to the Pico Explorer.

The line drawing uses code from https://github.com/encukou/bresenham
Copyright © 2016 Petr Viktorin

![Sample Plot](docs/img/sine3.jpg)

## Installation

You need to have the Pimoroni uf2 version 0.0.7 or later installed on your Pico.
Copy explorer.py, plots.py and demo.py to your Pico using Thonny or ampy.

Then run `demo-multi.py`

The demo displays a multi-colour graph plot on the display and then creates a graph.bmp monochrome bitmap in the Pico.

![Pico display](docs/img/new-sin.jpg)

ampy does not download binary files byt you can copy the file to your computer using `pyboard`;

```shell
./pyboard.py -d /dev/ttyACM0 -f cp :graph.bmp graph.bmp
```
Here's the bitmap file:

![graph.bmp](docs/img/bmp.png)



