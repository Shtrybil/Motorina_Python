# Для задачи из блока 1 создать две функции, save_def и load_def, которые позволяют
# сохранять информацию из экземпляров класса (3 шт.) в файл и загружать ее обратно.
# Использовать модуль pickle для сериализации и десериализации объектов Python в бинарном формате.
import pickle
from PZ_16.pz_16_1 import c1, c2, c3

def save_def(circles, file):
    with open(file, 'wb') as f:
        pickle.dump(circles, f)

def load_def(file):
    with open(file, 'rb') as f:
        return pickle.load(f)

# Сохраняем круги в файл
save_def([c1, c2, c3], 'circles.pkl')

# Загружаем
loaded = load_def('circles.pkl')
for c in loaded:
    print(f"Радиус: {c.r}, Площадь: {c.area():.1f}")