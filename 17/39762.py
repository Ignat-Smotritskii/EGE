with open('17.39762.txt') as f:
    # list - преобразует элемент в список
    # map  - применяет функцию (int) к каждому элементу коллекции (массив строк)
    numbers = list(map(int, f.readlines()))
    count = 0
    max_sum = 0
    for i in range(len(numbers) - 1):
        if ((numbers[i] * numbers[i + 1]) % 15 == 0) and ((numbers[i] + numbers[i + 1]) % 7 == 0):
            count += 1
            max_sum = max(max_sum, numbers[i] + numbers[i + 1])
    print(count, max_sum)
