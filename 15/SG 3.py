for a in range(1, 256):
    flag = True
    for x in range(256):
        if not(((x & 35 != 0) or (x & 22 != 0)) <= ((x & 15 == 0) <= (x & a != 0))):
            flag = False
    if flag:
        print(a)
