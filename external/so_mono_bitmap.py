import math, struct

mult4 = lambda n: int(math.ceil(n/4))*4
mult8 = lambda n: int(math.ceil(n/8))*8
lh = lambda n: struct.pack("<h", n)
li = lambda n: struct.pack("<i", n)

def bmp(rows, w):
    h, wB = len(rows), int(mult8(w)/8)
    s, pad = li(mult4(wB)*h+0x20), [0]*(mult4(wB)-wB)
    s = li(mult4(w)*h+0x20)
    return (b"BM" + s + b"\x00\x00\x00\x00\x20\x00\x00\x00\x0C\x00\x00\x00" +
            lh(w) + lh(h) + b"\x01\x00\x01\x00\xff\xff\xff\x00\x00\x00" +
            b"".join([bytes(row+pad) for row in reversed(rows)]))