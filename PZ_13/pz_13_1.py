# В двумерном списке элементы кратные 3 увеличить в 3 раза.
import  random

a = int(input('Введите количество столбцов: '))
n = int(input('Введите количество строк: '))
lis_gen = ([random.randint(1, 15) for i in range(a)] for i in range(n))
listik = list(lis_gen)
print("Исходная матрица:")
for row in listik:
    print(row)

print("\nИзмененная матрица:")
result = [[x * 3 if not x % 3 else x for x in i] for i in listik]
for i in result:
    print(i)