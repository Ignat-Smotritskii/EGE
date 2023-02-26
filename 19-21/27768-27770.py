def game(heap1, heap2, moves, to):
    if heap1 + heap2 > 83:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    options = [game(heap1 + 1, heap2, moves + 1, to),
               game(heap1, heap2 + 1, moves + 1, to),
               game(heap1 * 2, heap2, moves + 1, to),
               game(heap1, heap2 * 3, moves + 1, to)]
    return any(options)


def game2(heap1, heap2, moves, to):
    if heap1 + heap2 > 83:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    options = [game2(heap1 + 1, heap2, moves + 1, to),
               game2(heap1, heap2 + 1, moves + 1, to),
               game2(heap1 * 2, heap2, moves + 1, to),
               game2(heap1, heap2 * 3, moves + 1, to)]
    return any(options) if (moves + 1) % 2 == to % 2 else all(options)


print(f'19: {min(s for s in range(1, 68) if game(16, s, 0, 2))}')
print(f'20: {[s for s in range(1, 68) if game2(16, s, 0, 3) and not game2(16, s, 0, 1)]}')
print(f'21: {min(s for s in range(1, 68) if game2(16, s, 0, 4) and not game2(16, s, 0, 2))}')
