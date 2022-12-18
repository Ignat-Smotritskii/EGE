import itertools

combinations = itertools.product('РОСМАХ', repeat=8)
uls2 = ['AAРС', 'AAРМ', 'AAРХ', 'AAСР', 'AAСМ', 'AAСХ', 'AAМР', 'AAМС', 'AAМХ', 'AAХР', 'AAХС', 'AAХМ',
        'ООРС', 'ООРМ', 'ООРХ', 'ООСР', 'ООСМ', 'ООСХ', 'ООМР', 'ООМС', 'ООМХ', 'ООХР', 'ООХС', 'ООХМ',
        'AОРС', 'AОРМ', 'AОРХ', 'AОСР', 'AОСМ', 'AОСХ', 'AОМР', 'AОМС', 'AОМХ', 'AОХР', 'AОХС', 'AОХМ',
        'ОAРС', 'ОAРМ', 'ОAРХ', 'ОAСР', 'ОAСМ', 'ОAСХ', 'ОAМР', 'ОAМС', 'ОAМХ', 'ОAХР', 'ОAХС', 'ОAХМ',
        'РСAA', 'РМAA', 'РХAA', 'СРAA', 'СМAA', 'СХAA', 'МРAA', 'МСAA', 'МХAA', 'ХРAA', 'ХСAA', 'ХМAA',
        'РСОО', 'РМОО', 'РХОО', 'СРОО', 'СМОО', 'СХОО', 'МРОО', 'МСОО', 'МХОО', 'ХРОО', 'ХСОО', 'ХМОО',
        'РСОA', 'РМОA', 'РХОA', 'СРОA', 'СМОA', 'СХОA', 'МРОA', 'МСОA', 'МХОA', 'ХРОA', 'ХСОA', 'ХМОA',
        'РСAО', 'РМAО', 'РХAО', 'СРAО', 'СМAО', 'СХAО', 'МРAО', 'МСAО', 'МХAО', 'ХРAО', 'ХСAО', 'ХМAО']
count = 0


def F(s):
    for q in uls2:
        if q in line:
            return False
    return True


for i in combinations:
    line = ''.join(i)
    if line.count('Р') == 1 and line.count('О') == 2 and line.count('С') == 1 and line.count('М') == 1 \
            and line.count('А') == 2 and line.count('Х') == 1 and F(line):
        count += 1
print(count)
