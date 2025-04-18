#В последовательности на n целых элементов найти произведение элементов
# средней трети
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(nums)
start = n // 3
end = (2 * n) // 3
res = 1
for x in nums[start:end]:
    res *= x
print("Средняя треть:", nums[start:end])
print("Произведение:", res)