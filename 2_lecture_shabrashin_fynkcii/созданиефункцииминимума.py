def minimum(a, b):
    if a < b:
        return a  # возвращает результат цикла if, дальнейший цикл не работает
    return b


a = minimum(4, 6)  # позиционный тип аргумента
print(a)