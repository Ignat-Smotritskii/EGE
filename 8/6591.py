import itertools

nums = itertools.product('0123456', repeat=5)
count = 0

for i in nums:
    num = ''.join(i)
    if (num.count('6') == 1) and (num[0] != '0') and (num.count('2')*2 + num.count('4')*4 + 6 < num.count('3')*3 + num.count('5')*5 + num.count('1')):
        count += 1
print(count)
