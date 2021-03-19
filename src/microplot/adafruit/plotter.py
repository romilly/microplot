from abstract_plotter import AbstractPlotter, Frame
from color import COLORS
import board
import displayio
import terminalio
from adafruit_display_text import label
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.triangle import Triangle


class Plotter(AbstractPlotter):
    def __init__(self):
        AbstractPlotter.__init__(self)
        self.display = board.DISPLAY
        self.width = self.display.width
        self.height = self.display.height
        self.group = displayio.Group(max_size=100)
        colors = COLORS.ALL + (COLORS.WHITE, COLORS.BLACK)
        self.bitmap = displayio.Bitmap(320, 240, len(colors))
        self.palette = displayio.Palette(len(colors))
        self.pallet_index = {}
        for (index, color) in enumerate(colors):
            hex_color = COLORS.rgb_to_hex(color)
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
        text_area = label.Label(self.font, text=text, color=COLORS.rgb_to_hex(COLORS.WHITE))
        text_area.x = x
        text_area.y = y + 10
        self.group.append(text_area)

    def circle(self, x, y, r, color=COLORS.RED):
        color_hex = COLORS.rgb_to_hex(color)
        c = Circle(x, y, r, fill=color_hex, outline=color_hex)
        self.group.append(c)

    def triangle(self, x: int, y: int, r: int, color=COLORS.RED) -> None:
        """
        triangle function
        Draws a equilateral triangle with center in cordinates (x, y) and side
        size ``a``. Where ``a`` is equal to ``(6 x r) / √3``

                      (x0,y0)
                    /\
                   /  \
                  / .  \
                 / x, y \
         (x2,y2)/________\ (x1,y1)

        :param int x: x coordinate of the triangle center
        :param int y: y coordinate of the triangle center
        :param int r: r radius of the circle inside the triangle
        :param int color: color identification
        :return: None
        :rtype None
        """
        color_hex = COLORS.rgb_to_hex(color)
        # to simplify math we take the following approximation √3≈1.732
        square_three = 1.732
        r = r // 2
        x0 = x - int(round(square_three * r))
        y0 = y + r
        x1 = x
        y1 = y - int(round(square_three * 2 * r))
        x2 = x + int(round(square_three * r))
        y2 = y + r

        c = Triangle(x0, y0, x1, y1, x2, y2, fill=color_hex, outline=color_hex)
        self.group.append(c)

    def set_pen(self, color):
        self.pen = self.pallet_index[color]

    def default_frame(self):
        return Frame(320, 240, 20, 20, 60, 20)

    def blk(self):
        self.bitmap.fill(len(self.palette))

    def show(self):
        self.display.show(self.group)
