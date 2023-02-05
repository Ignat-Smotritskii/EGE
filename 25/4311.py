for i in range(123889, 10**8 + 1):
    s = str(i)
    if i % 1000 == 890 and s[:3] == '123':
        if i % 27 == 0:
            print(i, i//27)