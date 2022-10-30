def f(s):
    while '00' not in s:
        s = s.replace('01', '210', 1)
        s = s.replace('02', '3101', 1)
        s = s.replace('03', '2012', 1)
    return s


for x1 in range(50):
    for x2 in range(50):
        for x3 in range(50):
            s = '0' + ('1' * x1) + ('2' * x2) + ('3' * x3) + '0'
            # Вызывать только один раз!!!
            res = f(s)
            if res.count('1') == 61 and res.count('2') == 50 and res.count('3') == 18:
                print(len(s))
