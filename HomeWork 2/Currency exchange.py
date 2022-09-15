
# обмен сюда/туда :)

x=float(input(f'Enter amount of $'))
y=float(input(f'Enter rate'))
print(f' you get {round(x*y, 2)} in UAH')
print(f'if you have {x*y} UAH, for today rate {y} - it\'s about {round((x*y)/y, 2)} USD')