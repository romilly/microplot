"""
Write a monochrome bitmap file using MicroPython.

Inspired by https://stackoverflow.com/questions/8729459/how-do-i-create-a-bmp-file-with-pure-python.
"""

import math, struct, os


BF_TYPE = b'BM'

"""
Create and write out a Monochrome Bitmap File.

File is built from BITMAPFILEHEADER, BITMAPINFOHEADER, RGBQUAD table, scanlines
"""


def mult(m, n):
    return m * ((n+m-1) // m)


def padding_length(w):
    return (-w) % 4


class BitmapWriter:
    def __init__(self, file_name, width=240, height=240):
        self._bmf = None
        self.file_name  = file_name
        self.width = width
        self.height = height

    def __enter__(self):
        if self.file_name in os.listdir():
            os.remove(self.file_name)
        self._bmf = open(self.file_name,'wb')
        self.write_header(self.width, self.height)
        width_in_bytes = self.width // 8
        self.padding = bytearray([0] * padding_length(width_in_bytes))
        return self

    def add_row(self, row):
        self._bmf.write(row+self.padding)

    def __exit__(self, et, val, tb):
        self._bmf.close()

    def write_header(self, width, height, biBitCount=b'\x01\x00', bfOffBits=b'\x20\x00\x00\x00'):
        n = mult(4,width) * height + 0x20
        self.write_bitmap_file_header(bfOffBits, n)
        self.write_bitmap_info_header(biBitCount, height, width)
        self.write_mono_rgb_triples()

    def write_mono_rgb_triples(self):
        rgbBlack = b'\xff\xff\xff'
        rgbWhite = b'\x00\x00\x00'
        self.write(rgbBlack,
                   rgbWhite)

    def write_bitmap_info_header(self, biBitCount, height, width):
        self.write(b'\x0C\x00\x00\x00',
                   struct.pack("<H", width),
                   struct.pack("<H", height),
                   b'\x01\x00',
                   biBitCount)

    def write_bitmap_file_header(self, bfOffBits, n):
        self.write(b"BM",
                   struct.pack("<I", n),
                   b'\x00\x00',
                   b'\x00\x00',
                   bfOffBits)

    def write(self, *items):
        for item in items:
            self._bmf.write(item)


class MonoBitmapWriter(BitmapWriter):
    pass


