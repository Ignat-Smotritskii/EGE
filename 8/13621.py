import itertools
combinations = itertools.product('ABCDEX', repeat=4)
count = 0
for c in combinations:
    line = ''.join(c)
    if line.count('X') == 1 and (line[0] == 'X' or line[-1] == 'X'):
        count += 1
print(count)
