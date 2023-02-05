with open('37369.txt') as txt:
    nums = list(map(int, txt.readlines()))
    count = 0
    max_dex = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if (nums[i] - nums[j]) % 80 == 0:
                count += 1
                max_dex = max(max_dex, abs(nums[i] - nums[j]))
    print(count, max_dex)