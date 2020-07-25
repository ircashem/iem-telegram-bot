import logging, requests, re
from filters.notice_header import extract_notice_header
from filters.notice_body import extract_notice_body
from filters.contact_body import extract_contact
from filters.news_body import extract_news

NOTICE_URL = 'https://www.iem.edu.in/notices'
CONTACT_URL = 'https://www.iem.edu.in/contact-us'
NEWS_URL = 'https://www.iem.edu.in/tag/news-articles'

print("Extracting notice_header")
notice_header = extract_notice_header(NOTICE_URL)
print("Extracting notice_body")
notice_body = extract_notice_body(NOTICE_URL)
print("Extracting contact_body")
contact_body =extract_contact(CONTACT_URL)
print("Extracting news_body")
news_body = extract_news(NEWS_URL)

TOKEN = '1295365378:*******************************'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
























    # Start the bot
    
    # conv_handler = ConversationHandler(
    #     entry_points=[CommandHandler("start",start)],

    #     states={
    #         INITIAL_CHOICE: [MessageHandler(Filters.regex('^(/notice|/contact|/news|/done)$'), init_choice)],
    #         NOTICE_CHOICE: [CommandHandler("next", notice),
    #                         CommandHandler("done",good_bye)],
    #         NEWS_CHOICE: [CommandHandler("next", news),
    #                         CommandHandler("done",good_bye)]
    #         },
        
    #     fallbacks=[CommandHandler("cancel", good_bye)]
    # )

    # dp.add_handler(conv_handler)
    
