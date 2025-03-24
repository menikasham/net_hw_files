class ShopList:
    def __init__(self, file='recipes.txt'):
        self.file = file
        self.cook_book = {}
        self.shop_list = {}

    def read_cook_book(self):
        self.cook_book = {}
        with open(self.file, 'r', encoding='utf-8') as file:
            current_recipe = None
            ingredients_count = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if not current_recipe:
                    current_recipe = line
                    self.cook_book[current_recipe] = []
                elif not ingredients_count:
                    ingredients_count = int(line)
                else:
                    ingredient_info = line.split(' | ')
                    ingredient = {
                        'ingredient_name': ingredient_info[0],
                        'quantity': int(ingredient_info[1]),
                        'measure': ingredient_info[2]
                    }
                    self.cook_book[current_recipe].append(ingredient)
                    ingredients_count -= 1
                    if ingredients_count == 0:
                        current_recipe = None
                        ingredients_count = 0

        return self.cook_book

    def get_shop_list_by_dishes(self, dishes: list, person_count: int):
        for dish in dishes:
            lst_ingredients = self.cook_book[dish]
            for item in lst_ingredients:
                if item['ingredient_name'] not in self.shop_list:
                    self.shop_list[item['ingredient_name']] = {
                        'measure': item['measure'],
                        'quantity': item['quantity'] * person_count,
                    }
                else:
                    self.shop_list[item['ingredient_name']]['quantity'] += item['quantity'] * person_count

        return self.shop_list

    def print_cook_book(self):
        print(self.cook_book)

    def print_shop_list(self):
        print(self.shop_list)



if __name__ == '__main__':
    cook_book = ShopList()
    cook_book.read_cook_book()
    cook_book.print_cook_book()
    cook_book.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    cook_book.print_shop_list()