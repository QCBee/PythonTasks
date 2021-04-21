# Даны три вещественных числа aa, bb, cc. Напишите программу,
# которая находит вещественные корни квадратного уравнения
# Если уравнение имеет два корня, то следует вывести их в порядке возрастания.
from math import sqrt
a, b, c = float(input()), float(input()), float(input())
if a != 0:
    discriminant = pow(b, 2) - 4 * a * c
    if discriminant > 0:
        x1 = (-b + sqrt(discriminant)) / (2 * a)
        x2 = (-b - sqrt(discriminant)) / (2 * a)
        print(min(x1, x2))
        print(max(x1, x2))
    elif discriminant == 0:
        x1 = - b / (2 * a)
        print(x1)
    elif discriminant < 0:
        print('Нет корней')
else:
    x1 = - c / b
    print(x1)