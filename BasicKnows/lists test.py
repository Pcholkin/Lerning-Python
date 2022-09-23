x = [3, 4, 5, 6]
print(len(x))

x = [5, 7, 4]
print(type(x))

x = [5, 7, 4]
x[2] = 5
print(x)

x = (2, 3, 8)
print(type(x))

x = [2, 3, 4]
for element in x:
    element += 3
print(x)

x = [2, 3, 4]
new_x = list()
for element in x:
    new_x.append(element + 10)
print(new_x)

x = [8, 5, 22]
print(sorted(x))

x = [4, 5, 6]
new_x = list()
i = 0
for element in x:
    new_x.append(x[i] + 3)
    i += 1
print(new_x)

x = [1, 5, 8, 9, 10]
print(x[:2])

x = [1, 5, 8, 9, 10]
print(x[3:])            #чего возвращает 2 символа а не 3?


x = [1, 5, 8, 9, 10]
print(x[-2:])           # не понял пока почему 2 и при чем тут (-)

x = [1, 5, 8, 9, 10]
print(x[:33])

x = [1, 5, 8, 9, 10]
print(x[-100:])

x = [1, 5, 8, 9, 10]
print(x[::2])       #каждый второй

x = [1, 5, 8, 9, 10]
print(x[::-1])

x = list(range(101))
print(x[-5:])