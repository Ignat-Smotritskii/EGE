import itertools
words = itertools.product('ГЕПАРД', repeat=5)

count = 0
for c in words:
    if c.count('Г') == 1 and c[0] != 'А' and c[-1] != 'Е':
        count += 1
print(count)