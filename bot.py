import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

START_TEXT = """<b>Об AI GameBot</b>

Мы — проект для настоящих геймеров, которые хотят честную, глубокую информацию без коммерческих фильтров.

<b>Наша миссия</b>
Помочь тебе открывать лучшие игры, прокачивать навыки и получать максимум удовольствия от каждой игровой сессии — независимо от уровня и платформы.

<b>Что предлагаем</b>
- Честные обзоры игр
- Советы и гайды для всех уровней
- Актуальные новости гейминга
- Постоянные обновления

<b>Технология</b>
Подборки и материалы от экспертов игровой индустрии.

<b>Контакт:</b> скоро"""

MENU_TEXT = """🎮 <b>Главное меню</b>

Выбери раздел:"""

REVIEWS_TEXT = """🕹 <b>Обзоры игр</b>

<b>Elden Ring</b>
Шедевр от FromSoftware. Открытый мир, жёсткие боссы, невероятная атмосфера. Обязателен для тех, кто любит вызов.
⭐️ 10/10

<b>Baldur's Gate 3</b>
Лучшая RPG последних лет. Огромная свобода выбора, живые персонажи, сотни часов контента.
⭐️ 10/10

<b>Cyberpunk 2077</b>
После патчей — совсем другая игра. Мощный сюжет, атмосфера киберпанка, отличный открытый мир.
⭐️ 9/10"""

GUIDES_TEXT = """📖 <b>Советы и гайды</b>

<b>5 советов для любого геймера:</b>

1️⃣ <b>Изучи механики</b> — потрать 30 минут на туториал, сэкономишь часы потом

2️⃣ <b>Меняй чувствительность</b> — правильные настройки управления решают половину дела

3️⃣ <b>Делай паузы</b> — каждые 1.5 часа. Реакция и концентрация падают без отдыха

4️⃣ <b>Смотри реплеи</b> — анализируй свои ошибки как в спорте

5️⃣ <b>Играй в комфорте</b> — освещение, поза, гарнитура влияют на результат"""

NEWS_TEXT = """📰 <b>Новости гейминга</b>

🔥 <b>GTA VI</b>
Rockstar подтвердили выход в 2025. Действие в Майами, два главных героя, революционный открытый мир.

🔥 <b>Nintendo Switch 2</b>
Вышла в 2025. Обратная совместимость, улучшенный экран, новый Joy-Con с магнитным креплением.

🔥 <b>Xbox Game Pass</b>
Microsoft продолжает добавлять AAA-игры в день релиза. Один из лучших сервисов для геймеров.

🔥 <b>Инди-сцена</b>
2024-2025 — золотое время инди. Следи за Steam Next Fest — там всегда свежие жемчужины."""


def start_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("Главное меню", callback_data="main_menu"))
    return kb

def main_menu_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🕹 Обзоры игр", callback_data="reviews"),
        InlineKeyboardButton("📖 Советы и гайды", callback_data="guides"),
        InlineKeyboardButton("📰 Новости гейминга", callback_data="news"),
    )
    return kb

def back_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("◀️ В меню", callback_data="main_menu"))
    return kb


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer(START_TEXT, parse_mode="HTML", reply_markup=start_kb())

@dp.callback_query_handler(lambda c: c.data == "main_menu")
async def cb_main_menu(callback: types.CallbackQuery):
    await callback.message.answer(MENU_TEXT, parse_mode="HTML", reply_markup=main_menu_kb())
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "reviews")
async def cb_reviews(callback: types.CallbackQuery):
    await callback.message.answer(REVIEWS_TEXT, parse_mode="HTML", reply_markup=back_kb())
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "guides")
async def cb_guides(callback: types.CallbackQuery):
    await callback.message.answer(GUIDES_TEXT, parse_mode="HTML", reply_markup=back_kb())
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "news")
async def cb_news(callback: types.CallbackQuery):
    await callback.message.answer(NEWS_TEXT, parse_mode="HTML", reply_markup=back_kb())
    await callback.answer()

@dp.message_handler()
async def handle_message(message: types.Message):
    await message.answer("Используй меню для навигации 👇", reply_markup=start_kb())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)