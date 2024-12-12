from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
❥ ωєℓ¢σмє тσ тєαм ❍𝐒ʏsᴛᴇᴍ 𝐌ᴜsɪᴄ❍

❥ ʀᴇᴘᴏ ᴄʜᴀᴀʜɪʏʀ ᴛᴏ ʙᴏᴛ ᴋᴏ 

❥ Bᴀᴅɴᴀᴍ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ ʀᴇᴘᴏ Jᴀʙ ᴍɪʟᴇɢᴀ

❥ ᴀᴅᴍɪɴ ʙᴀɴᴏ ᴀᴜʀ sᴄʀᴇᴇɴsʜᴏᴛ 
     
❥ ᴏᴡɴᴇʀ ᴋᴏ Bᴀᴅɴᴀᴍ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ ʀᴇᴘᴏ Jᴀʙ ᴍɪʟᴇɢᴀ

"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("💠 𝖠ᴅᴅ ᴍᴇ 𝖡ᴀʙʏ 💠", url=f"https://t.me/system_music_prorobot?startgroup=true")
        ],
        [
          InlineKeyboardButton("❍𝐒ᴜᴘᴘᴏʀᴛ❍", url="@SYSTEM_BOT_UPDATE"),
          InlineKeyboardButton("❍𝐒ʏsᴛᴇᴍ 𝐌ᴜsɪᴄ❍ ", url="@SYSTEM_BOT_UPDATE"),
          ],
               [
                InlineKeyboardButton("ᴏᴛʜᴇʀ ʙᴏᴛs", url=f"@SYSTEM_BOT_UPDATE"),
],
[
InlineKeyboardButton("ᴄʜᴇᴄᴋ", url=f"https://t.me/system_music_prorobot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/arnzab.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
