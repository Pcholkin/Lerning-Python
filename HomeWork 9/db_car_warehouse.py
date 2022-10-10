import json  # импортируем библиотеку для работы с файлами
from pprint import pprint  # для +/- красивого вывода словаря на экран
from uuid import uuid4  # для генерации случайного уникального ID


def show_c_data(d: dict):
    return f'{d["car"]}, is {d["Condition"]} condition,{d["Year"]} model year, paint: {d["Colour"]}, use {d["Fuel type"]} to run, factory in {d["Factory"]}'


def all_index(index_view: dict, id_data: dict):
    for key, values in index_view.items():
        print()
        print(f'Displaying {key} cars: ')
        for id in values:
            print(f'    {show_c_data(id_data[id])}')


db_c = json.load(open('Cars_in_stock.json', mode='r'))  # считываем наш список словарей

id_index = dict()
year_index = dict()  # создаем словари индексов что нам нужны
condition_index = dict()
fuel_type_index = dict()
brand_index = dict()

for car_info in db_c['Cars']:
    car_info['id'] = str(
        uuid4())  # добавляем уникальный ID, ВАЖНО конвертировать в строку, так как изначально uuid4 в байтах
    car_info[
        'car'] = f"{car_info['Brand']} {car_info['Model']}"  # Выводим слитно бренд и модель авто обращаясь в словарь
    id_index[car_info['id']] = car_info

    if car_info['Year'] in year_index:
        year_index[car_info['Year']].append(car_info['id'])  # формируем списки по году выпуска
    else:
        year_index[car_info['Year']] = list()
        year_index[car_info['Year']].append(car_info['id'])

    if car_info['Condition'] in condition_index:
        condition_index[car_info['Condition']].append(car_info['id'])  # формируем списки по новый/Б.У.
    else:
        condition_index[car_info['Condition']] = list()
        condition_index[car_info['Condition']].append(car_info['id'])

    if car_info['Fuel type'] in fuel_type_index:
        fuel_type_index[car_info['Fuel type']].append(car_info['id'])  # формируем списки по типу топлива
    else:
        fuel_type_index[car_info['Fuel type']] = list()
        fuel_type_index[car_info['Fuel type']].append(car_info['id'])

    if car_info['Brand'] in brand_index:
        brand_index[car_info['Brand']].append(car_info['id'])  # формируем списки по бренду
    else:
        brand_index[car_info['Brand']] = list()
        brand_index[car_info['Brand']].append(car_info['id'])

exit = False
while not exit:

    print()
    print('Database of car showroom, what information to show you?')
    print("""
        1. Cars by brand
        2. Cars by year
        3. Cars by condition
        4. Cars by fuel type
        5. Add car
        6. Exit
        """)

    user_input = input('')

    if user_input == '1':
        all_index(brand_index, id_index)
    elif user_input == '2':
        all_index(year_index, id_index)
    elif user_input == '3':
        all_index(condition_index, id_index)
    elif user_input == '4':
        all_index(fuel_type_index, id_index)
    elif user_input == '6':
        exit = True






