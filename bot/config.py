import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN: str = str(os.getenv('BOT_TOKEN'))

admins: list[int] = [367757357]

page: int = 0