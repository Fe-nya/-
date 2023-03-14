# https://informatics.msk.ru/mod/statements/view.php?id=3962&chapterid=3792#1

# конструкция if излишняя
# def IsPointInSquare(x, y):
#     if -1 <= x <= 1 and -1 <= y <= 1:
#         return True
#     return False


def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


one = float(input())
two = float(input())
if IsPointInSquare(one, two):  # это тоже самое, что if IsPointInSquare(one, two) == True:
    print('YES')
else:
    print('NO')
