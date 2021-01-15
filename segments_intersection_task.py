# На числовой прямой даны два отрезка. Напишите программу, которая находит их пересечение
# Гарантируется, что b1 > a1 and b2 > a2
a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())
if a1 >= a2 and b1 >= b2:
    print(a1, b1)
elif a2 > a1 and b2 > b2:
    print(a2, b2)
elif a1 != b2 or a2 != b1:
    if a2 > a1 and b1 in (a2, b2):
        print(a2, b1)
    elif b2 in (a1, b1):
        print(a1, b2)
elif a1 == b2:
    print(a1)
elif a2 != b1:
    print(a2)
else:
    print('пустое множество')