from crowgram import *
from pyrogram import filters
from pytgcalls.types import *


@app.on_message(cdz(["stream"]) & ~filters.private)
async def test_media_stream(client, message):
    if message.sender_chat:
        return
    chat_id = message.chat.id
    link = (
        message.text.split(None, 1)[1]
        if len(message.command) != 1 else None
    )
    if not link:
        return
    stream = MediaStream(
        f"{link}",
        AudioQuality.HIGH,
        VideoQuality.HD_720p,
    )
    try:
        await call.join_group_call(chat_id, stream)
    except Exception:
        await call.change_stream(chat_id, stream)
    except:
        return

