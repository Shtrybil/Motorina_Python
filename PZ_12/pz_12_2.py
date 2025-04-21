#Составить генератор (yield), который преобразует все буквенные символы в
# строчные.

def lower_gen(text):
    for i in text:
        yield i.lower()

text = "От УЛЫБКИ хмурый день СВЕТЛЕЙ!"
chars = [char for char in lower_gen(text)]
print(''.join(chars))
