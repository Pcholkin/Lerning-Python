# def user_num():
#     num_a = float(input('Enter number: '))
#     return num_a

# exit = False
# while not exit:
num_a = 0
if num_a <= -500:
        print(f'{num_a}  больше или равно -500')
        #num_a = user_num()
elif num_a <= -100 or num_a > -500:
        #num_a = user_num()
        print(f'{num_a} меньше чем -100 но больше чем -500')
        #num_a = user_num()
elif num_a < 0 or num_a > -100:
        print(f'{num_a} меньше нуля но больше -100')
        #num_a = user_num()
elif num_a > 100 or num_a >=0:
        print(f'{num_a} равно или больше 0 но меньше 100')
        #num_a = user_num()
elif num_a < 500 or num_a >=100:
        print(f'{num_a} равно или больше 100 но меньше 500')
        #num_a = user_num()
elif num_a >= 500:
        print(f'{num_a} больше или равно 500')
else:
        print('the end')