print('x', 'y', 'z', 'w', 'F')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not(((x <= z) <= y) or not(w)):
                    print(x, y, z, w, 0)
