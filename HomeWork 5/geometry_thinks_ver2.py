def square():
    if a == b and b == c and c == d and d == a:  #проверяем что это квадрат
        print('Sponge Bob square pans will happy! It\'s square!')
        s1 = a ** 2
        print(f'Square area = {s1} cm2 ')
        exit()
    else:
        pass


def rect() -> float:  # проверяем что это правельный прямоугольник
    s3 = (a**2) + (b**2)
    s4 = (c**2) + (d**2)
    if s3 == s4:
        print(f'This is rectangle!')
        return True
    else:
        pass
    #return s3, s4


def srect():  # считаем площадь правильного прямоугольника
    s5 = a * b
    print(f'Rectangle area = {s5} cm2')


def perim_rect():
    return a + b + c + d


def areaconvrect():  # функция определяющая не правельный прямоугольник и подсчета его площади
    p = perim_rect() / 2
    q = pow(p - a) * (p - b) * (p - c) * (p - d) * 0.5)
    return q


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
print('Давай 4 стороны: ')
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
print(f'Его периметр = {perim_rect()} ')
print(f'Его площадь = {areaconvrect()}')