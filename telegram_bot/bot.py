from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

class Bot:
    def __init__(self, token):
        self.application = ApplicationBuilder().token(token).build()
    
    async def handle_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        photo_path = "assets/background.png"
        keyboard = [[InlineKeyboardButton("Open CiWallet", web_app=WebAppInfo("https://google.com"))]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_photo(
            chat_id=update.effective_chat.id, 
            photo=open(photo_path, "rb"),
            caption="""🎉 Introducing CiWallet - a Telegram-based wallet offering simplicity, security, and limitless earning potential within the Aptos ecosystem.""",
            reply_markup=reply_markup
        )
        
    def run(self):
        start_handler = CommandHandler('start', self.handle_start)  
        self.application.add_handler(start_handler)
        self.application.run_polling()
