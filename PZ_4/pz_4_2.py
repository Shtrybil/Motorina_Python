#2. Даны целые положительные числа A и B (A < B). Вывести все целые числа от A до
#B включительно; при этом каждое число должно выводиться столько раз, каково его
#значение (например, число 3 выводится 3 раза).
A = input('Введите А: ')
B = input('Введите В: ')
while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print('Некорректный ввод A!')
        A = input('Введите А: ')
while type (B) != int:
    try:
        B = int(B)
    except ValueError:
        print('Некорректный ввод B!')
        B = input('Введите В: ')
if A < B and A > 0 and B > 0:
  i = A
  while i <= B:
    count = 1
    while count <= i:
      count += 1
      print(i, end=" ")
    i += 1
else:
  print("Некорректный ввод. A должно быть меньше B и оба числа должны быть положительными.")

