import itertools

words = itertools.permutations('РОСОМАХА')
odd = 'РСМХ'
even = 'ОА'
count = 0

for c in words:
    line = ''.join(c)
    flag = True
    for i in range(7):
        if (line[i] in odd and line[i+1] in odd) or (line[i] in even and line[i+1] in even):
            flag = False
    if flag:
        count += 1
print(count/4)
