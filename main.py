import Constants as keys
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import *
import Responses as R


print("bot started....")

# Basic commands

def start_command(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Type something random to get started!")
# def start_command(update, context):
#     update.message.reply_text("Welcome to my awesome bot!")

def help_command(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="google it")

def handle_message(update: Update, context: CallbackContext):
    text = str(update.message.text).lower()
    user_name = update.message.chat.first_name
    response = R.sample_responses(text , user_name)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def help_command(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="google it")
# return all in caps

def caps_command(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

def error(update: Update, context: CallbackContext):
    print(f'Update {update} caused error {context.error}')

# inline caps

def inline_caps(update: Update, context: CallbackContext):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)



def main():
    # Create the Updater and pass it bot's token.
    updater = Updater(keys.APY_KEY, use_context=True)


    # Get the dispatcher to register handlers
    dp = updater.dispatcher


    # Register the commands...
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    caps_handler = CommandHandler("caps", caps_command)
    dp.add_handler(caps_handler)
    echo_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
    dp.add_handler(echo_handler)
    inline_caps_handler = InlineQueryHandler(inline_caps)
    dp.add_handler(inline_caps_handler)
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

    # updater.stop()


main()
