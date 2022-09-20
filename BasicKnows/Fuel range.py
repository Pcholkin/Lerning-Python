def Trip(distance):

    print(f'What is the range of your trip? {distance}')

def fuel(gasoline):

    print(f'How many gasoline you spended? {gasoline}')

if __name__ == "__main__":

    print("Lets count fuel economy of your car!")
    distance = float(input("What is the range of your trip?"))
    gasoline = float(input("How many gasoline you spended?"))

    ecco = round(gasoline / distance * 100, 1)
    print(f'Fuel economy for 100 km range = {ecco}')

    if ecco<=10:
        print(f'Not bad!')
    else:
        print(f'To much money! No good!')