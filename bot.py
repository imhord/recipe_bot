import telebot
bot = telebot.TeleBot('1849267179:AAFvkQbkeFoMsHqI-fFsuUtLAOlXogTDSh4')

@bot.massage_handler(commands=['start','help'])
def send_welcome(message):
	bot.reply_to(message, f'Я бот для поиска рецептов. Приятно познакомиться, {message.from_user.first_name}')
	
bot.polling(none_stop=True)
