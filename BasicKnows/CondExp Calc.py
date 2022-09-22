def read_a_b():
    user_a = float(input('input first number a= '))
    user_b = float(input('input second number b= '))
    return user_a, user_b

exit = False
while not exit:
    print("""
    This is calculator
    1. +
    2. -
    3. *
    4. /
    5. Exit
    """)

    user_input = input('Choose your math operation: ')

    if user_input == '1' or user_input == '+':
        user_a, user_b = read_a_b()
        print(f'{user_a} + {user_b} = {user_a + user_b}')
    elif user_input == '2' or user_input == '-':
        user_a, user_b = read_a_b()
        print(f'{user_a} - {user_b} = {user_a - user_b}')
    elif user_input == '3' or user_input == '*':
        user_a, user_b = read_a_b()
        print(f'{user_a} * {user_b} = {user_a * user_b}')
    elif user_input == '4' or user_input == '/':
        user_a, user_b = read_a_b()
        spl = round(user_a / user_b, 3)
        print(f'{user_a} / {user_b} = {spl}')
    elif user_input == '5' or user_input == 'E':
        exit = True
    else:
        print('Received value not recognized, press enter 1 - 4 or + - * /')