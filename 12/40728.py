def f(s: str):
    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)
    return s


max_count = 0
max_i = 0
for i in range(200, 5000):
    string = '1' * i
    string = f(string)
    if max_count < string.count('1'):
        max_count = string.count('1')
        max_i = i

print(max_i)