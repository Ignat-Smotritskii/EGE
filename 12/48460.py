max_count = -1
for x in range(1000):
    s = '0' + x * '2' + x * '1' + '0'
    while '00' not in s:
        s = s.replace('011', '20', 1)
        s = s.replace('022', '10', 1)
        s = s.replace('01', '220', 1)
        s = s.replace('02', '110', 1)
    if (s.count('1') == 47) and (s.count('2') < 70):
        max_count = max(max_count, s.count('2'))
print(max_count)
