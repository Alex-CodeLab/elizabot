from telegram.ext import Updater
from telegram.ext import CommandHandler
from config import token
import requests
import logging


updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def countdown(update, context):
    response = requests.get('https://blockstream.info/api/blocks/tip/height')
    blocks_until_fast = 2000 - (int(response.text) % 2000)
    hours_until = (blocks_until_fast / 6)
    message = "Next fast in {} blocks ({:.2f} hours).".format(blocks_until_fast, hours_until)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)



if __name__ == '__main__':
    # start_handler = CommandHandler('start', start)
    # dispatcher.add_handler(start_handler)

    blockHeight_handler = CommandHandler('countdown', countdown)
    dispatcher.add_handler(blockHeight_handler)

    updater.start_polling()
