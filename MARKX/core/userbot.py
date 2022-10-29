import sys

from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).info(f"Gettings Assistants Info...")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("CRAXYMARRK")
                await self.one.join_chat("marrkmusic")
            except:
                pass
            assistants.append(1)
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(
                f"Assistant Started as {self.one.name}"
            )
            try:
                await self.one.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴏɴᴇ sᴛᴀʀᴛᴇᴅ :**\n\n➻ ɪᴅ : `{self.one.id}`\n➻ ɴᴀᴍᴇ : {self.one.name}\n➻ ᴜsᴇʀɴᴀᴍᴇ : @{self.one.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("CRAXYMARRK")
                await self.two.join_chat("marrkmusic")
            except:
                pass
            assistants.append(2)
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.two.name = get_me.first_name
            try:
                await self.two.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴛᴡᴏ sᴛᴀʀᴛᴇᴅ :**\n\n➻ ɪᴅ : `{self.two.id}`\n➻ ɴᴀᴍᴇ : {self.two.name}\n➻ ᴜsᴇʀɴᴀᴍᴇ : @{self.two.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Assistant Two Started as {self.two.name}"
            )
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("CRAXYMARRK")
                await self.three.join_chat("marrkmusic")
            except:
                pass
            assistants.append(3)
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.three.name = get_me.first_name
            try:
                await self.three.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ᴛʜʀᴇᴇ sᴛᴀʀᴛᴇᴅ :**\n\n➻ ɪᴅ : `{self.three.id}`\n➻ ɴᴀᴍᴇ : {self.three.name}\n➻ ᴜsᴇʀɴᴀᴍᴇ : @{self.three.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Assistant Three Started as {self.three.name}"
            )
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("CRAXYMARRK")
                await self.four.join_chat("marrkmusic")
            except:
                pass
            assistants.append(4)
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.four.name = get_me.first_name
            try:
                await self.four.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ғᴏᴜʀ sᴛᴀʀᴛᴇᴅ :**\n\n➻ ɪᴅ : `{self.four.id}`\n➻ ɴᴀᴍᴇ : {self.four.name}\n➻ ᴜsᴇʀɴᴀᴍᴇ : @{self.four.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Assistant Four Started as {self.four.name}"
            )
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("CRAXYMARRK")
                await self.five.join_chat("marrkmusic")
            except:
                pass
            assistants.append(5)
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = (
                    get_me.first_name + " " + get_me.last_name
                )
            else:
                self.five.name = get_me.first_name
            try:
                await self.five.send_message(
                    config.LOG_GROUP_ID, f"**» {config.MUSIC_BOT_NAME} ᴀssɪsᴛᴀɴᴛ ғɪᴠᴇ sᴛᴀʀᴛᴇᴅ :**\n\n➻ ɪᴅ : `{self.five.id}`\n➻ ɴᴀᴍᴇ : {self.five.name}\n➻ ᴜsᴇʀɴᴀᴍᴇ : @{self.five.username}"
                )
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin ! "
                )
                sys.exit()
            LOGGER(__name__).info(
                f"Assistant Five Started as {self.five.name}"
            )
