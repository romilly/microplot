"""
Write a monochrome bitmap file using MicroPython.

Inspired by https://stackoverflow.com/questions/8729459/how-do-i-create-a-bmp-file-with-pure-python.
"""

import math, struct

HEADER1 = b"\x00\x00\x00\x00\x20\x00\x00\x00\x0C\x00\x00\x00"
HEADER2 = b"\x01\x00\x01\x00\xff\xff\xff\x00\x00\x00"


def round_up(n, m):
    """
    return the smallest multiple of m that is >= n
    """
    return m * ((n+m-1) // m)


def le2(n):
    """
    return n as a little-endian two-byte integer
    """
    return struct.pack("<h", n)


def le4(n):
    """
    return n as a little-endian four-byte integer
    """
    return struct.pack("<i", n)


def padding_length(w):
    return (-w) % 4


class MonoBitmapWriter:
    def __init__(self, file_name, width=240, height=240):
        self._bmf = open(file_name,'wb')
        self.width = width
        self.height = height

    def _header(self):
        bitmap_file_size = le4(round_up(self.width, 4) * self.height + 0x20)
        return b"BM" + bitmap_file_size + HEADER1 + le2(self.width) + le2(self.height) + HEADER2

    def __enter__(self):
        self._bmf.write(self._header())
        width_in_bytes = round_up(self.width, 8) // 8
        self.padding = [0] * padding_length(width_in_bytes)
        return self

    def add_row(self, row):
        self._bmf.write(bytes(row+self.padding))

    def __exit__(self, et, val, tb):
        if et is not None:
            raise RuntimeError('MonoBitmapWriter failed %s' % tb)
        self._bmf.close()


