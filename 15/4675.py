for a in range(1, 124):
    F = True
    for x in range(1, 124):
        if not(((x % 6 == 0) <= (not(x % 10) == 0)) or (x + a > 121)):
            F = False
    if F:
        print(a)
