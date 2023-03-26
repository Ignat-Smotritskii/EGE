for m in range(10000):
    summ = 135 + (2 * m)
    count = 0
    for t in range(2, summ):
        if summ % t == 0:
            count += 1
    if count == 3:
        print(m)
        break
