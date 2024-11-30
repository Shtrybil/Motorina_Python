# Составить программу, в которой функция генерирует четырехзначное число и
# определяет, есть ли в числе одинаковые цифры
import random

def generate_number():
    while True:
        number = random.randint(1000, 9999)
        digits = set()
        for digit in range(4):
            digit_value = number // (10**(3-digit)) % 10
            if digit_value in digits:
                return number
            else:
                digits.add(digit_value)
        return False

result = generate_number()

if result:
    print("В числе есть одинаковые цифры:", result)
else:
    print("Все цифры в числе различны")

