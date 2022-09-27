

def uah_usd(): # переводим из UAH - USD
    print(f'Today\'s currency is: 1 UAH = {c} USD')
    x = (float(input('I know you have UAH, how many?: ')))
    if x <= 1000:
        print(f'Your {x} UAH it\'s {x*c} USD')
    else:
        print(f'Hello rich boy, your {x} UAH it\'s {round(x/c), 2} USD')


def usd_uah(): # переводим из USD - UAH
    print(f'Today\'s currency is: 1 USD = {c1} UAH')
    x = (float(input('USD USD USD! Are you IT guy? How many you want to change?: ')))
    if x <=99:
        print(f'Man, I don\'t have a coins, look in your wallet again!')
    else:
        print(f'Your {x} USD it\'s {x*c1} UAH, now you are rich!')


def dialog():       #получаем данные от пользователя
    x = input('>> ')
    return x

exit = False
while not exit:

    print('''                                

        It\'s currency exchange window.
      Which currency you want to exchange?:         

    ''')

    x = dialog()
    c = 41
    c1 = 36

    if 'usd' in x.lower() or '$' in x or 'dollar' in x.lower() or 'usa' in x.lower():
        usd_uah()
    elif 'uah' in x.lower() or 'hryvna' in x.lower() or 'grn' in x.lower() or 'ua' in x.lower():
        uah_usd()
    else:
        print('Sorry, today only UAH or USD.')      # Я единственное что не понял пока как сделать так чтобы после else
                                                    # опять не выводился print а был тлоько input и после ввода валюты
                                                    # что в наличии уже выполнялось условие. НО я еще подумаю может пойму)))