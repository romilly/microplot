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
    RESISTORS = (BLACK, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, GREY)
    TOLERANCE = {
        1:  BROWN,
        2:  RED,
        5:  GOLD,
        10: SILVER,
        20: None
    }

    @classmethod
    def color(cls, i):
        return cls.ALL[i % len(cls.ALL)]
