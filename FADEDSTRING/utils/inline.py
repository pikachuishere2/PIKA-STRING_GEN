from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="⦿ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ⦿", callback_data="gensession")
                ],
                [
                    InlineKeyboardButton("⦿ sᴜᴘᴘᴏʀᴛ ⦿", url="https://t.me/YourSexyGc"),
                    InlineKeyboardButton("⦿ ᴜᴘᴅᴀᴛᴇ ⦿", url="https://t.me/PikaBotUpdates")
                ],
                [
                    
                    InlineKeyboardButton("⦿ ᴏᴡɴᴇʀ ⦿", url="https://t.me/CertifiedSexer"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="ᴛʀʏ ᴀɢᴀɪɴ", callback_data="gensession")]]
)
