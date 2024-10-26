#1. Дано вещественное число X и целое число N (> 0). Найти значение выражения
# 1 + X + X^2/(2!) + ... + X^N /(N!) (N! = 12 ...N).
# Полученное число является приближенным значением функции exp в точке X.
X = input('Введите вещественное число Х: ')
N = input('Введите целое число N: ')
while type(X) != float:
    try:
        X = float(X)
    except ValueError:
        print('Некорректный ввод Х')
        X = input('Введите вещественное число Х: ')

while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print('Некорректный ввод N')
        N = input('Введите целое число N: ')
if N <= 0:
  print("N должно быть положительным целым числом.")
else:
  result = 1.0
  for i in range(1, N + 1):
    factorial = 1
    for j in range(1, i + 1):
      factorial *= j # Вычисляем факториал i
    result += X ** i / factorial # Добавляем член ряда

  print(f"Приближенное значение exp({X}) с {N} членами ряда: {result}")