with open('47014.txt') as txt:
    nums = list(map(int, txt.readlines()))
    count = 0
    mid = 0
    max_summ = 0

    for i in nums:
        if i % 2 == 1:
            mid += i
            count += 1
    mid /= count
    count = 0

    for i in range(len(nums) - 1):
        if (nums[i] % 5 == 0 and nums[i+1] < mid) or (nums[i+1] % 5 == 0 and nums[i] < mid):
            count += 1
            max_summ = max(max_summ, nums[i] + nums[i+1])
    print(count, max_summ)
