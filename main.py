from telegram.ext import Updater
from telegram.ext import CommandHandler
from config import token
import requests
import json
import logging
import time


updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def countdown(update, context):
    message = _countdown()
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def _countdown(blockheight=False):
    if blockheight == False:
        response = requests.get('https://blockstream.info/api/blocks/tip/height')
        block_height = int(response.text)
    else:
        block_height = blockheight
    blocks_until_fast = 2000 - (block_height % 2000)
    hours_until = (blocks_until_fast / 6.2)

    # 1784 is about 36hours
    if blocks_until_fast > 1784:
        message = _countdown_while_fast(block_height)
    else:
        message = "Next fast in {} blocks ({:.1f} hours).".format(blocks_until_fast, hours_until)
    return message

def _countdown_while_fast(block_height):
    start_block = block_height - (block_height % 2000 )
    #get blockhash
    response = requests.get('https://blockstream.info/api/block-height/{}'.format(start_block))
    block_hash = str(response.text)
    # get blocktime
    response = requests.get('https://blockstream.info/api/block/{}'.format(block_hash))
    start_timestamp = json.loads(response.text)['timestamp']
    end_timestamp = int(start_timestamp) + 129600 # 36hours
    current_time = int(time.time())
    seconds_togo = end_timestamp - current_time
    hours_togo = seconds_togo /3600
    message = "We're fasting! This fast started at {}. About {:.1f} more hours to go.".format(start_block, hours_togo)
    return message



if __name__ == '__main__':
    # start_handler = CommandHandler('start', start)
    # dispatcher.add_handler(start_handler)

    blockHeight_handler = CommandHandler('countdown', countdown)
    dispatcher.add_handler(blockHeight_handler)

    updater.start_polling()
