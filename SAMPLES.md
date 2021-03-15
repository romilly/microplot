

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

