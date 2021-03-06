import re
# RESISTORS = (BLACK, BROWN, RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET, GREY)
# TOLERANCE = {
#         1:  BROWN,
#         2:  RED,
#         5:  GOLD,
#         10: SILVER,
#         20: None
#     }

res_reg = re.compile('([0-9][0-9]?0?)([RkKM])$|([0-9][0-9]?)([RkKM])([0-9])$')

multipliers = {'R' : '',
               'k' : '000',
               'K' : '000',
               'M' : '000000',

               }


class Resistor:
    def __init__(self, prefix, multiplier, suffix=''):
        self.prefix = prefix
        self.multiplier = multiplier
        self.suffix = suffix

    @classmethod
    def parse_from(cls, text):
        i = res_reg.match(text)
        if i is None:
            raise Exception('I only understand resistance values in standard form - e.g. 2R2, 220k, 1M2')
        if i.group(1):
            return Resistor(i.group(1), i.group(2))
        else:
            return Resistor(i.group(3), i.group(4), i.group(5))

    def __eq__(self, other):
        if not isinstance(other, Resistor):
            return False
        if (
            other.prefix != self.prefix or
            other.multiplier != self.multiplier or
            other.suffix != self.suffix):
                return False
        return True

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self):
        result = self.prefix+self.multiplier
        result += self.suffix
        return result

    def __repr__(self):
        return 'Resistor(%s)' % str(self)

    def value(self) -> str:
        result = self.prefix
        if self.multiplier == 'R' and self.suffix != '':
            return self.prefix+'.'+self.suffix
        if self.suffix == '':
            return self.prefix+multipliers[self.multiplier]
        else:
            return self.prefix + self.suffix + multipliers[self.multiplier][:-1]



# def bands_for(self, decimal_value):
#     digits, exponent = decimal_value.as_tuple()[1:]  # don't care about sign
#     zeros = sum([(0 == digit) for digit in digits])
#     significant_digits = [digit for digit in digits if digit != 0]
#     start = ([0] + significant_digits)[-2:]
#     multiplier = zeros + exponent
#     return list(colors[digit] for digit in start) + [multiplier_color[multiplier]]


# def tolerance_band(self, tolerance):
#     if tolerance not in tolerance_bands:
#         raise ValueError('Tolerance must be 1%, 5% or 10%')
#     return tolerance_bands[tolerance]