#2. Даны три числа. Найти среднее из них (то есть число, расположенное между наименьшим и наибольшим).
a = input('введите 1-е число: ')
b = input('введите 2-е число: ')
c = input('введите 3-е число: ')
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print('неправильно ввели 1 число')
        a = input('введите 1-e число: ')

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print('неправильно ввели 2 число')
        b = input('введите 2-e число: ')

while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print('неправильно ввели 3 число')
        c = input('введите 3-e число: ')
if a < b < c or a > b > c:
    print(f"Среднее число: {b}")
elif a > b < c or a < b > c:
    print(f"Среднее число: {a}")
else:
    print(f"Среднее число: {c}")
