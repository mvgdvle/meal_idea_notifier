import logging
import yaml


def parse_config(config_file_name: str):
    with open(config_file_name, "r", encoding="utf-8") as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            logging.error(e)
            raise e

        return config

#zwracanie sformatowanej wiadomości
def generate_message_content(dish_name, ingredients, instructions):

# wzór wiadomości - nazwa dania + instrukcja + lista składników wraz z miarami 
    meal_idea_template= """
<b>{DISH_NAME}</b>

<u>Cooking Instructions:</u>
{COOKING_INSTRUCTIONS}

<u>Ingredients:</u>
{INGREDIENTS}
"""
    meal_idea_template = meal_idea_template.replace("{DISH_NAME}", dish_name).replace(
        "{COOKING_INSTRUCTIONS}", instructions)
    
    cooking_ingredients = ""
    for i, (ingredient, measure) in enumerate(ingredients.items()):
        cooking_ingredients += f"{i+1}. {ingredient}: ({measure})\n"
    
    meal_idea_template = meal_idea_template.replace(
        "{INGREDIENTS}", cooking_ingredients)
    
    return meal_idea_template