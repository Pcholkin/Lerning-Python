def Costs(LPG):

    print(f'How is price of LPG? {LPG}')

def Costs2(GAS):

    print(f'How is price of GAS? {GAS}')

if __name__ == '__main__':

    LPG_100=16      #расход машины на 100 км газа, пока константа
    GAS_100=14      #расход машины на 100 км бенза, пока константа

    LPG = float(input("How is price of LPG?"))  #узнаем стоимость топлива
    GAS = float(input("How is price of GAS?"))

    LPGS = round(LPG_100*LPG, 1)      #умножаем чтобы получить стоимость 100 km
    GASS = round(GAS_100*GAS, 1)

    print(f'100 km by LPG cost {LPGS} Euro')    #показываем стоимость 100 км
    print(f'100 km by GAS cost {GASS} Euro')

    x=float(input('How many kilometers do you want to drive?'))     #узнаем сколько надо проехать км

    HOW_KM_LPG = float(round(x*LPGS/100, 1))    #делим по формуле чтобы узнать расход
    HOW_KM_GAS = float(round(x*GASS/100, 1))

    print(f'Price of {x} KM by LPG = {HOW_KM_LPG} Euro')    #показываем стоимость нужного расстояния
    print(f'Price of {x} KM by GAS = {HOW_KM_GAS} Euro')