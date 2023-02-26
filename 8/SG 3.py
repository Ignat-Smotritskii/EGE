import itertools

count = 0
odd = '1357'
nums = [''.join(c) for c in itertools.product('01234567', repeat=11)]

for c in nums:
    if (c[0] != '0') and (c.count('1') + c.count('3') + c.count('5') + c.count('7') == 3):
        flag = True
        for q in range(10):
            if c[q] in odd and c[q+1] in odd:
                flag = False
        if flag:
            count += 1
print(count)
