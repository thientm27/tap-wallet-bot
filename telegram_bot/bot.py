from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

class Bot:
    def __init__(self, token):
        self.application = ApplicationBuilder().token(token).build()
    
    async def handle_start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        photo_path = "assets/background-2.png"
        keyboard = [[InlineKeyboardButton("Open Game", web_app=WebAppInfo("https://wavemonster.starci.net/"))]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_photo(
            chat_id=update.effective_chat.id, 
            photo=open(photo_path, "rb"),
            caption="""🎉 WaveMonster is a top-tier action survival game where you will face relentless waves of monstrous attacks. You must continuously move, dodge, and eliminate the swarming monsters coming at you. Can you survive each wave of assaults and emerge as the ultimate hero?""",
            reply_markup=reply_markup
        )
         
    def run(self):
        start_handler = CommandHandler('start', self.handle_start)  
        self.application.add_handler(start_handler)
        self.application.run_polling() 
