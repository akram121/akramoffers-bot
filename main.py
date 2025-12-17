import os
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TOKEN or not CHAT_ID:
    raise RuntimeError("Missing TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID")

def main():
    bot = Bot(token=TOKEN)

    message = (
        "🔔 Akramoffers Bot\n\n"
        "هذا تشغيل مجدول عبر GitHub Actions.\n"
        "سيتم هنا لاحقاً إرسال:\n"
        "- عروض ChatGPT / Gemini / Copilot\n"
        "- عروض Canva\n"
        "- عروض TradingView\n"
        "- ملخص يومي الساعة 7 مساءً\n\n"
        "✅ البوت يعمل بنجاح"
    )

    bot.send_message(chat_id=CHAT_ID, text=message)

if __name__ == "__main__":
    main()
