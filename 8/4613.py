import itertools

nums = itertools.product('012345678', repeat=5)
count = 0
odd = '01357'

for c in nums:
    num = ''.join(c)
    if (num[0] not in odd) and num[-1] != '1' and num[-1] != '8' \
            and (num.count('3') <= 1):
        count += 1
print(count)
