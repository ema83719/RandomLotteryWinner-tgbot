
bot_token = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'
user_list = ['@User1', '@User2', '@User3', '@User4']

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['winner'])
def handle_winner(message):
    # This function is triggered when the user sends the command "/winner"

    # Select a random user from the list
    winner = random.choice(user_list)

    # Send the winner to the user who sent the command
    bot.send_message(message.chat.id, f'The winner is: {winner}')

