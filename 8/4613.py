import itertools

nums = itertools.product('012345678', repeat=5)
count = 0

for c in nums:
    num = ''.join(c)
    if (num[0] == '2' or num[0] == '4' or num[0] == '6' or num[0] == '8') and num[-1] != '1' and num[-1] != '8' \
            and (num.count('3') <= 1):
        count += 1
print(count)
