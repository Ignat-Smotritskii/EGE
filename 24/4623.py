with open('4623.txt') as txt:
    line = txt.readline()

    count = 0
    max_count = 0
    i = 0
    while i < len(line):
        if (line[i] == '1' or line[i] == '2') and (line[i+1] == '1' or line[i+1] == '2') and\
        (line[i+2] == 'A' or line[i+2] == 'B'):
            count += 1
            i += 3
        else:
            max_count = max(max_count, count)
            count = 0
            i += 1
    print(max_count)