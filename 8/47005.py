import itertools

words = itertools.permutations('ПАРАБОЛА')
glas = 'АО'
soglas = 'ПРБЛ'
s = set()

for c in words:
    flag = True
    for i in range(7):
        if not((c[i] in glas and c[i+1] in soglas) or (c[i] in soglas and c[i+1] in glas)):
            flag = False
    if flag:
        s.add(c)

print(len(s))
