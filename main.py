import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Получаем токен из переменной окружения
TOKEN = os.getenv('TELEGRAM_TOKEN')
PORT = int(os.environ.get('PORT', 5000))

# Функция для обработки команды /start
async def start(update: Update, context):
    await update.message.reply_text('Привет! Я ваш помощник по юридическим вопросам. Напишите свой вопрос.')

# Функция для обработки команды /help
async def help_command(update: Update, context):
    await update.message.reply_text('Я могу помочь вам с юридическими вопросами. Напишите свой вопрос.')

# Функция для обработки сообщений от пользователя
async def handle_message(update: Update, context):
    text = update.message.text
    await update.message.reply_text(f'Ваш вопрос: {text}. Спасибо за обращение!')

# Основная функция для запуска бота
def main():
    # Создаем экземпляр приложения
    app = ApplicationBuilder().token(TOKEN).build()

    # Обработка команды /start
    app.add_handler(CommandHandler("start", start))
    
    # Обработка команды /help
    app.add_handler(CommandHandler("help", help_command))

    # Обработка всех текстовых сообщений
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запуск бота с использованием вебхука
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"https://unionhelper.herokuapp.com/{7921966575:AAHHe8EahOrzWiYeMeJelvJj2Hy979Nfdn8}"
    )

if __name__ == '__main__':
    main()
