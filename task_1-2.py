import pprint


def read_cook_book():
    cook_book = {}
    with open('recipes.txt', 'r', encoding='utf-8') as file:
        current_recipe = None
        ingredients_count = 0
        for line in file:
            line = line.strip()
            if not line:
                continue
            if not current_recipe:
                current_recipe = line
                cook_book[current_recipe] = []
            elif not ingredients_count:
                ingredients_count = int(line)
            else:
                ingredient_info = line.split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                cook_book[current_recipe].append(ingredient)
                ingredients_count -= 1
                if ingredients_count == 0:
                    current_recipe = None
                    ingredients_count = 0

    return cook_book


cook_book = read_cook_book()
print(cook_book, end='\n\n')


def get_shop_list_by_dishes(dishes: list, person_count: int):
    shop_list = {}
    for dish in dishes:
        lst_ingredients = cook_book[dish]
        for item in lst_ingredients:
            if item['ingredient_name'] not in shop_list:
                shop_list[item['ingredient_name']] = {
                    'measure': item['measure'],
                    'quantity': item['quantity'] * person_count,
                }
            else:
                shop_list[item['ingredient_name']]['quantity'] += item['quantity'] * person_count

    return shop_list


shop_dict = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint.pp(shop_dict)
