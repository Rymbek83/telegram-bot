import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Получаем токен из переменной окружения
TOKEN = os.getenv('TELEGRAM_TOKEN')

def start(update, context):
    update.message.reply_text('Привет! Я ваш помощник по юридическим вопросам. Напишите свой вопрос.')

def help_command(update, context):
    update.message.reply_text('Я могу помочь вам с юридическими вопросами. Напишите свой вопрос.')

def handle_message(update, context):
    text = update.message.text
    # Ответ бота на текстовые сообщения
    update.message.reply_text(f'Ваш вопрос: {text}. Спасибо за обращение!')

def main():
    # Создаем бота с использованием токена
    updater = Updater(TOKEN, use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Обработка команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # Обработка текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запуск бота
    updater.start_polling()

    # Запуск работы бота до остановки
    updater.idle()

if __name__ == '__main__':
    main()
