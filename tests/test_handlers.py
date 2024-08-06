from unittest.mock import AsyncMock
import pytest

from handlers.default_handlers import get_help, get_start
from keyboards import keyboard_start
from lexicon_ru.lexicon import commands


@pytest.mark.asyncio
async def test_help_handler():
    message = AsyncMock()
    await get_help(message)

    message.answer.assert_called_with(commands["/help"], reply_markup=keyboard_start)


@pytest.mark.asyncio
async def test_start_handler():
    message = AsyncMock()
    message.from_user.id = "1111111"
    await get_start(message)

    message.answer.assert_called_with(commands["/start"], reply_markup=keyboard_start)


if __name__ == "__main__":
    result = pytest.main()
