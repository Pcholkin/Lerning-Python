import math
def square():
    if a == b and b == c and c == d and d == a:  #проверяем что это квадрат
        print('Это таки квадрат!')
        s1 = a ** 2
        print(f'Площадь квадрата = {s1} cm2 ')
        exit()
    else:
        pass


def rect() -> float:  # проверяем что это правельный прямоугольник
    s3 = (a**2) + (b**2)
    s4 = (c**2) + (d**2)
    if s3 == s4:
        print(f'Это прямоугольник!')
        return True
    else:
        pass


def srect():  # считаем площадь прямоугольника
    s5 = a * b
    print(f'Площадь прямоугольника = {s5} cm2')


def perim_rect():  # считаем периметр
    return a + b + c + d


def areaconvrect():  # считаем полупериметр и площадь
    p = perim_rect() / 2
    num = (p - a) * (p - b) * (p - c) * (p - d)
    sqrt = math.sqrt(num)
    return sqrt


def read_sides(name):
    while True:
        x = input(f'{name}')
        try:
            x = float(x)
        except Exception:
            print('Буквы не подходят, цифры надо!')
            continue
        if x > 0:
            return x
        else:
            print('Ну как отрицательная может быть сторона? Давай нормальную цифру!')

print('#' *5)
print('Давай 4 стороны в сантиметрах: ')
print('#' *5)
a = read_sides('a = ')
b = read_sides('b = ')
c = read_sides('c = ')
d = read_sides('d = ')


square()  # проверяем на квадрат

if rect():  # проверяем на правельный прямоугольник
    print(f'{srect()}')
    exit()
            # получается что если это не квадрат и не правельный прямоугольник то это выпуклый прямоугольник
print('Это выпуклый прямоугольник')
print(f'Его периметр = {perim_rect()} cm')
print(f'Его площадь = {areaconvrect()} cm2')