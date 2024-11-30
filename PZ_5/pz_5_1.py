# Составить программу, в которой функция генерирует четырехзначное число и
# определяет, есть ли в числе одинаковые цифры
import random

def generate_number():
    while True:
        number = random.randint(1000, 9999)
        try:
            digits = set()
            for digit in str(number):
                if digit in digits:
                    return number # Вернуть число, если найдена одинаковая цифра
                else:
                    digits.add(digit)
            return False  # Если все цифры уникальны
        except ValueError:
            print('Ошибка!')

result = generate_number()

if result:
    print("В числе есть одинаковые цифры:", result)
else:
    print("Все цифры в числе различны")
