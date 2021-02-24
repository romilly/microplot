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

## Using the plotter to explore electronics

This experiment uses the plotter to illustrate the charging of a capacitor.

Here's the explorer set-up.

![Explorer](docs/img/cap-demo.jpg)

The output from GP0 is connected to one end of a 1K resistor. The other is connected to the positive side of 
a 4.7uF electrolytic capacitor, amd the common connection is used as an input to ADC0.

The negative side of the electrolytic capacitor is connected to  Ov (ground).

The code turns GP0 on and off every 50 milli-seconds, and the plot shows how the voltage across the capacitor varies.

The program is called `capvoltage.py`.

```python
from machine import Pin, ADC
from utime import sleep_us

from explorer import ExplorerPlotter
from plots import LinePlot


def capture_voltage(time_us=1000, samples=100):
    data = [0]*samples
    source = Pin(0, Pin.OUT)
    voltmeter = ADC(26)
    for i in range(samples):
        value = 1 if i < samples // 2 else 0
        source.value(value)
        data[i] = 3.3 * voltmeter.read_u16() / 65000.0
        sleep_us(time_us)
    return data


plot = LinePlot(capture_voltage(),'Cap charging')
plotter = ExplorerPlotter()
plot.plot(plotter)
```




