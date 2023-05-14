txt = open('17_7596.txt')
nums = list(map(int, txt.readlines()))
min_num = 123123123
min_summ = 123123123
count = 0

for q in nums:
    if 99 < q < 1000 and q % 10 == 5:
        min_num = min(q, min_num)

for i in range(len(nums) - 1):
    if ((99 < nums[i] < 1000) and not(99 < nums[i+1] < 1000)) or ((99 < nums[i+1] < 1000) and not(99 < nums[i] < 1000)):
        summ = nums[i] + nums[i+1]
        if summ % min_num == 0:
            count += 1
            min_summ = min(summ, min_summ)
print(count, min_summ)
