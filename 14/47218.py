for x in range(10):
    a = int(f'123{x}5', 15) + int(f'1{x}233', 15)
    if a % 14 == 0:
        print(a//14)
        break