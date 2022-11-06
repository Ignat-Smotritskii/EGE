with open('27421.txt') as txt:
    line = txt.readline()
    count = 1
    max_count = 0
    for i in range(len(line) - 1):
        if line[i] != line[i+1]:
            count += 1
            max_count = max(count, max_count)
        else:
            count = 1
    print(max_count)