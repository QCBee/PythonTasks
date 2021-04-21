# Напишите программу, которая считывает натуральное число nn и
# выводит первые nn чисел последовательности Фибоначчи.

n = int(input())
first_num = 0
second_num = 0
new_pre_1 = 0
new_pre_2 = 1
for i in range(n):
    if i == 0:
        new_num = new_pre_1 + new_pre_2
        print(new_num, end=' ')
    else:
        first_num, second_num = new_pre_1, new_pre_2
        new_num = first_num + second_num
        print(new_num, end=' ')
        new_pre_2 = new_num
        new_pre_1 = second_num
