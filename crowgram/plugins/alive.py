from crowgram import app
from pyrogram import filters


@app.on_message(filters.command(["alive"], ["."]))
async def check_userbot_status(client, message):
    return await message.reply_text("**I am Alive.**")
