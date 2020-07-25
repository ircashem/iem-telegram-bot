from setup import logger
from telegram.ext import (Updater)#, CommandHandler, MessageHandler, Filters, ConversationHandler)
from handlers.start import start_handler
from handlers.notice import notice_handler
from handlers.news import news_handler
from handlers.good_bye import exit_handler
from handlers.contact import contact_handler
from setup import TOKEN,error

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(start_handler)
    dp.add_handler(notice_handler)
    dp.add_handler(news_handler)
    dp.add_handler(contact_handler)
    dp.add_handler(exit_handler)
    dp.add_error_handler(error)

    print("Handler started successfully.")
    updater.start_polling()
    updater.idle()
    print("Handler shut down successfully.")


if __name__ == "__main__":
    main()