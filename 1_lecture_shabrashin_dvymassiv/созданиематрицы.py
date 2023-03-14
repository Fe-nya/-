#matrix = [[0] * 5] * 3 копируется, каждая первая цифра будет заменена
matrix = [[0] * 5] * [for i in range(3)] #создается новая ячейка памяти
matrix[0][0] = 1
for i in range(len(matrix)):
    print(*matrix)