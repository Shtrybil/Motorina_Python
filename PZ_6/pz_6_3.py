# Дан список размера N, все элементы которого, кроме первого, упорядочены по
# возрастанию. Сделать список упорядоченным, переместив первый элемент на новую
# позицию.
lst = input("Введите элементы списка через пробел: ").split()
print("Исходный список", lst)
if not lst:
    print("Список пуст")
else:
    try:
        lst.sort()
    except Exception as e:
        print("Ошибка при перемещении элемента:", e)
print("Преобразованный список", lst)




