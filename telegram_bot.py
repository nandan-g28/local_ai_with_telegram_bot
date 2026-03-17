import ollama
import asyncio
import threading
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Your regenerated token here (REGENERATE THIS ASAP!)
TOKEN = "8315923650:AAGf7esZZtAiojBL6Nx7-Ao_3ffEA7Edtkg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    await update.message.reply_text(
        "Hey! I'm OpenHermes running locally on Nandan's i5-6500T 🤖\n"
        "Ask me anything and I'll think about it (might take 10-40 secs).\n"
        "Type /help for commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    await update.message.reply_text(
        "Commands:\n"
        "/start - Start the bot\n"
        "/help - Show this message\n"
        "Just send any message and I'll respond with OpenHermes!"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle regular messages"""
    user_message = update.message.text
    user_name = update.message.from_user.first_name
    chat_id = update.message.chat_id
    
    print(f"\n{'='*60}")
    print(f"📱 Message from {user_name}: {user_message}")
    print(f"💬 Chat ID: {chat_id}")
    print(f"{'='*60}")
    
    await update.message.chat.send_action("typing")
    
    try:
        print(f"🤖 OpenHermes is thinking...")
        
        response = ollama.chat(
            model='openhermes',
            messages=[
                {'role': 'system', 'content': 'You are a helpful AI assistant. Provide detailed, thoughtful answers with good explanations. Use 2-4 paragraphs when needed. Be conversational and engaging.'},
                {'role': 'user', 'content': user_message}
            ],
            stream=False
        )
        bot_response = response['message']['content']
        
        print(f"✅ OpenHermes Response: {bot_response}")
        print(f"{'='*60}\n")
        
        await update.message.reply_text(bot_response)
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        print(f"❌ {error_msg}")
        await update.message.reply_text(error_msg)

def main():
    """Start the bot"""
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("\n" + "="*60)
    print("🚀 Bot is running! Send messages in Telegram...")
    print("="*60 + "\n")
    
    app.run_polling()

if __name__ == "__main__":
    main()
