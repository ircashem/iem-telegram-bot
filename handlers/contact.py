from telegram.ext import CommandHandler, MessageHandler, ConversationHandler
from setup import contact_body

def done(update, context):
    chat_id = str(update.message.chat_id)
    msg = "See you morty..."
    update.message.reply_text(text=msg)
    return ConversationHandler.END


def contact(update, context):
    chat_id = str(update.message.chat_id)
    msg = ''
    for element in contact_body:
        msg += "<b>" + element
    update.message.reply_text(text= msg, parse_mode='HTML')
    return done(update,context)
    # context.bot.send_message(chat_id=chat_id,text= msg, parse_mode='HTML')
    # return done(update, context)


contact_handler = CommandHandler("contact", contact)