def receive():
    with open('binary.txt') as text_file:
        with open('binary.bmp','wb' ) as bmp_file:
            buffer = None
            bl = 0
            count = 0
            for line in text_file:
                count += 1
                line = line.strip()
                if len(line) == 0:
                    break
                bl = len(line) // 2
                if buffer is None:
                    buffer = bytearray(bl)
                for i in range(bl):
                    try:
                        buffer[i] = int(line[2*i:2*i+2],16)
                    except Exception as e:
                        print(count, line, e)
                        return
                bmp_file.write(buffer)

receive()
