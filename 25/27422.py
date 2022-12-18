from math import sqrt
for i in range(174457, 174506):
    del_ = 0
    count = 0
    for j in range(2, round(sqrt(i))):
        if i/j == i//j:
            del_ = j
            count += 1
        if count > 1:
            break
    if count == 1:
        print(del_, i//del_)