with open('4597.txt') as txt:
    count = 0
    max_summ = 0
    nums = list(map(int, txt.readlines()))
    nums_min = min(nums)

    for i in range(len(nums) - 1):
        if ((nums[i] % 117) == nums_min) or ((nums[i+1] % 117) == nums_min):
            count += 1
            max_summ = max(max_summ, nums[i] + nums[i+1])
    print(count, max_summ)
