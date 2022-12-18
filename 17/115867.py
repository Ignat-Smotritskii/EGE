s = 0
max_num = -10001
max_summ = 0
with open('115867.txt') as txt:
    nums = list(map(int, txt.readlines()))
    for i in range(len(nums)):
        if nums[i] > max_num and abs(nums[i]) % 10 == 3:
            max_num = nums[i]
    for i in range(len(nums) - 1):
        if ((abs(nums[i]) % 10 == 3 and abs(nums[i+1]) % 10 != 3) or (abs(nums[i+1]) % 10 == 3 and abs(nums[i]) % 10 != 3)) and (nums[i] ** 2 + nums[i+1] ** 2 >= max_num ** 2):
            s += 1
            max_summ = max(max_summ, nums[i] ** 2 + nums[i + 1] ** 2)
    print(s, max_summ)