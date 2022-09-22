print('''
Hey! 
I\'m school bot R2D2.
I got task to made new uniform for you,
and I need your sizes.
''')
print('Ok, what\'s your name?')
student = input()
print(f'''
Cool, {student}, what is your gender?
male / female / animal''')
gender = input()

if 'male' in gender:
    print('OK handsome, now how you\'r tall?')
    if 'female' in gender:
        print('OK beauty, now how you\'r tall?')
    elif 'animal' in gender:
        print('Go back to the zoo, you dirty animal!')
else:
    print('hello beauty!')
    print('')