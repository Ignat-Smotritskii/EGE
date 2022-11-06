for x in range(10):
    a = int(f'4C{x}4', 15) + int(f'{x}62A', 13)
    if a % 121 == 0:
        print(a//121)
        break