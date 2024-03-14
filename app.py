import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import BotCommandScopeAllPrivateChats

from bot_cmds_list import command_list
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Футболки", callback_data="t_shirt"),
        ],
        {
            InlineKeyboardButton(text="Зипки", callback_data="zip"),
        },
        {
            InlineKeyboardButton(text="Кофты", callback_data="sweater"),
        },
        {
            InlineKeyboardButton(text="Головные уборы/Очки", callback_data="cap"),
        },
        {
            InlineKeyboardButton(text="Кроссовки", callback_data="shoes"),
        },
        {
            InlineKeyboardButton(text="Штаны", callback_data="trousers"),
        },
        {
            InlineKeyboardButton(text="Брендовая/Оригинальная одежда", callback_data="brend")
        },
        {
            InlineKeyboardButton(text="Отзывы", url="https://t.me/ff_poizon_otzivi"),
        }
    ],
)

brand = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Футболки", callback_data="t_shirt_brand"),
        ],
        {
            InlineKeyboardButton(text="Зипки", callback_data="zip_brand"),
        },
        {
            InlineKeyboardButton(text="Кофты", callback_data="sweater_brand"),
        },
        {
            InlineKeyboardButton(text="Головные уборы/Очки", callback_data="cap_brand"),
        },
        {
            InlineKeyboardButton(text="Кроссовки", callback_data="shoes_brand"),
        },
        {
            InlineKeyboardButton(text="Штаны", callback_data="trousers_brand"),
        },
    ],
)

brand_shoes = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Nike", callback_data="nike_shoes"),
        ],
        {
            InlineKeyboardButton(text="Puma", callback_data="puma_shoes"),
        },
        {
            InlineKeyboardButton(text="Reebok", callback_data="reebok_shoes"),
        },
        {
            InlineKeyboardButton(text="Alexander Mcqueen", callback_data="alex_shoes"),
        },
        {
            InlineKeyboardButton(text="Louis Vuitton", callback_data="louis_shoes"),
        },
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

@dp.callback_query(F.data == "t_shirt")
async def replik(callback: types.CallbackQuery):
    await callback.answer("")

    await callback.message.answer_photo(photo="AgACAgIAAxkBAAP0ZfMDahGv-n4NdkTwQgky4yesQMUAAsnWMRs9CJlLTJjnvmGbsh8BAAMCAAN4AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAP2ZfMDdLh6nnHi0dIpDDJAAy8FG90AAsrWMRs9CJlLOYbpSK6RKH0BAAMCAAN4AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAP4ZfMDeuVA_S2AwIRdgYVsYWLRzyEAAsvWMRs9CJlL7tOfQ0IjdW0BAAMCAAN5AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAP6ZfMDiA5luda51_PaOI6wG2THnG4AAs3WMRs9CJlLZV_ocnETOXkBAAMCAAN5AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBBWXzA6MO6ur3VmZSTfxlk53dvEMuAALV1jEbPQiZS4MYgwuToOroAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBBGXzA6M6BDqHFaNlfJlZpFi8ODuHAALU1jEbPQiZS8ascqT0hzwEAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBAmXzA6MLRjENI2IQ1sOYHvaM7P85AALR1jEbPQiZS-jdlZesVvYgAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBAWXzA6PG4PnjSR04nBDv-ij-KOzhAALS1jEbPQiZS3hFT_fRAgb5AQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAP_ZfMDo1igStBbOyYBdrYSlHSvRVEAAtDWMRs9CJlLStmBg7KwQZsBAAMCAAN5AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBA2XzA6OgQTXtS_pD6ahk9DAsLrHrAALT1jEbPQiZS9o7DLF6pmP0AQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBAAFl8wOjIgi0diW5GKxWv1qXad1uzwACz9YxGz0ImUtFqKQfEygCHAEAAwIAA3kAAzQE")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBBmXzA6NJ7wFs8o7XTKsoD6J2_w0IAALW1jEbPQiZSyhmtEt30d_EAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAP-ZfMDo2JbNLVCZOQg9UiRBvbem44AAs7WMRs9CJlL4LLFxxAUQnYBAAMCAAN5AAM0BA")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBEGXzBXcEKoQlcUD19fxJNESsDZ7SAALo1jEb9TqYS_Hfs0LJK1r0AQADAgADeAADNAQ",
                                        caption="У нас вы найдете футболки PREMIUM качества, а также дешёвую стоимость\n"
                                              "\nЦена: от 1 490,00 ₽ - до 2 490,00 ₽\n\nЕсли у вас есть вопросы или требуется помощь,"
                                              " обратитесь к нашему менеджеру.\n\nПолный ассортимент моделей👉🏻 "
                                              "https://t.me/ff_poizon", reply_markup=supp)

