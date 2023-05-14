from fnmatch import fnmatch

for i in range(1200361, 10 ** 8):
    if fnmatch(str(i), '12??36*1') and (i % 273 == 0):
        print(i, i//273)
