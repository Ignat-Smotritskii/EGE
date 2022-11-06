with open('78276.txt') as txt:
    line = txt.readline()
    max_count = 0
    max_c = '0'
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        p = line.count(f'A{c}')
        if max_count < p:
            max_c = c
            max_count = p
    print(max_c)