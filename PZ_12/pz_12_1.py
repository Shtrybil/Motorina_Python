#В последовательности на n целых элементов найти произведение элементов
# средней трети
import  random
n = int(input("введите число n"))
lst = []
for num in range(n):
    num = random.randint(0, 50)
    lst.append(num)
print(lst)
n = len(lst)
start = n // 3
end = (2 * n) // 3
res = 1
for x in lst[start:end]:
    res *= x
print("Средняя треть:", lst[start:end])
print("Произведение:", res)