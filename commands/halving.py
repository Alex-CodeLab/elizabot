import requests
import json
import time
import datetime
from datetime import datetime, timedelta, date

def halving(update, context):
    message = _halving()
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def _halving():
    response = requests.get('https://blockstream.info/api/blocks/tip/height')
    block_height = int(response.text)
    halving_block = 630000
    blocks_until_halving = halving_block - block_height
    hours_until_halving = int(blocks_until_halving / 6.2)
    halvingDate = date.today() + timedelta(days=hours_until_halving/24)
    message = "Blocks until halving: {} (expected halving date: {}) ".format(blocks_until_halving, halvingDate.strftime('%d %b %Y'))
    return message
