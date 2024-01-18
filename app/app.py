from meal_api import MealApi
import logging
import argparse

logging.basicConfig(format="%(levelname)s %(message)s")


def parse_app_args():
    parser = argparse.ArgumentParser(prog="Meal Idea Notifier")

    parser.add_argument(
        "-d",
        "--debug",
        help="Enable debug mode",
        required=False,
        action="store_true",
    )

    return parser.parse_args()


if __name__ == "__main__":
    parsed = parse_app_args()

    meal_api = MealApi(debug=parsed.debug)
    meal_api.load_single_meal()

    dish_name = meal_api.get_dish_name()
    ingredients = meal_api.get_ingredients()
    instructions = meal_api.get_instructions()

    meal_image = meal_api.get_meal_image()
