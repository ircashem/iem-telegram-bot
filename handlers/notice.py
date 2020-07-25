from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, Filters
from msg import wrong_option,done
from setup import notice_body, notice_header
from handlers.start import start

notice_page = {
}

def notice(update, context):
    chat_id = str(update.message.chat_id)
    # notice_page[ chat_id ] = 0
    # msg = "It will took quite a few second to fetch data from the server, hold on; "
    # update.message.reply_text(msg)
    msg = 'Here we go Rick: '
    # if  notice_page[ chat_id ] == 0 :
        # print("ek baar aaya")
    msg +=  "\n0: " + "<b>" + notice_header[0] + "</b>"
    msg +=   notice_body['0']
    msg += "\n /next for next page"
    msg += "\n /done for exit"
    update.message.reply_text(text=msg, parse_mode='HTML')
    notice_page[chat_id] = 1
    # elif int(notice_page[chat_id])  < len(notice_header) and update.message.text == '/next':
        # notice_no = int(notice_page[chat_id])
        # msg +=  "\n" + str(notice_no + 0) + ": <b>" + notice_header[notice_no + 0]
        # msg +=  "</b>\n" + notice_body[str(notice_no)]
        # notice_page[chat_id] = notice_no + 1
        # msg += "\n /next for next page"
        # msg += "\n /done for exit"
        # update.message.reply_text(text =msg, parse_mode='HTML')
    # else:
    #     update.message.reply_text("END OF PAGE MORTY!!!")
    #     return ConversationHandler.END
    return 0


def next_notice(update,context):
    chat_id = str(update.message.chat_id)
    if  update.message.text == '/next':
        if int(notice_page[chat_id])  < len(notice_header):
            notice_no = int(notice_page[chat_id])
            msg =  "\n" + str(notice_no + 0) + ": <b>" + notice_header[notice_no + 0]
            msg +=  "</b>\n" + notice_body[str(notice_no)]
            notice_page[chat_id] = notice_no + 1
            msg += "\n /next for next page"
            msg += "\n /done for exit"
            update.message.reply_text(text =msg, parse_mode='HTML')
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
    notice_page[chat_id] = 0
    return ConversationHandler.END


def check(update, context):
    chat_id = str(update.message.chat_id)
    # print(update.message.text)
    if notice_page[chat_id] == 1 or update.message.text == "/next":
        return next_notice(update,context)
    else:
        return done(update,context)
        
        # return ConversationHandler.END

notice_states = {
    0 : [MessageHandler(Filters.regex("^(/next|/done)$"), check)],
    1 : [MessageHandler(Filters.all, wrong_option)]
}

notice_handler = ConversationHandler(
    entry_points=[CommandHandler("notice", notice)],
    states=notice_states,
    fallbacks=[MessageHandler(Filters.all, wrong_option)],
)
