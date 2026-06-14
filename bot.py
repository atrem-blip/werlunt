
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Токен от BotFather
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Поиск лекарств"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Привет! Я помогу найти лекарства в вашем городе.", reply_markup=reply_markup)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Поиск лекарств":
        await update.message.reply_text("Введите название лекарства и город (например: 'Парацетамол Москва').")
    else:
        # Парсинг запроса: лекарство + город
        parts = text.split()
        if len(parts) < 2:
            await update.message.reply_text("Пожалуйста, укажите лекарство и город.")
            return

        medicine_name = parts[0]
        city_name = " ".join(parts[1:])

        # Здесь — запрос к БД
        results = search_medicine_in_db(medicine_name, city_name)

        if results:
            response = "\n".join([f"{p['pharmacy']}: {p['price']} руб. ({p['quantity']} шт.)" for p in results])
        else:
            response = "Лекарство не найдено. Попробуйте другое название или город."

        await update.message.reply_text(response)

def search_medicine_in_db(medicine_name: str, city_name: str) -> list:
    # Заглушка: здесь должен быть SQL-запрос к вашей БД
    # Пример результата:
    return [
        {"pharmacy": "Аптека №1", "price": 150.0, "quantity": 10},
        {"pharmacy": "Аптека №2", "price": 160.0, "quantity": 5}
    ]

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()

if __name__ == "__main__":
    main()
