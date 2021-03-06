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
    def to_hex_color(cls, triple: tuple):
        r, g, b = triple
        return (r << 16) + (g << 8) + b
