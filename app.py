from lunch_bot_getter import Lunchbot
#from url_getter import Menu
#from email2text import TextBot #https://github.com/js802025/email2text
from datetime import date
import configparser
from email2text.gmailbot import Gmailbot


##menu = Menu()
##
##url = menu.get_pdf_url()

url = 'https://fwparker.myschoolapp.com/ftpimages/1048/download/download_6209679.pdf'

bot = Lunchbot(url)



#today = date.today().strftime('%A')

#@app.route('/sms', methods=['POST'])
def lunch(message, From):
    if message in bot.days_of_the_week:
        reply = bot.get_day(message)
    else: reply = bot.get_week()
    text.send_message(reply, From)
if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("config.ini")
    username = config.get("email", "username")
  #  password = config.get("email", "password")
    text = Gmailbot(username, "token.json", handle_messages=lunch)
    text.start()    
