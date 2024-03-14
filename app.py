import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import BotCommandScopeAllPrivateChats

from bot_cmds_list import command_list
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Реплика", callback_data="replik"),
        ],
        {
            InlineKeyboardButton(text="Одежда", callback_data="clothes"),
        },
        {
            InlineKeyboardButton(text="Кроссовки", callback_data="shoes"),
        },
        {
            InlineKeyboardButton(text="Брендовая одежда", callback_data="brend"),
        },
        {
            InlineKeyboardButton(text="Отзывы", callback_data="otzivi"),
        }
    ],
)

supp = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Написать менеджеру", url="https://t.me/official_supp_t"),
        ],
        {
            InlineKeyboardButton(text="Назад", callback_data="back"),
        },
    ],
)

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
    await message.answer_photo(photo="AgACAgIAAxkBAANVZfLt3Tltjd8sYwkFLiMgLpumMWcAAmLWMRv1OphLSVFOIRMNa-wBAAMCAAN4AAM0BA", reply_markup=start_kb)

@dp.callback_query(F.data == "replik")
async def replik(callback: types.CallbackQuery):
    await callback.message.answer_photo(photo="AgACAgIAAxkBAANsZfL1e5gh_nn4ZQdsdb2DQ7_V-JQAApTWMRv1OphLWg8f7UPK2O0BAAMCAAN5AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAANuZfL1hPLBB_IPLGKiI5Vj2HtRmY0AApXWMRv1OphLLufGyPZj2sMBAAMCAAN5AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAANwZfL1iPikRrHbDV9chZtcTVNsrksAApbWMRv1OphLfJaqcZDTUp0BAAMCAAN5AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAANyZfL1jsRC5ToBBP20GoSaX1JLPk4AApfWMRv1OphLdWjM8O-V-wwBAAMCAAN5AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAN-ZfL349zhp5YGWJnrFFDPsHwrhKkAAqTWMRv1OphLybj1megV7FIBAAMCAAN4AAM0BA",
                                        caption="У нас вы найдете реплику PREMIUM качества, которая ничем не отличается от оригинала\n"
                                              "\nЦена: от 2 490,00 ₽\n\nЕсли у вас есть вопросы или требуется помощь,"
                                              " обратитесь к нашему менеджеру.\n\nПолный ассортимент моделей👉🏻 "
                                              "https://t.me/ff_poizon", reply_markup=supp)

@dp.callback_query(F.data == "clothes")
async def replik(callback: types.CallbackQuery):
    await callback.message.answer_photo(photo="AgACAgIAAxkBAANsZfL1e5gh_nn4ZQdsdb2DQ7_V-JQAApTWMRv1OphLWg8f7UPK2O0BAAMCAAN5AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAANuZfL1hPLBB_IPLGKiI5Vj2HtRmY0AApXWMRv1OphLLufGyPZj2sMBAAMCAAN5AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAANwZfL1iPikRrHbDV9chZtcTVNsrksAApbWMRv1OphLfJaqcZDTUp0BAAMCAAN5AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAANyZfL1jsRC5ToBBP20GoSaX1JLPk4AApfWMRv1OphLdWjM8O-V-wwBAAMCAAN5AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAN-ZfL349zhp5YGWJnrFFDPsHwrhKkAAqTWMRv1OphLybj1megV7FIBAAMCAAN4AAM0BA",
                                        caption="У нас вы найдете реплику PREMIUM качества, которая ничем не отличается от оригинала\n"
                                              "\nЦена: от 2 490,00 ₽\n\nЕсли у вас есть вопросы или требуется помощь,"
                                              " обратитесь к нашему менеджеру.\n\nПолный ассортимент моделей👉🏻 "
                                              "https://t.me/ff_poizon", reply_markup=supp)







@dp.callback_query(F.data == "back")
async def back(callback: types.CallbackQuery):
    await callback.message.answer(
        f"<em>Здравствуйте, <b>{callback.message.from_user.full_name}</b>! Я бот магазина FF Poizon. Я могу прислать подробные фото "
        f"о каждом товаре. Для этого выберите кнопкой ниже нужную категорию "
        f"и там найдите интересующий товар. Я скину всю информацию, которая у меня есть</em>", parse_mode="HTML")
    await callback.message.answer_photo(
        photo="AgACAgIAAxkBAANVZfLt3Tltjd8sYwkFLiMgLpumMWcAAmLWMRv1OphLSVFOIRMNa-wBAAMCAAN4AAM0BA",
        reply_markup=start_kb)



@dp.message(F.photo)
async def photo(message: types.Message):
    photo_data = message.photo[-1]

    await message.answer(f'{photo_data}')

async def main():
    await bot.set_my_commands(commands=command_list, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


asyncio.run(main())