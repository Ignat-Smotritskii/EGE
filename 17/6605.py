with open('6605.txt') as txt:
    nums = list(map(int, txt.readlines()))

count = 0
max_num = -10000
max_dif = -10000

for i in nums:
    max_num = max(max_num, i**2)

for i in range(len(nums) - 1):
    a = nums[i]**2
    b = nums[i+1]**2
    dif = abs(a - b)
    if (dif <= max_num) and ((a % 10 == 5 and b % 10 != 5) or (a % 10 != 5 and b % 10 == 5)):
        count += 1
        max_dif = max(dif, max_dif)
print(count, max_dif)
