import random
import string
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Command handler for the /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Welcome! Use /generate to create a random password.')

# Command handler for the /generate command
def generate(update: Update, context: CallbackContext):
    length = 12  # Default length
    if context.args:
        try:
            length = int(context.args[0])
            if length < 6:  # Minimum length check
                update.message.reply_text('Please enter a length of at least 6.')
                return
        except ValueError:
            update.message.reply_text('Please enter a valid number.')

    password = generate_password(length)
    update.message.reply_text(f'Your generated password is: {password} Thanks for using 👾')

def main():
    # Replace 'YOUR_TOKEN_HERE' with your bot's token
    updater = Updater("7595077739:AAHah6PUtxy5lziXX1t1I2uRwLb1z9ufMMk")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("generate", generate))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    