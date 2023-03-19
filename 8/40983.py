import itertools

count = 0
codes = itertools.permutations('ГЕОРГИЙ')

for c in codes:
    line = ''.join(c)
    if 'ГГ' not in line:
        count += 1

print(count//2)
