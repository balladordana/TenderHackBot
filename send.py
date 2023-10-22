import telebot
import config
import datetime
import time
import db


def send_all(description, decision):
    bot = telebot.TeleBot(config.TOKEN)
    scheduled_time = (12, 59)

    while True:
        now = datetime.datetime.now().time()
        if scheduled_time[0] == now.hour and now.minute == scheduled_time[1]:
            users_data = db.select_users()
            for user in users_data:
                bot.send_message(user[0], "Описание ошибки: " + description + "\nРешение: " + decision)
            return
        time.sleep(60)


def send_one(username, description, decision):
    bot = telebot.TeleBot(config.TOKEN)
    chat_id = db.select_user(username)
    bot.send_message(chat_id[0], "Описание ошибки: " + description + "\nРешение: " + decision)
    return


