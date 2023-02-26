with open('SG 3.txt') as txt:
    nums = list(map(int, txt.readlines()))
count = 0
min_num = 0
max_sum = 0
for c in nums:
    if abs(c) % 10 == 3:
        min_num = min(c, min_num)

for i in range(len(nums) - 1):
    if ((abs(nums[i]) % 10) == (abs(nums[i+1]) % 10)) and \
            (((nums[i] % 3 == 0) and (nums[i+1] % 3 != 0)) or ((nums[i+1] % 3 == 0) and (nums[i] % 3 != 0))) and \
            ((nums[i]**2 + nums[i+1]**2) <= min_num**2):
        count += 1
        max_sum = max(max_sum, nums[i]**2 + nums[i+1]**2)
print(count, max_sum)
