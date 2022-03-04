import Constants as keys
from telegram import Update
from telegram.ext import *
import Responses as R
from flask import Flask

print("bot started....")

def start_command(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Type something random to get started!")

    
def help_command(update, context):
    update.message.reply_text('google it')
    
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)

def main():
    updater = Updater(keys.APY_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))

    updater.start_polling()
    updater.idle()
    # updater.stop()
main()
