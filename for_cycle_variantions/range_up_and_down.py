# Даны два целых числа mm и nn. Напишите программу, которая выводит
# все числа от mm до nn включительно в порядке возрастания, если m <n,
# или в порядке убывания в противном случае.

m, n = int(input()), int(input())
if n >= m:
    for i in range(m, n + 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)
