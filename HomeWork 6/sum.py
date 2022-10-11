def is_number(str): #проверяем чтобы небыло букв
    try:
        float(str)
        return True
    except ValueError:
        return False

x = list()

exit = False
while not exit:

    print('Press SUM to + all your numbers.')
    y = input('Your numbers: ')
    is_number(y)  #вызываем функцию для проверки

    if is_number(y) == True:  #тут проверяем или функция дает True - таки цифры
        x.append(float(y))    #переводим строку в цифру и записываем в конец списка

    elif 'sum' in y.lower():  #считываем есть ли введенное кодовое слово
        print(f'Your numbers is: {x}')
        print(f'Summa is : {sum(x)}')
        exit = True
    elif is_number(y) == False:  #опция чтобы тот кто вводит цифры не валял дурака с буквами
        print('Just numbers please..')