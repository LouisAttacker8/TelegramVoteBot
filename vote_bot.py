import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Dictionary to store recommendations
recommendations = {'Red': 0, 'Blue': 0}
user_recommendations = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome! Please recommend either 'Red' or 'Blue' by typing /recommend <color>.")

async def recommend(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.message.from_user.id
    if user_id in user_recommendations:
        await update.message.reply_text("You have already made a recommendation.")
        return

    if len(context.args) != 1:
        await update.message.reply_text("Please specify a color: 'Red' or 'Blue'.")
        return

    color = context.args[0].capitalize()
    if color not in ['Red', 'Blue']:
        await update.message.reply_text("Invalid color! Please recommend either 'Red' or 'Blue'.")
        return

    # Record the recommendation
    recommendations[color] += 1
    user_recommendations[user_id] = color
    await update.message.reply_text(f"Thank you for your recommendation! '{color}' now has {recommendations[color]} votes.")

async def results(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    red_votes = recommendations['Red']
    blue_votes = recommendations['Blue']
    await update.message.reply_text(f"Current Recommendations:\nRed: {red_votes}\nBlue: {blue_votes}")

def main() -> None:
    # Replace 'YOUR_TOKEN_HERE' with your bot's API token
    application = ApplicationBuilder().token("7166251717:AAE_VC69fwDfo_VAZ-Rj5CGDRAkpanA1hjA").build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("recommend", recommend))
    application.add_handler(CommandHandler("results", results))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
