"""
Write a monochrome bitmap file using MicroPython.

Inspired by https://stackoverflow.com/questions/8729459/how-do-i-create-a-bmp-file-with-pure-python.
"""

import math, struct, os


WORD = "<h"
DWORD = "<i"
BF_TYPE = b'BM'

"""
Create and write out a Monochrome Bitmap File.

File is built from BITMAPFILEHEADER, BITMAPINFOHEADER, RGBQUAD table, scanlines
"""


def mult(m, n):
    """
    return the smallest multiple of m that is >= n
    """
    return m * ((n+m-1) // m)


def word(n):
    """
    return n as a little-endian two-byte integer
    """
    return struct.pack(WORD, n)


def dword(n):
    """
    return n as a little-endian four-byte integer
    """
    return struct.pack(DWORD, n)


def padding_length(w):
    return (-w) % 4


def header(width, height):
    width_in_bytes = int(mult(8, width) / 8)
    pad = [0]*(mult(4, width_in_bytes)-width_in_bytes)
    bfSize = dword(mult(4,width) * height + 0x20)
    bfReserved1 = b'\x00\x00'
    bfReserved2 = b'\x00\x00'
    bfOffBits = b'\x20\x00\x00\x00'
    bfType = b"BM"
    biSize = b'\x0C\x00\x00\x00'
    biWidth = word(width)
    biHeight = word(height)
    biPlanes = b'\x01\x00'
    biBitCount = b'\x01\x00'
    rgbBlack = b'\xff\xff\xff'
    rgbWhite = b'\x00\x00\x00'
    return (
            # BITMAPFILEHEADER
            bfType +
            bfSize +
            bfReserved1 +
            bfReserved2 +
            bfOffBits +
            # BITMAPINFOHEADER
            biSize +
            biWidth +
            biHeight +
            biPlanes +
            biBitCount +
            # RGB_TRIPLES
            rgbBlack +
            rgbWhite)


class MonoBitmapWriter:
    def __init__(self, file_name, width=240, height=240):
        self._bmf = None
        self.file_name  = file_name
        self.width = width
        self.height = height

    def __enter__(self):
        if self.file_name in os.listdir():
            os.remove(self.file_name)
        self._bmf = open(self.file_name,'wb')
        self._bmf.write(header(self.width, self.height))
        width_in_bytes = self.width // 8
        self.padding = bytearray([0] * padding_length(width_in_bytes))
        return self

    def add_row(self, row):
        self._bmf.write(row+self.padding)

    def __exit__(self, et, val, tb):
        self._bmf.close()


