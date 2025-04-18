# В двумерном списке элементы кратные 3 увеличить в 3 раза.
lst= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = [[x * 3 if x % 3 == 0 else x for x in i] for i in lst]
for i in result:
    print(i)