txt = open('24_7600.txt')
line = txt.readline()
line = line.replace('QQ', 'Q Q').replace('QR', 'Q R').replace('QS', 'Q S').replace('RQ', 'R Q').replace('RR', 'R R')\
    .replace('RS', 'R S').replace('SQ', 'Q Q').replace('SR', 'S R').replace('SS', 'S S')
lines = list(line.split())
for i in range(len(lines)):
    lines[i] = len(lines[i])
print(max(lines))
