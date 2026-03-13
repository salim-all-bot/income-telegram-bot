import telebot
import json
import os

TOKEN = "8792695521:AAEq0qyTQSDUj-r-Nmt3G1fEZkMY_KGmDYQ"
ADMIN = 8541526129  # admin telegram id

bot = telebot.TeleBot(TOKEN)

DB = "users.json"

def load():
    if not os.path.exists(DB):
        return {}
    with open(DB,"r") as f:
        return json.load(f)

def save(data):
    with open(DB,"w") as f:
        json.dump(data,f)

@bot.message_handler(commands=['start'])
def start(message):

    users = load()
    uid = str(message.from_user.id)

    if uid not in users:

        users[uid] = {
            "balance":0,
            "ref":0
        }

        if len(message.text.split()) > 1:
            ref = message.text.split()[1]

            if ref in users:

                users[ref]["balance"] += 15
                users[ref]["ref"] += 1

    save(users)

    link = f"https://t.me/{bot.get_me().username}?start={uid}"

    bot.send_message(message.chat.id,f"""
💰 Welcome to Income Bot

💵 Balance: {users[uid]['balance']} Tk
👥 Referrals: {users[uid]['ref']}

🔗 Your Link:
{link}

Invite friends & earn 15 Tk
""")

@bot.message_handler(commands=['balance'])
def balance(message):

    users = load()
    uid = str(message.from_user.id)

    bal = users.get(uid,{"balance":0})["balance"]

    bot.send_message(message.chat.id,f"💰 Balance: {bal} Tk")

@bot.message_handler(commands=['task'])
def task(message):

    bot.send_message(message.chat.id,
"""
📌 Task

Join this bot
https://t.me/examplebot

Reward: 15 Tk
""")

@bot.message_handler(commands=['withdraw'])
def withdraw(message):

    users = load()
    uid = str(message.from_user.id)

    bal = users.get(uid,{"balance":0})["balance"]

    if bal < 100:

        bot.send_message(message.chat.id,
        "❌ Minimum withdraw 100 Tk")

    else:

        bot.send_message(ADMIN,
        f"Withdraw request from {uid}\nBalance: {bal}")

        bot.send_message(message.chat.id,
        "✅ Withdraw request sent")

bot.infinity_polling()
