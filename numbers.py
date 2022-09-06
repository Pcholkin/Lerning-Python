# x=10
# print(type(x))

# y=12.4
# print(type(y))

# x=5
# print(id(x))
# print(type(x))
# x=2.2
# print(id(x))
# print(type(x))

# x=2+3
# print(f'operation plus (+) ={x}')       # + сложение цифр
#
# y = 10 - 3
# print(f'operation minus (-) = {y}')     # - вычитание
#
# z = 5 * 5
# print(f'operation multiplication (*) = {z}')    # * - умножение
#
# e = 12 / 7
# print(f'operation division (/) = {e}')  # / - деление. Узнать как ограничить количество цифр после точки
#
# r = 12 // 7
# print(f'operation integer division (//) = {r}')  # сколько целых чисел помещаеться в делимом, от есть 12//7=1
#
# q = 10 % 6
# print(f'operation remainder of the division (%) = {q}')  # вотзврат остатка от деление (не понимаю)
#
# t = 3 ** 3
# print(f'operation exponentiation (**) = {t}')       # ** - возведение в степень

def print_hi(n2um):
    print(f'Введи число {n2um}')

#    n2um=input({n2um})

    if n2um % 2 == 0:
        print(f'Число {n2um} четное')
    else:
        print(f'Число {n2um} не четное')
