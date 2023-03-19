import itertools

words = itertools.product('АНДРЕЙ', repeat=6)
count = 0

for c in words:
    line = ''.join(c)
    if (line[0] != 'Й') and (line[-1] != 'Й') and (line.count('Й') <= 1) and ('ЙЕ' not in line) and ('ЕЙ' not in line):
        count += 1
print(count)
