print('''
Hey! 
I\'m school bot R2D2.
I got task to made new uniform for you,
and I need your sizes.
''')
print('Ok, what\'s your name?')
student = input()

while True:

    print(f'''
Cool, {student}, what is your gender?
boy / girl / animal''') # я сначало написал male и female и потом час ломал голову почему при feMALE отрабатывает MALE.
    gender = str.capitalize(input())

    if 'Boy' in gender:
        print('OK handsome, how you\'r tall?')
        tall_b = int(input())
        if tall_b > 180:
                print('Good, I hope you in basketball team!')
        else:
            print('I got it, next question is: ')
        break
    elif 'Girl' in gender:
            print('OK beauty, how you\'r tall?')
            tall_b = int(input())
            if tall_b > 170:
                    tall_g_num = int(input('I like it, give me your phone number :) : '))  # ну а шо (:
            else:
                    print('I got it, next question is:')
            break

    elif 'Animal' in gender:
        print('Go back to the zoo, you dirty animal!')
        exit()

    else:
        print(f'Are you sure, that {gender} is right value? let\'s  try again:')

while True:
    print('''
What colour gamma you prefer?
We have 3 options:
    1. Gray
    2. Green
    3. Cherry
    4. Black
''')

    color = str.capitalize(input())

    if 'Gray' in color or '1' in color:
        print('Gray it\'s a good choice!')
        break
    elif '2' in color or 'Green' in color:
        print('Green it\'s a good choice!')
        break
    elif '3' in color or 'Cherry' in color:
        print('Good choice!')
        break
    elif '4' in color or 'Black' in color:
        print('Total Black, cool!')
        break
    else:
        print('Not time for games, choice one from list!')


while True:
    print('''
Okay, last question for today, about style:
    
     Classic
     Fashion
     Modern
     Wild
''')
    style = str.capitalize(input('Make a right choice: '))

    if 'Classic' in style:
        print('Of course classic!')
        break
    else:
        print('think again (:')

print(f'''
Okay, I\'ll send this information in s school office:
 
Gender:    {gender}
Tall:      {tall_b}
Student:   {student}
Colour:    {color}
Style:     {style}  
''')
if tall_g_num > 0:
    print('Your phone number I\'ll send to developers office (: ')
else:
    pass

