f = open('47231A.txt')
n = int(f.readline())
points = []
cost = [0 for i in range(n)]
right_boxes = left_boxes = 0

for line in f:
    pos, count = map(int, line.split())
    points.append([pos, (count // 36) + (count % 36 != 0)])

for i in range(1, n):
    cost[0] += (points[i][0] - points[0][0]) * points[i][1]
    right_boxes += points[i][1]

for i in range(1, n):
    left_boxes += points[i - 1][1]
    distance = points[i][0] - points[i - 1][0]
    cost[i] = cost[i - 1] - (right_boxes * distance) + (left_boxes * distance)
    right_boxes -= points[i][1]

print(min(cost))
