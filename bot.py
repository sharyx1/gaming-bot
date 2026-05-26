import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

START_TEXT = """<b>Tentang AI GameBot</b>

Kami adalah proyek untuk para gamer sejati yang menginginkan informasi jujur, mendalam, dan bebas dari filter komersial.

<b>Misi Kami</b>
Membantu kamu menemukan game terbaik, meningkatkan skill, dan mendapatkan pengalaman bermain maksimal — untuk semua level dan platform.

<b>Yang Kami Tawarkan</b>
- Ulasan game yang jujur
- Tips dan panduan untuk semua level
- Berita gaming terkini
- Update rutin

<b>Teknologi</b>
Konten pilihan dari para ahli industri game.

<b>Kontak:</b> segera hadir"""

MENU_TEXT = """🎮 <b>Menu Utama</b>

Pilih kategori:"""

REVIEWS_TEXT = """🕹 <b>Ulasan Game</b>

<b>Elden Ring</b>
Mahakarya dari FromSoftware. Dunia terbuka, bos yang menantang, atmosfer luar biasa. Wajib dimainkan bagi yang suka tantangan.
⭐️ 10/10

<b>Baldur's Gate 3</b>
RPG terbaik dalam beberapa tahun terakhir. Kebebasan pilihan yang luar biasa, karakter hidup, ratusan jam konten.
⭐️ 10/10

<b>Cyberpunk 2077</b>
Setelah berbagai patch — game yang benar-benar berbeda. Cerita kuat, atmosfer cyberpunk, open world yang keren.
⭐️ 9/10"""

GUIDES_TEXT = """📖 <b>Tips & Panduan</b>

<b>5 Tips untuk Semua Gamer:</b>

1️⃣ <b>Pelajari mekanik</b> — luangkan 30 menit untuk tutorial, hemat berjam-jam setelahnya

2️⃣ <b>Atur sensitivitas</b> — pengaturan kontrol yang tepat menentukan setengah dari permainan

3️⃣ <b>Ambil jeda</b> — setiap 1,5 jam. Reaksi dan konsentrasi menurun tanpa istirahat

4️⃣ <b>Tonton replay</b> — analisis kesalahanmu seperti dalam olahraga

5️⃣ <b>Bermain dengan nyaman</b> — pencahayaan, postur, dan headset mempengaruhi hasil"""

NEWS_TEXT = """📰 <b>Berita Gaming</b>

🔥 <b>GTA VI</b>
Rockstar mengkonfirmasi rilis di 2025. Berlatar di Miami, dua karakter utama, open world yang revolusioner.

🔥 <b>Nintendo Switch 2</b>
Rilis di 2025. Kompatibilitas mundur, layar yang ditingkatkan, Joy-Con baru dengan pemasangan magnetik.

🔥 <b>Xbox Game Pass</b>
Microsoft terus menambahkan game AAA di hari rilis. Salah satu layanan terbaik untuk gamer.

🔥 <b>Indie Scene</b>
2024-2025 adalah era emas indie. Pantau Steam Next Fest — selalu ada permata baru di sana."""


def start_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("Menu Utama", callback_data="main_menu"))
    return kb

def main_menu_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🕹 Ulasan Game", callback_data="reviews"),
        InlineKeyboardButton("📖 Tips & Panduan", callback_data="guides"),
        InlineKeyboardButton("📰 Berita Gaming", callback_data="news"),
    )
    return kb

def back_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("◀️ Menu", callback_data="main_menu"))
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
    await message.answer("Gunakan menu untuk navigasi 👇", reply_markup=start_kb())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)