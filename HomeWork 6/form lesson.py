

x = [5, 6, 7, 10, 'text', 'text2', [10, 30, 'text3']]
print(x)
print(type(x))

#самый простой вариант обращатся к спискам
print(x[0])  #выводим на экран нулевой элемент (программа считает с 0)
print(x[1])  #выводим первый
print(x[-1])  #выводим последний, в нашем случае это подсписок

# print(x[7]) - ошибка, в не дипапзона 7, всего 6 элементов

print(f'{len(x)}') #length - длинна списка

y = [5, 3, 6, 78, 7777, 54, 45, 2, -5, -67]

# динамическая по-элементная операция над списком любой длинны
# цикл for!
for element in y: # для каждого елемента в списке у делаем следующее:
    print(element **2, end=', ')

print('\n', y)

y = [5, 3, 6, 78, 7777, 54, 45, 2, -5, -67]
y_second = list() # пустой список
# динамическая по-элементная операция над списком любой длинны
# цикл for!
for element in y: # для каждого елемента в списке 'у' делаем следующее:
    y_second.append(element ** 2)

print('#' *10)
print(y, y_second)
print('#' *10)

# посчитать сумму елементов списка
y = [1, 5, 6, 8, 45, -34, 23, 4, -545, 5]
summa = 0
for element in y:
    summa += element #оператор накапливания (increment)
print(summa)
print(sum(y)) # sum - это встроенный метод подсчета в python

# ручное итерирование
iterator = 0
change_y = list()
for element in y:
    print((f'{element} это {iterator}-ый элемент списка'))
    if iterator < 4:
        procces_element = element - 100
        change_y.append(procces_element)
    else:
        procces_element = element + 100
        change_y.append(procces_element)
    iterator +=1
print(f'Past: {y}')
print(f'Now: {change_y}')

# итерирование встроенным методом
for element in enumerate(y):
    print(f'{element[1]} это {element[0]} - ый элемент списка')
   # print(type(element) - tuple - это кортеж

# операции с кортежами
t = (4, 7, 36, 8) # tuple в круглых скобках
print(len(t))
print(sum(t))
print(t[-1])
print(t[0])

t = tuple([5, 7, 54, 'python', False])
conv_tuple = list(t)
conv_tuple[0] = 99
print(t)
print(conv_tuple)

#instance - мы спрашиваем является ли...
print(type(t))
#print(isinstance(t, tuple)) # является ли t кортежем полкчим True
if isinstance(t, tuple):
    t = list(t)
t[0] = 5
print(type(t))
print(t)

x = [6, 5, 3, 55, 'True']  # динамическое обращение к спискам и поиск
if isinstance(x, str):
    print(x.capitalize())
elif isinstance(x, int):
    print(x / 5)
else:
    print(x)

if x:  # проверка на не 0 или на пустоту
       # хотя бы один елемент в списке не важно какой - True
    print('x is True')
else:
    print('x is False')

x = [4, 5, 7, 88, -4, -43] # found MIN and MAX in X
print(f'{min(x)=} ')
print(f'{max(x)=} ')

print(sorted(x)) #сортирует, возращает сортированное а сам список не меняет
print(x)

x.sort() # сортирует список меняя его
print(x)

print(sorted(x, reverse=True)) #сортирует в обратном порядке

sack_of_fruits = [
    ("apple", 20),
    ("Pinnapple", 37),
    ("watermelon", 790),
    ("stroberry", 15),
]
print(sack_of_fruits)


def get_fruit_weight(element): #сортируем по второму елементу от минимума и до максимума
    return element[1]


print('sorted by weight', sorted(sack_of_fruits, key=get_fruit_weight))
print('min', min(sack_of_fruits, key=get_fruit_weight))
print('max', max(sack_of_fruits, key=get_fruit_weight))

def get_fruit_name(element):  # сортируем по алфавиту, регистр влияет!
    return element[0].lower() #тут мы написали LOWER для того чтобы в стортировке код видел все нижние буквы

print('sorted by name', sorted(sack_of_fruits, key=get_fruit_weight))
print('min A - Z', min(sack_of_fruits, key=get_fruit_name))
print('max Z - A', max(sack_of_fruits, key=get_fruit_name))


import os

print(os.listdir()) #посмотрели какие есть файлы в директории

for filename in os.listdir():  # цикл работает так: для файлов в нашей папке
    if '.py' not in filename:  # если расширение .ру нет в названии
        os.remove(filename)    # удалить файлы нахер

# slice -

x = [1, 2, 3, 45, 56, 3, 23, 22, 36]
print(len(x))  # показываем длинну
print(x[:4])  # показываем елемент сначало и до 4 элемента
print(x[4:])  # показать с 4 и до конца
print(sorted(sack_of_fruits, key=get_fruit_weight)[:3])

print(x[::2])  #показать Х от начала до конца с шагом 2
print(x[::-1])  #простой способ получить обратный список

x.reverse()  # так же возращает обратный список
print(x)

x = [1, 2, 3, 45, 56, 3, 23, 22, 36]
i = 0
while i < len(x):
    element = x[i]
    #do something
    print(element)
    i +=1