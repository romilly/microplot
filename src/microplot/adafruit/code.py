import math
from plotter import Plotter
from plots import ScatterPlot
import board
import digitalio
import busio
import adafruit_sdcard
import storage
from adafruit_bitmapsaver import save_pixels


def plot():
    data = [[(20, 30), (40, 50), (10, 90), (60, 60)], [(10, 25), (45, 65)], [(33, 70)]]

    splot = ScatterPlot(data, 'Scatter Plot')
    plotter = Plotter()
    splot.plot(plotter)


def save():
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    cs = digitalio.DigitalInOut(board.SD_CS)
    sdcard = adafruit_sdcard.SDCard(spi, cs)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, "/sd")
    save_pixels("/sd/splot.bmp")


plot()
save()
print('done')
