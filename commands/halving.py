import requests
import json
import time

def halving(update, context):
    message = _halving()
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def _halving():
    response = requests.get('https://blockstream.info/api/blocks/tip/height')
    block_height = int(response.text)
    halving_block = 630000
    blocks_until_halving = halving_block - block_height
    time_until_halving = int(blocks_until_halving / 6.2)
    message = "Blocks until halving: {} ({} hours to go...) ".fomat(blocks_until_halving, time_until_halving)
    return message
