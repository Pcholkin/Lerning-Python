
def squ():# проверяет что это квадрат
    if a == b and b == c and c == d and d == a:
        print('Sponge Bob square pans will happy! It\'s square!')
        s1 = a**2
        print(f'Square area = {s1} cm2 ')
    else:
        pass


def rect():  # проверяет что это правельный прямоугольник
    s3 = (a**2) + (b**2)
    s4 = (c**2) + (d**2)
    if s3 == s4:
        print(f'This is rectangle!')
    else:
        pass
    return s3, s4

def srect():  # считаем площадь правильного прямоугольника
    s5 = a * b
    print(f'Rectangle area = {s5} cm2')

#def convrect(): # методом исчисления понимаем что если есть 4 стороны  что это опуклый прямоугольник
#    if


def enter(): # получаем данные
    a = float(input('Side A = '))
    b = float(input('Side B = '))
    c = float(input('Side C = '))
    d = float(input('Side D = '))

    if a <= 0 or b <= 0 or c <= 0 or d <=0:
        print('All four sides have to be more than 0. Try again!')
        enter()
    else:
        pass

    return a, b, c, d  # вечер убил чтобы разобраться что в этом случае возращается кортеж


exit = False
while not exit:
    print('Give me four sides: ')

    a, b, c, d = enter()  # ввели данные
    if squ():   # проверяем на квадрат
        print('Сработал квадрат')
    elif rect(): # если не квадрат то проверяем на правельный прямоугольник
        srect()
        print('сработал прямоугольник')
else:
    pass

#s3, s4 = rect()
#    if s3 == s4:


