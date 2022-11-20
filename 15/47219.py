for a in range(1, 200):
    f = True
    for x in range(1, 200):
        if not(((x % 2 == 0) <= (not(x % 3 == 0))) or (x + a >= 100)):
            f = False
    if f:
        print(a)
        break