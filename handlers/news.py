from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, Filters
from setup import news_body
from msg import wrong_option

news_page = {}
def news(update,context):
    chat_id = str(update.message.chat_id)
    msg = news_body[0]
    # msg += "------------------------------------------------------------------------------------"
    msg += "/next for next page"
    msg += "\n /done for exit"
    msg += "\n------------------------------------------------------------------------------------"
    news_page[chat_id] = 1
    update.message.reply_text(text=msg, parse_mode='HTML')
    return 0
    # elif update.message.text == '/next' and int(news_page[chat_id]  + 1 < len(news_body) ):
        # news_no = int(news_page[chat_id])
        # # msg = "\n-------------------------------------------------------------------------------\n"
        # msg = news_body[news_no]
        # # msg += news_body[news_no + 1]
        # # msg += "\n-------------------------------------------------------------------------------\n"
        # msg += "/next for next page"
        # msg += "\n /done for exit"
        # msg += "\n------------------------------------------------------------------------------------"
        # news_page[chat_id] = news_no + 1
        # update.message.reply_text(text=msg, parse_mode='HTML')
    # elif update.message.text == '/done':
    #     msg = "See you morty..."
    #     update.message.reply_text(text=msg)
    # else:
    #     update.message.reply_text("END OF PAGE MORTY!!!")
    #     ConversationHandler.END

def next_news(update,context):
    chat_id = str(update.message.chat_id)
    if update.message.text == '/next':
        if int(news_page[chat_id] ) + 1 < len(news_body) :
            news_no = int(news_page[chat_id])
            # msg = "\n-------------------------------------------------------------------------------\n"
            msg = news_body[news_no]
            # msg += news_body[news_no + 1]
            # msg += "\n-------------------------------------------------------------------------------\n"
            msg += "/next for next page"
            msg += "\n /done for exit"
            msg += "\n------------------------------------------------------------------------------------"
            news_page[chat_id] = news_no + 1
            update.message.reply_text(text=msg, parse_mode='HTML')
            return 0
        else:
            update.message.reply_text("END OF PAGE MORTY!!!")
            return ConversationHandler.END
    elif update.message.text == "/done":
        return done(update, context)
    else:
        return wrong_option(update,context)

def done(update, context):
    chat_id = str(update.message.chat_id)
    msg = "See you morty..."
    update.message.reply_text(text=msg)
    news_page[chat_id] = 0
    return ConversationHandler.END

def check(update, context):
    chat_id = str(update.message.chat_id)
    # print(update.message.text)
    if news_page[chat_id] == 1 or update.message.text == "/next":
        return next_news(update,context)
    else:
        return done(update,context)
        # return 1
    
news_states = {
    0 : [MessageHandler(Filters.regex("^(/next|/done)$"), check)],
    1 : [MessageHandler(Filters.all, wrong_option)]
}

news_handler = ConversationHandler(
    entry_points=[CommandHandler("news", news)],
    states=news_states,
    fallbacks=[MessageHandler(Filters.all, wrong_option)],
)
