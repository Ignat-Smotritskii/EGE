count = 0
with open('47213.txt') as txt:
    for line in txt:
        nums = list(map(int, line.split('\t')))
        if (len(nums) - len(set(nums)) == 1):
            a = sum(nums) - sum(set(nums))
            if 2*a >= (sum(set(nums)) - a)/4:
                count += 1
print(count)