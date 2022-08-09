from email2text.gmailbot import Gmailbot

import configparser
config = configparser.ConfigParser()
config.read("config.ini")
username = config.get("email", "username")
  #  password = config.get("email", "password")
text = Gmailbot(username, "token.json")
text.watch("projects/lunchbot-1660075267644/topics/newmessage")

