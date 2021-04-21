# Даны названия трех городов.
# Напишите программу, которая определяет самое короткое и самое длинное название города.
city1, city2, city3 = input(), input(), input()
mini_l = min(city1, city2, city3, key=len)
print(mini_l)
maxi_l = max(city1, city2, city3, key=len)
print(maxi_l)
