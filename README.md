# Meal Idea Notifier
Meal Idea Notifier is a Python application that provides you with a random meal idea along
with its ingredients, instructions, and image. The application utilizes the 
[MealDB API](https://themealdb.com/api/json/v1/1/random.php)
to fetch random meal data and sends the information via Telegram. It is hosted on a server and 
automatically runs every day at 13:00 (1:00 PM).

## Requirements
* **python** version 3.10
* **requests** version 2.31.0
* **argparse** version 1.4.0
* **pyyaml** version 6.0.1
* **pytelegrambotapi**  version 4.15.2

To install required packages:
1. Make sure you have poetry installed. If not, you can install it using:
```bash
pip install poetry
```
2. Navigate to the project directory containing the `pyproject.toml` file.
3. Run the following command to install the dependencies defined in `pyproject.toml`:
```bash
poetry install
```

## Configuration 
To use the Meal Idea Notifier application, create a config.yaml file and customize it according 
to your needs. Below is an example structure for the config.yaml file:
```yaml
api_key: "TELEGRAM_BOT_TOKEN"
recipients:
  user1: "TELEGRAM_USER_ID_1"
  user2: "TELEGRAM_USER_ID_2"
  # Add more recipients as needed
```
* `api_key`: The access token for the Telegram Bot API. To obtain an access token, 
register a new bot with BotFather and get the bot token.
* `recipients`: A section containing the names of recipients and their Telegram IDs. 
Each recipient has a unique name (e.g., user1, user2) and is associated with a Telegram ID. 
You can obtain a user's Telegram ID by chatting with the User Info Bot.

## Features
### MealApi Class:
* Interacts with the [MealDB API](https://themealdb.com/api/json/v1/1/random.php)
to retrieve random meal data.
* Provides methods to extract meal details such as dish name, ingredients, instructions, and meal image.

### TelegramSender Class:
* Uses the telebot library to send messages and images via Telegram.
* Methods include sending a text message, sending a text message with an image, sending a text 
message to multiple recipients and sending a text message with an image to multiple recipients.

### Configuration parser and message formatter:
* The generate_message_content function formats a message with meal information using a template.
* The parse_config function reads the content of a YAML configuration file.
