def div(n):
    count = 0
    q = 0
    sqrt = int(n ** 0.5)
    if sqrt == n ** 0.5:
        for t in range(2, sqrt):
            if n % t == 0:
                count += 1
                q = t
            if count > 1:
                break
        if count == 1:
            return n//q
    return -1


for a in range(289123456, 389123457):
    h = div(a)
    if h != -1:
        print(a, h)
