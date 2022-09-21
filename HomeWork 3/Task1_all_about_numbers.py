def user_num():
    num_a = float(input('Enter number: '))
    return num_a

exit = False
while not exit:

        num_a = user_num()

        if num_a <= -500:
                print(f'{num_a} <= -500')
        elif num_a > -500 and num_a <= -100: # при and должны совпасть оба условия - тогда True
                print(f'{num_a} > -500 and <= -100')
        elif num_a < 0 and num_a > -100:
                print(f'{num_a} < 0 and > -100')
        elif num_a >= 0 and num_a < 100:
                print(f'{num_a} >= 0 and < 100')
        elif num_a >= 100 and num_a < 500:
                print(f'{num_a} >= 100 and < 500')
        elif num_a >= 500:
                print(f'{num_a} >= 500')
