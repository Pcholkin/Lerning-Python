# наверно можно было и так сделать, но что то я решил намудрить.

print('Hey, nice to see you, how\'s your day?')
c1 = input('>> ')
if 'studyed' in c1.lower() or 'school' in c1.lower() or 'work' in c1.lower():
        print('all our life we study or work, how you prefer to rest?')
elif 'sorry' in c1.lower() or 'tired' in c1.lower() or 'sleap' in c1.lower():
        print('I got it, see you next time!')
        exit()
else:
    print('are you sure it\'s in english')
c2 = input('>> ')
if 'games' in c2.lower():
    print('I\'m also love games, my favourite is FORZA Motosport 5')
elif 'movie' in c2.lower() or 'cinema' in c2.lower() or 'film' in c2.lower():
    print('Did you see SNATCH movie with BradPitt?')
    c2_2 = input(">> ")
    if 'yes' in c2_2.lower() or 'cool' in c2_2.lower() or 'best' in c2_2.lower():
        print('I want to watch it for the second time today!')
    elif 'no' in c2_2.lower() or 'don\'t' in c2_2.lower() or 'never' in c2_2.lower():
        print('You missed a lot, It\'s my best recommendation')
    else:
        print('Don\'t worry, maybe later (:')
elif 'youtube' in c2.lower() or 'instagram' in c2.lower() or 'social' in c2.lower():
    print('Social network is my favourite type to change attention from work or study process ')
elif 'walk' in c2.lower() or 'sport' in c2.lower() or 'gym' in c2.lower():
    print('The same, I prefeare park!')
else:
    print('Interesting point, sometimes I need just be alone, and rest.')

print('Sorry, i have to go, my mom\'s coming!')
c3 = input('>> ')
if 'bye' in c3.lower() or 'glad' in c3.lower() or 'ok' in c3.lower() or 'good' in c3.lower():
    print('See you next time!')
else:
    print('sorry, next time man, she calling me... chears!')
    exit()





# сначало сделал так

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

