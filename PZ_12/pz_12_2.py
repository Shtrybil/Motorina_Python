#Составить генератор (yield), который преобразует все буквенные символы в
# строчные.
s = "Hello, World!"
gen = (c.lower() for c in s)
res = ''.join(gen)
print("Исходная строка:", s)
print("Результат:", res)