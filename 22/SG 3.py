from fnmatch import fnmatch

txt = open('SG 3.txt')
duration = {}
relation = {}
time = {}
lines = txt.readlines()

for l in lines:
    l = l.strip()
    a, b, c = l.split('\t')
    duration[a] = int(b)
    relation[a] = c.replace('"', '')
    if relation[a] == '0':
        time[a] = duration[a]
    elif fnmatch(relation[a], '*;*'):
        first, second = relation[a].split(';')
        time[a] = duration[a] + max(time[first], time[second])
    else:
        time[a] = duration[a] + time[relation[a]]

count = 0
ms = 0
for ms in range(100000):
    for i in time:
        if int(time[i]) == ms:
            count += 1
    if count == 70:
        print(ms)
        break
