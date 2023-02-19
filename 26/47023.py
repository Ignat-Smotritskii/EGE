matrix = [[0 for j in range(10001)] for i in range(10001)]
max_count = 0
max_num = -1
line = ''

with open('47023.txt') as txt:
    a = int(txt.readline())
    for i in range(a):
        b = list(map(int, txt.readline().split()))
        matrix[b[0]][b[1]] = 1

for i in range(10001):
    for j in range(10000):
        if matrix[i][j] != matrix[i][j+1]:
            line = line + str(matrix[i][j])
        else:
            line = line + str(matrix[i][j])
            if line.count('1') > max_count:
                max_count = line.count('1')
                max_num = i
            line = ''


print(max_count, max_num)
