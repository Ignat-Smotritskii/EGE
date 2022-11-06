with open('27699.txt') as txt:
    line = txt.readline()
    count = 1
    max_count = 0
    for i in range(len(line) - 1):
        if line[i] == 'L':
            f = True
        if f and (line[i] == 'L' and line[i+1] == 'D') or (line[i] == 'D' and line[i+1] == 'R') or (line[i] == 'R' and line[i+1] == 'L'):
            count += 1
            max_count = max(count, max_count)
        else:
            count = 1
            f = False
    print(max_count)