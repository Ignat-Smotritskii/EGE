matrix = [[0 for i in range(10001)] for j in range(10001)]
max_count = 0
line = 0

with open('46984.txt') as txt:
    c = int(txt.readline())
    for i in range(c):
        q = list(map(int, txt.readline().split()))
        matrix[q[0]][q[1]] = 1

for i in range(10001):
    count = 0
    for j in range(10000):
        if matrix[i][j] == 1 and matrix[i][j+1] == 1:
            count += 1
        elif matrix[i][j] == 1 and matrix[i][j+1] == 0:
            count += 1
            if max_count < count:
                max_count = count
                line = i
            count = 0

print(max_count, line)
