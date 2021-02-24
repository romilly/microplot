"""
Display the voltage across a capacitor as it charges and discharges.
"""

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




