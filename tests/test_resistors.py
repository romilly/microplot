import unittest

from resistors import Resistor


class ResistorsTestCase(unittest.TestCase):
    def test_parses_text(self):
        self.assertEqual(Resistor.parse_from('1R').value(), '1')
        self.assertEqual(Resistor.parse_from('12R').value(), '12')
        self.assertEqual(Resistor.parse_from('220R').value(), '220')
        self.assertEqual(Resistor.parse_from('1K').value(), '1000')
        self.assertEqual(Resistor.parse_from('3K9').value(), '3900')
        self.assertEqual(Resistor.parse_from('10K').value(), '10000')
        self.assertEqual(Resistor.parse_from('68K').value(), '68000')
        self.assertEqual(Resistor.parse_from('68k').value(), '68000')
        self.assertEqual(Resistor.parse_from('100K').value(), '100000')
        self.assertEqual(Resistor.parse_from('220K').value(), '220000')
        self.assertEqual(Resistor.parse_from('1M').value(), '1000000')


if __name__ == '__main__':
    unittest.main()
