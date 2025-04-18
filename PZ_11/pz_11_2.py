# Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое,
# количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
# который поместить текст в стихотворной форме выведя строки в обратном порядке.
# Чтение содержимого файла и вывод на экран
import string
with open('text18-18.txt', 'r', encoding='utf-16') as file:
    lines = file.readlines()
    print("Содержимое файла:")
    for line in lines:
        print(line.strip())

znaki = string.punctuation + "«»„“”‘’—…"
count = 0
for line in lines[:4]:
    for i in line:
        if i in znaki:
            count += 1

print(f"\nКоличество знаков пунктуации в первых 4 строках: {count}")

with open('обратный_порядок.txt', 'w', encoding='utf-8') as file:
    reversed_lines = reversed(lines)
    for line in reversed_lines:
        file.write(line)

print("Файл с обратным порядком строк создан!")