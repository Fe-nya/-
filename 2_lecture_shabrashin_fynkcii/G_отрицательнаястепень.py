# https://informatics.msk.ru/mod/statements/view.php?id=3962&chapterid=3796#1 похожа на задачу K, эту через цикл

def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(a, -n)
    else:
        return a * power(a, n - 1)  # a в степени n это a * a в степени n-1


# a = float(input())
# n = int(input())
print(power(2, 100))