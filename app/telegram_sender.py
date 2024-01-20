from telebot import TeleBot 

class TelegramSender:

    def __init__(self, api_key: str):
        self.bot =TeleBot(api_key, parse_mode="HTML")

    #wysyłanie wiadomości tekstowej na wskazany chat ID
    def send_message(self, chat_id: str, message: str):
        self.bot.send_message(chat_id, message)

    #wiadomość tekstowa + zdjęcie na wskazany chat ID
    def send_message_with_image(self, chat_id: str, message: str, image: bytes):
        self.bot.send_photo(chat_id, image)
        self.send_message(chat_id, message)

    #wiadomość tekstowa do wielu ID
    def send_message_to_multiple(self, chat_ids: list, message: str):
        
        for chat_id in chat_ids:
            self.send_message(chat_id, message)

    #wiadomość tekstowa +zdjęcie do wielu ID
    def send_message_with_photo_to_multiple(self, chat_ids: list, message: str, image: bytes):
        for chat_id in chat_ids:
            self.send_message_with_image(chat_id, message, image)

