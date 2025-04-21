#В последовательности на n целых элементов найти произведение элементов
# средней трети
import  random
n = int(input("введите число n: "))
lst = []
for num in range(n):
    num = random.randint(1, 50)
    lst.append(num)
print(lst)

start = n // 3
end = 2 * n // 3
lst2 = [lst[i] for i in range(start, end)]
from functools import reduce
result= reduce(lambda x, y: x * y, lst2, 1)
print(f"Произведение средней трети: {result}")