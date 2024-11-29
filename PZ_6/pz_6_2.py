# Дано число R и список размера N. Найти два различных элемента списка, сумма
# которых наиболее близка к числу R, и вывести эти элементы в порядке возрастания
# их индексов (определение наиболее близких чисел - то есть такой элемент AK, для
# которого величина |AK - R| является минимальной).
def find_closest_elements(R, lst):
    closest_sum = None
    closest_indices = []
    try:
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if closest_sum is None or abs(lst[i] + lst[j] - R) < abs(closest_sum - R):
                    closest_sum = lst[i] + lst[j]
                    closest_indices = [i, j]
        return closest_indices
    except Exception as e:
        print("Ошибка: ", e)

R = int(input("Введите число R: "))
lst = list(map(int, input("Введите список чисел через пробел: ").split()))
closest_indices = find_closest_elements(R, lst)
if closest_indices:
    print("Ближайшие элементы:", lst[closest_indices[0]], lst[closest_indices[1]])
else:
    print("Список пуст или содержит только одно число.")
print("Исходный список",lst)