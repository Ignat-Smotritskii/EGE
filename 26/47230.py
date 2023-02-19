with open('47230.txt') as txt:
    a = int(txt.readline())
    boxes = list(map(int, txt.readlines()))
    boxes.sort(reverse=True)
    count = 1
    box_now = boxes[0]

for i in range(a):
    if boxes[i] <= box_now - 3:
        count += 1
        box_now = boxes[i]

print(count, box_now)