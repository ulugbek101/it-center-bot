from aiogram.dispatcher.filters import Filter
from aiogram.types import Message


class IsPrivate(Filter):
    """
    Chat type checking filter
    """
    key = "is_private"

    async def check(self, message: Message) -> bool:
        """
        Check if user is messaging in private chat
        :param message:
        :return: True if chat type is private, False otherwise
        """
        return message.chat.type == "private"
