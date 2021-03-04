import struct

WORD = "<h"
DWORD = "<i"
BF_TYPE = b'BM'

"""
Create and write out a Monochrome Bitmap File.

File is build from BITMAPFILEHEADER, BITMAPINFOHEADER, RGBQUAD table, scanlines
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


def write_mono_bmp(file_name, rows, height, width):
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
    with open(file_name,'wb') as bmf:
        bmf.write(
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
            # PIXELS
        for padded in pad_rows(pad, rows):
            bmf.write(padded)
        bmf.close()




def pad_rows(pad, rows):
    return b"".join([bytes(row + pad) for row in rows])