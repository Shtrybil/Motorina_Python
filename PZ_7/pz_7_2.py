# Дана строка, состоящая из русских слов, разделенных пробелами (одним или
# несколькими). Вывести строку, содержащую эти же слова, разделенные одним
# пробелом и расположенные в обратном порядке.
string = input("Введите строку: ")
words = string.split()
result_string = ' '.join(words[::-1])
print("Исходная строка: ", string)
print("Преобразованная строка: ", result_string)
