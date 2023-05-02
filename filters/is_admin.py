from aiogram.dispatcher.filters import Filter
from aiogram.types import Message

from environs import Env

env = Env()
env.read_env()
ADMINS = env.list("ADMINS")
ADMINS = [int(admin) for admin in ADMINS]


class IsAdmin(Filter):
    """
    Filter to check whether a user is an admin
    """

    key = "is_admin"

    async def check(self, message: Message) -> bool:
        """
        Check if user is an admin
        :param message:
        :return: True or False
        """
        return message.from_user.id in ADMINS
