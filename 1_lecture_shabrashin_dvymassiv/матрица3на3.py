matrix = []
for i in range(5): #высота
    a = [0 for i in range(3)] #ширина
    matrix.append(a)

for i in range(len(matrix)):
    print(*matrix[i])
print(matrix)