txt = open('33494.txt')
line = txt.readline()
letters = {}
m = 0
s = ''

for i in range(len(line) - 1):
    if line[i] == 'E':
        if line[i+1] in letters:
            letters[line[i+1]] += 1
        else:
            letters[line[i+1]] = 1
        if letters[line[i+1]] > m:
            m = letters[line[i+1]]
            s = line[i+1]
print(s)
