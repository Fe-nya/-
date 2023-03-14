# https://informatics.msk.ru/mod/statements/view.php?id=3962&chapterid=3790#1

def min4(a, b, c, d):
    i = min(a, b)
    j = min(c, d)
    return min(i, j)


a = int(input())
b = int(input())
rr = int(input())
d = int(input())
print(min4(a, b, rr, d))
