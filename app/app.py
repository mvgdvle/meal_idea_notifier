from meal_api import MealApi


if __name__ == "__main__":
    meal_api = MealApi()
    meal_api.load_single_meal()

    dish_name = meal_api.get_dish_name()
    ingredients = meal_api.get_ingredients()
    instructions = meal_api.get_instructions()

    print(f'Dish name: {dish_name}')
    print(f'Ingredients: {ingredients}')
    print(f'Instructions: {instructions}')
