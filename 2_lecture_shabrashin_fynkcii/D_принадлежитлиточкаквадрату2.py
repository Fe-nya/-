# https://informatics.msk.ru/mod/statements/view.php?id=3962&chapterid=3793#1

# def IsPointInSquare(x, y):
#    if abs(x) + abs(y) <= 1:
#        return True
#    return False


def IsPointInSquare(x, y):
    return abs(x) + abs(y) <= 1


one = float(input())
two = float(input())
if IsPointInSquare(one, two):  # это тоже самое, что if IsPointInSquare(one, two) == True:
    print('YES')
else:
    print('NO')
