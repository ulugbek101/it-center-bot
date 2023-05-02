from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from environs import Env

from data import config
from utils.db_api.database import Database


env = Env()
env.read_env()

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database(
    db_name=env.str("DB_NAME"),
    db_user=env.str("DB_USER"),
    db_password=env.str("DB_PASSWORD"),
    db_port=env.int("DB_PORT"),
    db_host=env.str("DB_HOST"),
)