@dp.callback_query(F.data == "zip")
async def zip(callback: types.CallbackQuery):
    await callback.answer("")

    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBkWXzCORQUioVvvURbA70E1mzDS38AAIL1zEbPQiZS8HS0vzy9H6cAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBlGXzCOTlQseQJ1gMDjyHVZakCjOxAAIO1zEbPQiZSyDYC3JyP66LAQADAgADeAADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBjWXzCOT2rbU6TCYAAfnIRgkU5CKCVwACB9cxGz0ImUu7vNwJ4qXr2gEAAwIAA3kAAzQE")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBk2XzCORQ71cAASJIxzjYVpCJfIRviAACDdcxGz0ImUtz51n4GnTpAQEAAwIAA3kAAzQE")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBlWXzCOQQIlTIHbigumOfOfv3k6ZrAAIP1zEbPQiZS_x7c4LGfgMqAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBjGXzCOSNHYEsxKJ5Ip65hlSnoG6UAAIG1zEbPQiZS6nMUkHWGmJ4AQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBkGXzCOTK90SbYZGhpbJPzJPB6ulWAAIK1zEbPQiZS8SpwII6WIN4AQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBkmXzCOQyPuV5CYfzKHTl79HT-4KlAAIM1zEbPQiZS5jbCUELJ78iAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBj2XzCOTQkiI9eb4kNhnwVPD5zg7HAAIJ1zEbPQiZS9OKu8WXEt6tAQADAgADeAADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIBoGXzCV-_UIBdiOmPoHIV917ASqQnAAL41jEb9TqYSwZuL9LX8zPzAQADAgADeAADNAQ",
                                        caption="У нас вы найдете зипки PREMIUM качества, а также дешёвую стоимость\n"
                                              "\nЦена: от 3 490,00 ₽ - до 4 490,00 ₽\n\nЕсли у вас есть вопросы или требуется помощь,"
                                              " обратитесь к нашему менеджеру.\n\nПолный ассортимент моделей👉🏻 "
                                              "https://t.me/ff_poizon", reply_markup=supp)

@dp.callback_query(F.data == "sweater")
async def sweater(callback: types.CallbackQuery):
    await callback.answer("")

    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICDWXzDLK5ZaPTt7w0YDMox7k8AAFIGgACJNcxGz0ImUtRx2zqHOoDRQEAAwIAA3gAAzQE")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICC2XzDLJuDjrjEYRKxjDQRf_i47DMAAIi1zEbPQiZS9znJhGyBB--AQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICEGXzDLKM0j93xGVGZ-UDtdycSks4AAIp1zEbPQiZSxWlJExyrIzGAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICDGXzDLIcxchYLnq7vcATJuvzTj2_AAIj1zEbPQiZS49x0y-ymT45AQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICDmXzDLKrgGjq5z1eFw94bAmsAAE90wACJ9cxGz0ImUudjFGbOvCzygEAAwIAA3kAAzQE")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICCmXzDLIw4ZfhHEIieh3eu52BBx2BAAIh1zEbPQiZS5WblYnm0MstAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICD2XzDLKb-NU_aVOFUk36QahXayn3AAIo1zEbPQiZSxjk4OGR86cLAQADAgADeQADNAQ")

    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICGGXzDYBXIvbg4n7fsXwyjg9waiNWAAII1zEb9TqYS4pkjyDtxQ9GAQADAgADeAADNAQ",
                                        caption="У нас вы найдете кофты PREMIUM качества, а также дешёвую стоимость\n"
                                              "\nЦена: от 3 990,00 ₽ - до 4 990,00 ₽\n\nЕсли у вас есть вопросы или требуется помощь,"
                                              " обратитесь к нашему менеджеру.\n\nПолный ассортимент моделей👉🏻 "
                                              "https://t.me/ff_poizon", reply_markup=supp)

