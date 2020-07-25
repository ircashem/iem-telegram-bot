from telegram.ext import CommandHandler, ConversationHandler

def good_bye(update, context):
    user = update.message.from_user
    msg = "See you again :) " + str(user.first_name)
    update.message.reply_text(text=msg,)
    print("Successfully handled user: " + str(user.first_name))
    return ConversationHandler.END

exit_handler = CommandHandler("exit", good_bye)