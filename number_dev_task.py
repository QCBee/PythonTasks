# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
num = int(input())
third_num = num % 10
second_num = (num % 100) // 10
first_num = num // 100
summa = third_num + second_num + first_num
proiz = third_num * second_num * first_num
print('Сумма цифр', summa, sep=' = ')
print('Произведение цифр', proiz, sep=' = ')
