from pyrogram import Client, enums

from config import LOGGER, Config
from user import User


class Bot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            "oxmohsen_bot",
            api_hash=Config.API_HASH,
            api_id=Config.APP_ID,
            bot_token=Config.TG_BOT_TOKEN,
            sleep_threshold=0,
            plugins={"root": "plugins"},
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot {usr_bot_me.first_name} (@{usr_bot_me.username}) started!")
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
