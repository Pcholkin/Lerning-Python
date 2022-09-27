

def uah_usd():
    x = (float(input('I know you have UAH, how many?: ')))
    if x <= 1000:
        print(f'Your {x} UAH it\'s {x*c} USD')
    else:
        print(f'Hello rich boy, your {x} UAH it\'s {round(x/c), 2} USD')


def usd_uah():
    x = (float(input('USD USD USD! Are you IT guy? How many you want to change?: ')))
    if x <=99:
        print(f'Man, I don\'t have a coins, look in your wallet again!')
    else:
        print(f'Right way! Your {x} USD it\'s {x*c} UAH, now you are rich!')


def dialog():
    print('''
    
    It\'s currency exchange window.
  Which currency you want to exchange?:

''')
    x = input('>> ')
    return x

def wrong():
    print('Sorry, today only UAH or USD.')
    x = input('>> ')
    return x

exit = False
while not exit:

    x = dialog()
    c = 40

    if 'usd' in x.lower() or '$' in x or 'dollar' in x.lower() or 'usa' in x.lower():
        usd_uah()
    elif 'uah' in x.lower() or 'hryvna' in x.lower() or 'grn' in x.lower() or 'ua' in x.lower():
        uah_usd()
    else:
        wrong()