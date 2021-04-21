# На вход программе подаются два целых числа aa и bb (a \le b)(a≤b).
# Напишите программу, которая подсчитывает количество чисел в диапазоне
# от aa до bb включительно, куб которых оканчивается на 44 или 99.

a, b = int(input()), int(input())
if a <= b:
    counter = 0
    for i in range(a, b + 1):
        kub_number_last_digit = (i ** 3) % 10
        if kub_number_last_digit == 4 or kub_number_last_digit == 9:
            counter += 1
        else:
            counter = counter
    print(counter)
else:
    print('Invalid data')
