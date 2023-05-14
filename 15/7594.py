for a in range(1, 4096):
    flag = True
    for x in range(1, 4096):
        if not((x & 39 == 0) or ((x & 11 == 0) <= (not(x & a == 0)))):
            flag = False
    if flag:
        print(a)
        break
