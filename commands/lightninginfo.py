import json


def lightninginfo(update, context):
    message = _lightninginfo()
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def _lightninginfo():
    message = ""
    return message
