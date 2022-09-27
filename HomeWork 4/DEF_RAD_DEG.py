import math


def rad_to_d():
    x = (float(input('How many radians you have?: ')))
    print(f'> Man, {x} RAD it\'s about {math.degrees(x)} DEG, crazy...')


def deg_to_r():
    z = float(input('I know you have some DEG? how many?: '))
    print(f'> Your {z} DEG it\'s only {math.radians(z)} RAD, i hope you like it!')


def read_user():
    print('''

     Radians / Dergees mixer: 

     1. RAD > DEG
     2. DEG > RAD
     3. Sorry i want to mommy!     
    ''')
    x = input('Make your choice!: ')
    return x


exit = False
while not exit:

    x = read_user()

    if '1' in x or 'rad' in x.lower():
        rad_to_d()
        exit = True
    elif '2' in x or 'deg' in x.lower():
        deg_to_r()
        exit = True
    elif '3' in x or 'sorry' in x.lower() or 'mommy' in x.lower():
        exit = True
    else:
        print('> Don\'t mess with me! Lets start again...')
