def m(n):
    mult = 1
    count = 0
    for i in range(2, n+1):
        if count == 5:
            break
        if n % i == 0:
            mult *= i
            count += 1
    if count == 5:
        return mult
    return 0


num_count = 0
num = 500000001
while num_count != 5:
    q = m(num)
    if 0 < q < num:
        print(q)
        num_count += 1
    num += 1
