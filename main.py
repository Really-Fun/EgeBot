import asyncio
import logging
from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.types import Message, LabeledPrice
from config_data import load_config, load_pay
from colorama import Fore
from handlers import default_handlers, tasks_handlers, material_handlers, database_handlers

async def main():

    logging.basicConfig(
        level=logging.INFO,
        format=Fore.RED + '%(filename)s:%(lineno)d #%(levelname)-8s '
        '[%(asctime)s] - %(name)s - %(message)s')

    logging.info('Strart Logging')

    config = load_config()

    bot: Bot = Bot(config.tg_bot.token, parse_mode='HTML')
    dis: Dispatcher = Dispatcher()

    @dis.message(Command(commands=['vip', 'Vip', 'VIP']))
    async def buy_vip(message: Message):
        a = load_pay()
        await bot.send_invoice(message.chat.id,
                           title="Подписка на бота",
                           description="Активация подписки на бота на 1 месяц",
                           provider_token=str(a),
                           currency="rub",
                           is_flexible=False,
                           prices=[LabeledPrice(label='Subscribe on bot', amount=100000)],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")

    dis.include_router(database_handlers.router)
    dis.include_router(default_handlers.router)
    dis.include_router(tasks_handlers.router)
    dis.include_router(material_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dis.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
