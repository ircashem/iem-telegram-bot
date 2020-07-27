from setup import logger
from telegram.ext import (Updater)#, CommandHandler, MessageHandler, Filters, ConversationHandler)
from handlers.start import start_handler
from handlers.notice import notice_handler
from handlers.news import news_handler
from handlers.good_bye import exit_handler
from handlers.contact import contact_handler
from setup import error,token

avail_handlers = [start_handler, notice_handler, news_handler, contact_handler, exit_handler]

def main():
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher
    for handler in avail_handlers:
        dp.add_handler(handler)

    print("Handler started successfully.")
    updater.start_polling()
    updater.idle()
    print("Handler shut down successfully.")


if __name__ == "__main__":
    main()