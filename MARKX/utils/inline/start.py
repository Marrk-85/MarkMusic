from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from MARKX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="» Aᴅᴅ ᴍᴇ ʙᴀʙʏ «",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="•ʜᴇʟᴩ•",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="•sᴇᴛᴛɪɴɢs•", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="•Mᴏɪ ᴏᴡɴᴇʀ•", user_id=OWNER),
            InlineKeyboardButton(
                text="•ɢʀᴏᴜᴩ•", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="» Aᴅᴅ ᴍᴇ ʙᴀʙʏ «",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="•ʜᴇʟᴩ•", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(text="•ᴅᴇᴠᴇʟᴏᴘᴇʀ•", url=f"https://t.me/marrk_85"),
        ],
        [ 
            InlineKeyboardButton(text="•ᴄʜᴀɴɴᴇʟ•", url=f"{config.SUPPORT_CHANNEL}"),
            InlineKeyboardButton(text="•ɢʀᴏᴜᴩ•", url=f"{config.SUPPORT_GROUP}"),
        ],
        [
            InlineKeyboardButton(text="•sᴏᴜʀᴄᴇ•", url=f"{config.UPSTREAM_REPO}"),
            InlineKeyboardButton(text="•Mᴏɪ ᴏᴡɴᴇʀ•", user_id=OWNER)
        ],
     ]
    return buttons



