import math
from plotter import Plotter
from plots import LinePlot
import board
import digitalio
import busio
import adafruit_sdcard
import storage
from adafruit_bitmapsaver import save_pixels


def plot():
    sines = list(math.sin(math.radians(x))
                 for x in range(0, 361, 4))
    lineplot = LinePlot([sines],'MicroPlot line')
    plotter = Plotter()
    lineplot.plot(plotter)


def save():
    spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    cs = digitalio.DigitalInOut(board.SD_CS)
    sdcard = adafruit_sdcard.SDCard(spi, cs)
    vfs = storage.VfsFat(sdcard)
    storage.mount(vfs, "/sd")
    save_pixels("/sd/screenshot.bmp")


plot()
save()
print('done')
