class MockPlotter:
    def __init__(self):
        self.width = 10
        self.height = 5
        self._display_buffer = list(range(100))

    def get_pixel(self, x, y):
        start = x + y*self.width
        data = self._display_buffer
        # b_low, b_high = self._display_buffer[start:start+2]
        # return b_low + b_high << 8
        return (data[start * 2] ) , (data[start * 2 + 1])

for y in range(5):
    print(list(MockPlotter().get_pixel(x,y) for x in range(10)))