@dp.callback_query(F.data == "cap")
async def cap(callback: types.CallbackQuery):
    await callback.answer("")

    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICNGXzDp-6O0mNxQHOSARXFCRhvd9DAAIx1zEbPQiZSwl9x7uhNo_JAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICM2XzDp9sAAGDHwqxWDEp_D7__IP-sgACMNcxGz0ImUtumz1fVAqCZAEAAwIAA3gAAzQE")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICMmXzDp8Rr7-ZmO7ghXHNkw3zrbbYAAIv1zEbPQiZS6nM7T0AAbZuGAEAAwIAA3kAAzQE")

    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICPGXzD3dXvIvQWVM9RHXrZmenRpmoAAIL1zEb9TqYSzBZj8Fq64l6AQADAgADeAADNAQ",
                                        caption="У нас вы найдете головной убор/очки PREMIUM качества, а также дешёвую стоимость\n"
                                              "\nЦена: от 0 490,00 ₽ - до 1 090,00 ₽\n\nЕсли у вас есть вопросы или требуется помощь,"
                                              " обратитесь к нашему менеджеру.\n\nПолный ассортимент моделей👉🏻 "
                                              "https://t.me/ff_poizon", reply_markup=supp)

@dp.callback_query(F.data == "shoes")
async def shoes(callback: types.CallbackQuery):
    await callback.answer("")

    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICeGXzEKAqiLYbPAExQAdfqbrkYnrBAAJO1zEbPQiZS2v4NdFY7R1hAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICe2XzEKCZne_zX9Wk4eP1fsYuBJdPAAJR1zEbPQiZS4j7Z69EVNhMAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICeWXzEKAiay1GZE8PKdDQPRxshiLdAAJP1zEbPQiZS3BHrF6IqoqoAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICemXzEKCQaHSg91T2sm6jlW0P3o3QAAJQ1zEbPQiZS8eiNwHnQPbXAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICd2XzEKBMykVCiTmxC--X7fY7UCZTAAJN1zEbPQiZS6GWHpTYSB66AQADAgADeQADNAQ")

    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICgWXzEgvg4nb1Jm1Uu3o3TAKQOgJdAAIS1zEb9TqYS8DUzXbLOSqrAQADAgADeAADNAQ",
                                        caption="У нас вы найдете кроссовки PREMIUM качества, а также дешёвую стоимость\n"
                                              "\nЦена: 3 490,00 ₽\n\nЕсли у вас есть вопросы или требуется помощь,"
                                              " обратитесь к нашему менеджеру.\n\nПолный ассортимент моделей👉🏻 "
                                              "https://t.me/ff_poizon", reply_markup=supp)

@dp.callback_query(F.data == "trousers")
async def trousers(callback: types.CallbackQuery):
    await callback.answer("")

    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICkmXzE0KWLqrMtpaMFc8w4jfiWaXmAAJi1zEbPQiZS-dz88g_13hoAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICkWXzE0LDaUEn2BrBEdZjmYzKoSp9AAJh1zEbPQiZS5a0-Nvl-KOFAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICmGXzFF8uFHZuDnf-9Ue2xtrRjcprAAJn1zEbPQiZS7ba7wXCp4GwAQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICmWXzFF93KG9oxFznXDw82a69C_diAAJo1zEbPQiZS4C44luoGrK-AQADAgADeQADNAQ")
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAICl2XzFF8HZK0KjE9pu8FGSDZOk90nAAJm1zEbPQiZS6Avk0DQy_IRAQADAgADeQADNAQ")

    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIClWXzFBNfl5_StSr4uOmAuO1b3VjgAAIX1zEb9TqYS8AK06eDO2nPAQADAgADeAADNAQ",
                                        caption="У нас вы найдете штаны PREMIUM качества, а также дешёвую стоимость\n"
                                              "\nЦена: от 1 990,00 ₽ - до 2 490,00 ₽\n\nЕсли у вас есть вопросы или требуется помощь,"
                                              " обратитесь к нашему менеджеру.\n\nПолный ассортимент моделей👉🏻 "
                                              "https://t.me/ff_poizon", reply_markup=supp)


@dp.callback_query(F.data == "brend")
async def brend(callback: types.CallbackQuery):
    await callback.answer("Бренды/Оригинальные товары", show_alert=True)
    await callback.message.answer_photo(photo="AgACAgIAAxkBAAIDamXzTyF39ef90ZOvn979XmEdQ2WyAAJw2DEb9TqYS77uBMcjD9OyAQADAgADeAADNAQ",
                                        reply_markup=brand)


@dp.callback_query(F.data == "shoes_brand")
async def shoes_brand(callback: types.CallbackQuery):
    await callback.answer("Shoes")

    await callback.message.edit_caption(caption="<em>Выберите бренд:</em>", parse_mode="HTML", reply_markup=brand_shoes)


@dp.callback_query(F.data == "back")
async def back(callback: types.CallbackQuery):
    await callback.answer("")
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