import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# Set up logging
logging.basicConfig(level=logging.INFO)

# Directly set the API key in the configure function
genai.configure(api_key="AIzaSyC-9ctm23M0zdLvsUOPIpPnhfL9FVls4CE")

TOKEN = '6496895412:AAE19tN7cZyACAx61SCNZJh1se2Q6hhrcRA'

# Define the Gemini API Request Function
def get_gemini_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        logging.error(f"Error with the Gemini API request: {e}")
        return f"Error: {str(e)}"

# Define the Bot's Command and Message Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm a bot. Ask me anything, and I'll get you a response using the Gemini API.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = get_gemini_response(user_input)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("An error occurred. Please try again.")

# Set Up the Main Function
if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error)
    application.run_polling()
