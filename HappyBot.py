from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from quotes_crawler import Crawler

import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
crawler = Crawler()
cid = int(454323424)

print("HappyBot wurde instanziiert")

updater = Updater(token='785333374:AAGiHCETBBEwIBJUY_qaYGrnIAbttBqqQn8')
job = updater.job_queue
dispatcher = updater.dispatcher

#answer section
def start(bot, update):
    print(update.message.chat_id)
    bot.send_message(chat_id=update.message.chat_id, text="Hi, ich bin Leons persönlicher Bot. Ich helfe ihm dabei fokusiert und motiviert zu bleiben")

def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Den Command habe ich nicht im Repertoire, hörma!")

def caps(bot, update, args):
    text_caps = ' '.join(args).upper()
    bot.send_message(chat_id=update.message.chat_id, text=text_caps)

def quote(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=crawler.getRandomQuote())

def fetch(bot, update):
    crawler.fetchQuotes()
    bot.send_message(chat_id=update.message.chat_id, text="Ich besorch mal eben neue Quotes!")

def callback_quote(bot, job):
    print("message sent")
    quote = crawler.getRandomQuote()
    bot.send_message(chat_id=cid, text=quote)


job.run_repeating(callback_quote, interval=1800, first=0)

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("caps", caps, pass_args=True))
dispatcher.add_handler(CommandHandler("quote", quote))
dispatcher.add_handler(CommandHandler("fetch", fetch))
# this must be the last argument so it goes through all commands
dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()
updater.idle()


