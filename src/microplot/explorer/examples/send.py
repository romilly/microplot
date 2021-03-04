def send(filename):
    with open(filename,'rb') as bf:
        while True:
            buffer = bf.read(100)
            if len(buffer) == 0:
                break
            text= ''.join('%02X' % ch for ch in buffer)
            print(text)

send('demo1.bmp')