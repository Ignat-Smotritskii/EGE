const = 5 + 7 * 80 + 4 * 80**2 + 4 * 80**3
max_dex = 0
for x in range(80):
    a = const + x * 80 + x * 80**2
    if a % 17 == 0:
        max_dex = max(a // 17, max_dex)
print(max_dex)
