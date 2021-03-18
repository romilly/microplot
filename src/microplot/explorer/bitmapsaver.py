"""
Adapted from "https://github.com/adafruit/Adafruit_CircuitPython_BitmapSaver.git"
"""


import gc
import struct

from abstract_plotter import AbstractPlotter


def _write_bmp_header(output_file, filesize):
    output_file.write(bytes("BM", "ascii"))
    output_file.write(struct.pack("<I", filesize))
    output_file.write(b"\00\x00")
    output_file.write(b"\00\x00")
    output_file.write(struct.pack("<I", 54))


def _write_dib_header(output_file, width, height):
    output_file.write(struct.pack("<I", 40))
    output_file.write(struct.pack("<I", width))
    output_file.write(struct.pack("<I", height))
    output_file.write(struct.pack("<H", 1))
    output_file.write(struct.pack("<H", 24))
    for _ in range(24):
        output_file.write(b"\x00")


def _bytes_per_row(source_width):
    pixel_bytes = 3 * source_width
    padding_bytes = (4 - (pixel_bytes % 4)) % 4
    return pixel_bytes + padding_bytes


def rgb565_to_bgr_tuple(pixel565):
    pass


def _write_pixels(output_file, plotter: AbstractPlotter):
    width = plotter.width()
    height = plotter.height()
    row_buffer = bytearray(_bytes_per_row(width))
    for y in range(height, 0, -1):
        buffer_index = 0
        for i in range(width):
            try:
                pixel = plotter.get_pixel(i, y-1)
            except Exception as e:
                print(i, y)
                raise e
            for b in reversed(pixel):
                row_buffer[buffer_index] = b & 0xFF
                buffer_index += 1
        output_file.write(row_buffer)
        gc.collect()


def save_pixels(filename, plotter: AbstractPlotter):
    """Save pixels to a 24 bit per pixel BMP file.


    :param filename: the file name to save to
    :param plotter: plotter that created the image to save
    """
    width = plotter.width()
    height = plotter.height()
    filesize = 54 + height * _bytes_per_row(width)

    with open(filename, "wb") as output_file:
        _write_bmp_header(output_file, filesize)
        _write_dib_header(output_file, width, height)
        _write_pixels(output_file, plotter)
