line = '>' + 25 * '1' + 17 * '2' + 10 * '3'
while '>1' in line or '>2' in line or '>3' in line:
    if '>1' in line:
        line = line.replace('>1', '22>3', 1)
    if '>2' in line:
        line = line.replace('>2', '2>', 1)
    if '>3' in line:
        line = line.replace('>3', '11>2', 1)
print(line.count('1') + line.count('2') * 2 + line.count('3') * 3)
