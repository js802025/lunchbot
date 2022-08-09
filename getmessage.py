from email2text.gmailbot import Gmailbot

import configparser
from lunch_bot_getter import Lunchbot
url = 'https://fwparker.myschoolapp.com/ftpimages/1048/download/download_6209679.pdf'

bot = Lunchbot(url)
def lunch(message, From):
    if message in bot.days_of_the_week:
        reply = bot.get_day(message)
    else: reply = bot.get_week()
    text.send_message(reply, From)
config = configparser.ConfigParser()
config.read("config.ini")
username = config.get("email", "username")
  #  password = config.get("email", "password")
text = Gmailbot(username, "token.json", handle_messages=lunch)
print(text.get_new_message("39638"))