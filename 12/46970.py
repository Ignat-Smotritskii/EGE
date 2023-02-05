def f(s):
    while not('00' in s):
        s = s.replace('01', '210', 1)
        s = s.replace('02', '3101', 1)
        s = s.replace('03', '2012', 1)
    return s.count('1') == 70 and s.count('2') == 56 and s.count('3') == 23


for c1 in range(100):
    for c2 in range(100):
        for c3 in range(100):
            s = '0' + '1' * c1 + '2' * c2 + '3' * c3 + '0'
            if f(s):
                print(len(s))
