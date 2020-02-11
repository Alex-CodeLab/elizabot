import requests
import json
import time


def ticker(update, context):
    message = _ticker()
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def _ticker():
    response = requests.get('https://blockchain.info/ticker')
    res = response.json()
    return "$" + str(res["USD"]["15m"])
