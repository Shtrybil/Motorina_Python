# В двумерном списке найти среднее арифметическое элементов последних двух столбцов
import random

a = int(input('Введите количество столбцов: '))
b = int(input('Введите количество строк: '))
lst = [[random.randint(1, 15) for i in range(a)] for i in range(b)]

print("Исходная матрица:")
for row in lst:
    print(row)

last_two = []
for row in lst:
    last_two.extend(row[-2:])  # Добавляем последние два элемента каждой строки

sred = sum(last_two) / len(last_two)
print(f"Среднее арифметическое последних двух столбцов: {sred}")