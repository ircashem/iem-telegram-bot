from telegram.ext import CommandHandler, ConversationHandler

def wrong_option(update, context):
    msg = "Invalid option."
    update.message.reply_text(msg)
    return ConversationHandler.END

def done(update, context):
    msg = "See you morty..."
    update.message.reply_text(text=msg)
    return ConversationHandler.END

# done_handler = CommandHandler("done",done)
# msg_handler = 