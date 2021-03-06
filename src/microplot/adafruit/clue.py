from plotter import Plotter, Frame
from color import COLORS
import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.circle import Circle


class CluePlotter(Plotter):
    def __init__(self):
        Plotter.__init__(self)
        self.display = board.DISPLAY
        self.width = self.display.width
        self.height = self.display.height
        self.group = displayio.Group(max_size=100)
        colors = COLORS.ALL + (COLORS.WHITE, COLORS.BLACK)
        self.bitmap = displayio.Bitmap(320, 240, len(colors))
        self.palette = displayio.Palette(len(colors))
        self.pallet_index = {}
        for (index, color) in enumerate(colors):
            hex_color = COLORS.to_hex_color(color)
            self.palette[index] = hex_color
            self.pallet_index[color] = index
        tile_grid = displayio.TileGrid(self.bitmap, pixel_shader=self.palette)
        self.group.append(tile_grid)
        self.font = terminalio.FONT
        self.blk()
        self.display.show(self.group)
        self.display.refresh()

    def display_pixel(self, x, y):
        self.bitmap[x, y] = self.pen

    def get_pixel(self, x, y):
        return self.bitmap[x, y]

    def text(self, x, y, text):
        text_area = label.Label(self.font, text=text, color=COLORS.to_hex_color(COLORS.WHITE))
        text_area.x = x
        text_area.y = y + 10
        self.group.append(text_area)

    def circle(self, x ,y, r, color=COLORS.RED):
        color_hex = COLORS.to_hex_color(color)
        c = Circle(x, y, r, fill=color_hex, outline=color_hex)
        self.group.append(c)

    def set_pen(self, color):
        self.pen = self.pallet_index[color]

    def default_frame(self):
        return Frame(320, 240, 20, 20, 60, 20)

    def blk(self):
        self.bitmap.fill(len(self.palette))

    def show(self):
        self.display.show(self.group)