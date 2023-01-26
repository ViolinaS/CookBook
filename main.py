from pprint import pprint
"""
Чтение списка рецептов из файла recipes.txt и  преобразование в словарь cook_book
"""


def read_recipes_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def split_text_in_list(text):
    return [lines.splitlines() for lines in text.split('\n\n')]


def split_ingredients_in_dishes(dish):
    return dish[:1] + [lines.replace(' ', '').split('|') for lines in dish[2:]]


def dishes_to_dictionary(dish):
    return {
        dish[0]: [{
            'ingredient_name': line[0],
            'quantity': int(line[1]),
            'measure': line[2]
        } for line in dish[1:]]
    }


def cook_book_dict_data(file_path):
    cook_book_dict = {}
    text = read_recipes_file(file_path)
    dish_list = split_text_in_list(text)
    format_dish_list = [
        split_ingredients_in_dishes(lines) for lines in dish_list
    ]
    for lines in format_dish_list:
        cook_book_dict.update(dishes_to_dictionary(lines))
    return cook_book_dict


"""
Расчет необходимого количества ингредиентов на основании списка блюд из словаря cook_book и количества персон
"""


def dishes_to_shop_list(dish):
    return {
        dish[0]: {
            line[0]: {
                'measure': line[2],
                'quantity': int(line[1])
            }
            for line in dish[1:]
        }
    }


def shop_list_data(file_path):
    shop_ingredients = {}
    text = read_recipes_file(file_path)
    dish_list = split_text_in_list(text)
    format_dish_list = [
        split_ingredients_in_dishes(lines) for lines in dish_list
    ]
    for lines in format_dish_list:
        shop_ingredients.update(dishes_to_shop_list(lines))
    return shop_ingredients


def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = shop_list_data('recipes.txt')
    list_to_buy = {}
    if dishes in shop_list_by_dishes:
        list_to_buy.update(shop_list_by_dishes[dishes])
        for key, val in list_to_buy.items():
            val['quantity'] = val['quantity'] * person_count
        return list_to_buy
    else:
        print('Такого блюда в рецептах нет')


"""
На выходе получаем новый словарь с названием ингредиентов и его количества для конкретного блюда из списка рецептов.
"""
if __name__ == '__main__':
    cook_book = cook_book_dict_data('recipes.txt')
    print('Задание № 1 - вывод словаря cook_book:\n')
    pprint(cook_book)
    print('\nЗадание № 2 - вывод списка покупок на количество персон\n')
    shop_list_1 = get_shop_list_by_dishes(dishes='Фахитос', person_count=2)
    shop_list_2 = get_shop_list_by_dishes(dishes='Омлет', person_count=2)
    shop_list_3 = get_shop_list_by_dishes(dishes='Запеченный картофель',
                                          person_count=2)
    shop_list_4 = get_shop_list_by_dishes(dishes='Утка по-пекински',
                                          person_count=2)
    print('Список для Фахитос:\n')
    pprint(shop_list_1)
    print('\nСписок для Омлета:\n')
    pprint(shop_list_2)
    print('\nСписок для Запеченного картофеля:\n')
    pprint(shop_list_3)
    print('\nСписок для Утки по-пекински:\n')
    pprint(shop_list_4)
