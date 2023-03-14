# https://informatics.msk.ru/mod/statements/view.php?id=3962#1

def distance(x1, x2, y1, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  # **0.5 вычисление корня


a = float(input())
b = float(input())
c = float(input())
y2 = float(input())
print(distance(a, b, c, y2))
