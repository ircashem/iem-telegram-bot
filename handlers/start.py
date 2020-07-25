
from msg import wrong_option
from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, Filters

web_url = "https://www.iem.edu.in"

def start(update, context):
    # print(update.message)
    user = update.message.from_user
    chat_id = update.message.chat_id
    print("User: " + str(user.first_name) + " logged in.")
    msg = "Hi, " + "<b>" + user.first_name + "</b>."
    context.bot.send_message(chat_id=chat_id, text=msg, parse_mode='HTML')
    msg = "<strong> Welcome to the iemcrp group. </strong> \n"
    msg += "Quote of the day: \n<i>This is just start of a new adventure Rick. Wanna be a part of it.</i>\n"
    msg += web_url
    # print(logger.info(msg))
    msg += "\n/notice"
    msg += "\n/news"
    msg += "\n/contact"
    msg += "\n/exit"
    # print(msg)
    update.message.reply_text(text=msg, parse_mode = 'HTML')
    # context.bot.send_message(chat_id=chat_id, text = msg, parse_mode='HTML')
    return 0


start_handler = CommandHandler("start", start)

