# conditional expressions

s = 5
if 2 + 2 == s:  #если (некое условие)
    print('Math rools good!')
else: #иначе
    print('Math not true!')

a = 55
b = 7
if a > b:
    print(f'{a} is greater than {b}')
else:
    print(f'{a} is lesser than {b}')

print (a > b)

g = True #истинно
f = False #ложно

print(f'{type(a < b)=}')
print(f'{g=} {type(g)=}')
print(f'{f=} {type(f)=}')

#если условное выражение не типа bool, то проверяется не-ноль или не-пустота

h = 0.00001
if h:
    print('h is True')
else:
    print('h is False')

s = 'If we have a string?'
if s:
    print('s is True')
else:
    print('s is False')

# это базовое написание условий но много строк и текста.

color = 'Blue'
price = 10.0
if color == 'Blue':
    print(f'{color} цвет подходит какая цена?')
    if price < 10.1:
        print(f'цвет {color} ок цена {price} ок')
    else:
        print(f'цвет {color} ок но {price} дорого')
else:
    print(f'{color} не тот цвет')
print('###############################')
# ниже пример по оптимизации через логический операторы

color = 'Blue'
price = 10.2
if color == 'Blue' and price < 10.1: # логическое и (and)
    print(f'цвет {color} ок цена {price} ок')
else:
    print('или цена или цвет не подходит')

#рассмотрим логическое или 'or'
# in - в, оператор членства, есть ли что то в чем то

order = 'coffee,tea' #даже если написать все в 1 строчку без запятой будет работать. Регистр влияет!
if 'coffee' in order or 'cacao' in order: #хотя бы 1 условие должно сработать. Если 0 условий совпало тогда else
# if 'coffee' in order.lower() or 'cacao' in order.lower(): - если надо выровнять регистр
    print('This Menu is fine')
else:
    print('This menu don\'t included coffee of cacao' )

#расстояние Левенштайна (как работают поисковики когда заменяют правописание)

