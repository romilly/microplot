with open('test-binary-file.xx','wb') as bf:
    buffer = bytearray(256)
    for i in range(256):
        buffer[i] = i
    for row in range(1000):
        bf.write(buffer)


