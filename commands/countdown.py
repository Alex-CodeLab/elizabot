import requests
import json
import time


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

    # 216 is about 36hours
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
    hours_since_fast = (current_time - start_timestamp)/ 3600
    hours_togo = seconds_togo /3600
    message = "We're fasting! This fast started at {}, {:.1f} hours ago. ".format(start_block, hours_since_fast)
    return message
