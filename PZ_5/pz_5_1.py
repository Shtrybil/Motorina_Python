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
                    return number
                else:
                    digits.add(digit)
            return False
        except ValueError:
            pass

result = generate_number()

if result:
    print("В числе есть одинаковые цифры:", result)
else:
    print("Все цифры в числе различны")
