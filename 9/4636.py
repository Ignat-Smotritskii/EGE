with open('4636.txt') as txt:
    count = 0
    for line in txt:
        nums = list(map(int, line.split('\t')))
        if (max(nums) - min(nums) >= 50) and (nums[0] * nums[1] * nums[2] * nums[3] // max(nums) // min(nums) <= 1000):
            count += 1
    print(count)
