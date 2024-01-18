from typing import Dict
import logging
import requests


class MealApi:
    API_URL = "https://www.themealdb.com/api/json/v1/1/random.php"
    INGREDIENT_KEY_NAME = "strIngredient"
    MEASURE_KEY_NAME = "strMeasure"

    def __init__(self, debug: bool = False):
        logging.getLogger().setLevel(logging.INFO if not debug else logging.DEBUG)

        self.meal_data: Dict = {}

    def get_dish_name(self):
        return self.meal_data["strMeal"]

    def get_instructions(self):
        return self.meal_data["strInstructions"]

    def get_ingredients(self):
        ingredients = {}

        # Get all the keys that start with INGREDIENT_KEY_NAME
        ingredients_keys = [
            k
            for k in self.meal_data.keys()
            if k.startswith(MealApi.INGREDIENT_KEY_NAME)
        ]

        for i, key in enumerate(ingredients_keys):
            ingredient = self.meal_data[key]

            # If the ingredient is not empty, add it to the ingredients dictionary
            if ingredient and ingredient.strip() != "":
                ingredients[ingredient] = self.meal_data[
                    f"{MealApi.MEASURE_KEY_NAME}{i+1}"
                ]

        return ingredients

    def get_meal_image(self):
        img_key = "strMealThumb"

        if self.meal_data[img_key] is None or len(self.meal_data[img_key]) == 0:
            return None

        try:
            img_resp = requests.get(self.meal_data[img_key], stream=True, timeout=10)
            img_resp_raw = img_resp.raw.read()
        except requests.exceptions.RequestException as e:
            logging.error(e)
            return None

        return img_resp_raw

    def load_single_meal(self):
        try:
            json_data = requests.get(MealApi.API_URL, timeout=10).json()
            logging.debug(json_data)

            if json_data["meals"] is None or len(json_data["meals"]) == 0:
                raise MealApiException("Meal data is empty !")

            self.meal_data = json_data["meals"][0]

        except requests.exceptions.RequestException as e:
            logging.error(e)
            raise MealApiException() from e


class MealApiException(Exception):
    pass
