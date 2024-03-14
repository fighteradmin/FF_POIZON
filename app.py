import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import BotCommandScopeAllPrivateChats

from bot_cmds_list import command_list

bot = Bot(token="7176823300:AAGzo8nLwWhOF9S4VbQQ2hXeWwQHUnT2fV8")

dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await bot.send_sticker(message.from_user.id,
                           sticker="CAACAgIAAxkBAAELsPVl8tZBgN2WDzAFRNlu4ag8K05LuwAC0Q0AAstxcEvO1r8zXvNYlzQE")
    await message.answer(
        f"<em>Здравствуйте, <b>{message.from_user.full_name}</b>! Я бот магазина FF Poizon. Я могу прислать подробные фото "
        f"о каждом товаре. Для этого выберите кнопкой ниже нужную категорию "
        f"и там найдите интересующий товар. Я скину всю информацию, которая у меня есть</em>", parse_mode="HTML")


async def main():
    await bot.set_my_commands(commands=command_list, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


asyncio.run(main())