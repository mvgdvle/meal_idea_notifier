from meal_api import MealApi
from util import parse_config, generate_message_content
import logging
import argparse
from telegram_sender import TelegramSender

logging.basicConfig(format="%(levelname)s %(message)s")


def parse_app_args():
    parser = argparse.ArgumentParser(prog="Meal Idea Notifier")

    parser.add_argument(
        "-c",
        "--config",
        help="Path to the config file",
        required=False,
        default="config.yaml",
    )

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

    config = parse_config(parsed.config)

    meal_api = MealApi(config, debug=parsed.debug)
    meal_api.load_single_meal()

    meal_message = generate_message_content(
        meal_api.get_dish_name(),
        meal_api.get_ingredients(),
        meal_api.get_instructions(),
    )

    meal_image = meal_api.get_meal_image()

    sender=TelegramSender(config["api_key"])
    for recipient, chat_id in config["recipients"].items():
        logging.info(f"[+] Sending message to {recipient}")
       
        try: 
            if meal_image:
                sender.send_message_with_image(chat_id, meal_message, meal_image)
            else:
                sender.send_message(chat_id, meal_message)
        except Exception as e:
            logging.error(e)
            logging.error(f"[-] Failed to send message to {recipient}")
            continue
