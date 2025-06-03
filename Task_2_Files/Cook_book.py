cook_book = {}

with open("recipes.txt", "r", encoding="utf-8") as f:
    for _ in range(4): # согласно выходным данным из ТЗ требовалось только 3 блюда, но оставлю 4 для проверки повторяющихся ингридиентов
        name_receipt = f.readline().strip()
        count_points_receipt = int(f.readline().strip())
        ingr = []
        for _ in range(count_points_receipt):
            temp_list = f.readline().strip().split(" | ")
            ingr.append(
                {
                    "ingredient_name": temp_list[0],
                    "quantity": temp_list[1],
                    "measure": temp_list[2],
                }
            )
            cook_book[name_receipt] = ingr
        skip_line = f.readline().strip()


print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    how_to_cook = {}
    for dish in dishes:
        if dish in cook_book:
            for point in cook_book[dish]:  # point - это строка-словарь внутри списка
                keep_ingridients_dict = {
                        "measure": point["measure"],
                        "quantity": int(point["quantity"]) * person_count
                }
                ingr_name_for_reciept = point["ingredient_name"]
                if ingr_name_for_reciept in how_to_cook:
                    keep_ingridients_dict["quantity"] += int(point["quantity"])*person_count
                    how_to_cook[ingr_name_for_reciept] = keep_ingridients_dict
                else:
                    how_to_cook[ingr_name_for_reciept] = keep_ingridients_dict
        else:
            return print(
                "Если бы мы знали, как это готовить, мы не знаем как это готовить :("
            )
    return print(how_to_cook)

get_shop_list_by_dishes(["Фахитос", "Омлет"], 7)
print()
get_shop_list_by_dishes(["Запеканка", "Омлет"], 4)
print()
get_shop_list_by_dishes(["Утка по-пекински", "Фахитос"], 3)
print()
get_shop_list_by_dishes(["Омлет", "Омлет"], 2)
print()
get_shop_list_by_dishes(["Утка по-пекински", "Омлет", "Запеченный картофель"], 2)

