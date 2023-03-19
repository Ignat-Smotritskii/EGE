def game(heap, move, to):
    if heap >= 165:
        return move % 2 == to % 2
    if move == to:
        return 0
    var = [game(heap + 1, move + 1, to),
           game(heap + 4, move + 1, to),
           game(heap * 2, move + 1, to)]
    return any(var) if (move + 1) % 2 == to % 2 else all(var)


print(f'19: {min(s for s in range(1, 164) if not game(s, 0, 1) and game(s, 0, 2))}')
print(f'20: {[s for s in range(1, 164) if not game(s, 0, 1) and game(s, 0, 3)]}')
print(f'21: {min(s for s in range(1, 164) if not game(s, 0, 2) and game(s, 0, 4))}')
