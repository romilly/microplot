from so_mono_bitmap import bmp
from so_mono_bitmap_annotated import bmp as bmpa

smile = [[0xFF], [0x81], [0xA5], [0x81], [0xA5], [0xBD], [0x81], [0xFF]]

s1 = bytearray(bmp(smile, 8))
s2 = bytearray(bmpa(reversed(smile), 8, 8))
#print(type(s1))

def compare(s1, s2):
    for (b1, b2) in zip(s1, s2):
        if b1 != b2:
            return False
    return True

print(compare(s1, s2))