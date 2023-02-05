def game(heap, moves, to):
    if heap >= 40:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    var = [game(heap + 1, moves + 1, to),
           game(heap + 4, moves + 1, to),
           game(heap * 2, moves + 1, to)]
    return any(var) if (moves + 1) % 2 == to % 2 else all(var)


print(f'19: {min(s for s in range(1, 40) if not game(s, 0, 1) and game(s, 0, 2))}')
print(f'20: {[s for s in range(1, 40) if not game(s, 0, 1) and game(s, 0, 3)]}')
print(f'21: {min(s for s in range(1, 40) if not game(s, 0, 2) and game(s, 0, 4))}')
