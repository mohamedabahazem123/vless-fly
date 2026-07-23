import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")  # On va le mettre dans Replit Secrets
bot = telebot.TeleBot(TOKEN)

# Ton lien VLESS
VLESS_LINK = "vless://53f3e66a-4d03-4c55-9b41-6aeee4c0a0e2@69.46.46.31:443?encryption=none&type=ws&host=vless-fly-production.up.railway.app&path=%2FTelegram%2F%40MarocProxy%2F%40Server1&security=tls&sni=vless-fly-production.up.railway.app#Railway-Free"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"""🔥 Bienvenue sur MarocProxy 🔥

Copie ta config VLESS :

`{VLESS_LINK}`

**Comment l'utiliser:**
1. Copie le lien
2. V2rayNG > `+` > `Import from clipboard`
3. Connecte ✅

Groupe: @MarocProxy
Serveur: @Server1
""")

@bot.message_handler(commands=['config'])
def send_config(message):
    bot.reply_to(message, f"`{VLESS_LINK}`")

print("Bot is running...")
bot.infinity_polling()
