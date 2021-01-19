# Даны две различные клетки шахматной доски.
# Напишите программу,  которая определяет, может ли король
# попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки,
# потом для второй клетки. Программа должна вывести «YES»,
# если из первой клетки ходом короля можно попасть во вторую, или «NO» в противном случае.
ax, ay, bx, by = int(input()), int(input()), int(input()), int(input())
max_value = 8
min_value = 1
if min_value <= ax <= max_value and min_value <= ay <= max_value and min_value <= bx <= max_value and min_value <= by <= max_value:
    if 0 <= by - ay <= 1 and (-1 <= bx - ax <= 0 or -1 <= bx - ax <= 1):
        print('YES')
    else:
        if -1 <= bx - ax <= 1:
            if -1 <= by - ay <= 1:
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
else:
    print('NO')
