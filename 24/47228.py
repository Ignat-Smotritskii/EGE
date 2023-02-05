count = 0
max_count = 0
with open('47228.txt') as txt:
    line = txt.readline()
    i = 0
    while i < len(line):
        if (line[i] == 'C' or line[i] == 'F' or line[i] == 'D') and (line[i+1] == 'A' or line[i+1] == 'O'):
            count += 1
            i += 2
            max_count = max(max_count, count)
        else:
            i += 1
            count = 0
    print(max_count)