import json
import os

main_file = 'test.json'

if os.path.isfile(main_file):
    my_base = json.load(open(main_file))
else:
    my_base = {"Cars":""}

print(my_base)

brand = input('Brand: ')
model = input('Model: ')
year = input('Year: ')
factory = input('Factory: ')
colour = input('Colour: ')
cond = input('Condition: ')
fuel_t = input('Fuel type: ')

car_info = {
      "Brand": brand,
      "Model": model,
      "Year": year,
      "Factory": factory,
      "Colour": colour,
      "Condition": cond,
      "Fuel type": fuel_t
    }


my_base = (my_base, car_info)

print(my_base)

json.dump(my_base, open(main_file, mode='w'), indent=4)

