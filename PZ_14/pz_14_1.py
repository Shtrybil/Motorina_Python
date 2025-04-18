# Из исходного текстового файла (expansion.txt) выбрать имена фалов,
# соответствующие типам: .xls, .xml, .html, .css, .py. Посчитать количество полученных
# элементов.
import re
with open('expansion.txt', 'r', encoding='utf-8') as file:
    f = file.read()

reg = r'\b\w+\.(?:xls|xml|html|css|py)\b'

# Поиск всех совпадений
files = re.findall(reg, f)

count = len(files)

print("Найденные файлы:", files)
print("Количество файлов:", count)