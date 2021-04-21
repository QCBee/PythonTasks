# Даны два целых числа mm и nn ( m \le nm≤n).
# Напишите программу, которая выводит все числа от mm до nn включительно.

n, m = int(input()), int(input())
for i in range(n, m + 1):
    print(i)
