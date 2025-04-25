# В двумерном списке найти среднее арифметическое элементов последних двух столбцов
import random

a = int(input('Введите количество столбцов: '))
b = int(input('Введите количество строк: '))
lst = [[random.randint(1, 15) for i in range(a)] for i in range(b)]
print("Исходная матрица:")
for row in lst:
    print(row)

last_two = [i for row in lst for i in row[-2:]]
sred = sum(last_two) / len(last_two)
print(f"Среднее арифметическое последних двух столбцов: {sred}")