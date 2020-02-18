from telegram.ext import Updater
from telegram.ext import CommandHandler
from config import token
from commands.countdown import countdown
from commands.registernode import registernode
from commands.ticker import ticker
from commands.halving import halving
from util import sqlite_init

import logging
import signal


updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


if __name__ == '__main__':
    # nicely terminate
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    cursor = sqlite_init()

    registernode = CommandHandler('registernode', registernode)
    dispatcher.add_handler(registernode)

    blockHeight_handler = CommandHandler('countdown', countdown)
    dispatcher.add_handler(blockHeight_handler)

    blockHeight_handler = CommandHandler('price', ticker)
    dispatcher.add_handler(blockHeight_handler)

    halving_handler = CommandHandler('halving', halving)
    dispatcher.add_handler(halving_handler)

    updater.start_polling()
