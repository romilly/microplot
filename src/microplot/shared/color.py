class COLORS:
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    BROWN = (139,69,19)
    RED = (255, 0, 0)
    ORANGE = (255, 168, 0)
    YELLOW = (255, 255, 0)
    PURPLE = (128, 0, 128)
    VIOLET = (238,130,238)
    GREY = (128,128,128)
    WHITE = (255, 255, 255)
    GOLD = (255,215,0)
    SILVER = (192,192,192)

    ALL = (BLUE, GREEN, RED, ORANGE, YELLOW, PURPLE)

    @classmethod
    def color(cls, i, colors=None):
        if colors is None:
            colors = cls.ALL
        return colors[i % len(colors)]

    @classmethod
    def rgb_to_hex(cls, triple: tuple) -> int:
        r, g, b = triple
        return (r << 16) + (g << 8) + b

    @classmethod
    def hex_to_rgb(cls, hex_color: int) -> tuple:
        r = (hex_color >> 16) & 0xFF
        g = (hex_color >> 8) & 0xFF
        b = hex_color & 0xFF
        return (r, g, b)

    @classmethod
    def rgb565_to_bgr_tuple(cls, color: int) -> tuple:
        blue = (color << 3) & 0x00F8  # extract each of the RGB triple into its own byte
        green = (color >> 3) & 0x00FC
        red = (color >> 8) & 0x00F8
        return (blue, green, red)

    @classmethod
    def rgb565_to_rgb_tuple(cls, color: int) -> tuple:
        b, g, r = cls.rgb565_to_bgr_tuple(color)
        return (r, g, b)




