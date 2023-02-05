import itertools

lines = itertools.permutations('АМФИБРАХИЙ')
count = 0
s = set()


for q in lines:
    line = ''.join(q)
    if 'ААФИИ' in line or 'ИИФАА' in line:
        s.add(line)
        count += 1
print(count//4,  len(s))
