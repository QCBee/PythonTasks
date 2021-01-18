# На числовой прямой даны два отрезка. Напишите программу, которая находит их пересечение
# Гарантируется, что b1 > a1 and b2 > a2
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a2 <= a1 <= b2 and a2 <= b1 <= b2:
    print(a1, b1)
elif a1 <= a2 <= b1 and a1 <= b2 <= b1:
    print(a2, b2)
elif (a2 <= a1 <= b2) and b1 > b2:
    if a1 != b2:
        print(a1, b2)
    else:
        print(a1)
elif (a1 <= a2 <= b1) and b2 > b1:
    if a2 != b1:
        print(a2, b1)
    else:
        print(a2)
else:
    print('пустое множество')
