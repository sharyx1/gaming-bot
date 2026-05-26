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
- Ulasan game yang jujur dan detail
- Tips dan panduan untuk semua level
- Berita gaming terkini
- Update rutin tentang industri game

<b>Teknologi</b>
Konten pilihan dari para ahli industri game."""

MENU_TEXT = """🎮 <b>Menu Utama</b>

Pilih kategori yang ingin kamu jelajahi:"""

REVIEWS_TEXT = """🕹 <b>Ulasan Game</b>

<b>Elden Ring</b>
Mahakarya dari FromSoftware. Dunia terbuka yang luas, bos yang menantang, atmosfer luar biasa. Wajib dimainkan bagi yang suka tantangan tinggi.
⭐️ 10/10

<b>Baldur's Gate 3</b>
RPG terbaik dalam beberapa tahun terakhir. Kebebasan pilihan yang luar biasa, karakter yang hidup, ratusan jam konten. Masterpiece modern.
⭐️ 10/10

<b>Cyberpunk 2077</b>
Setelah berbagai patch — game yang benar-benar berbeda dan layak dimainkan. Cerita kuat, atmosfer cyberpunk yang unik, open world yang imersif.
⭐️ 9/10

<b>Baldur's Gate 3</b>
Game strategi yang challenging dengan mekanik unik. Cocok untuk pemain yang menginginkan pengalaman berbeda dan depth gameplay.
⭐️ 8/10"""

GUIDES_TEXT = """📖 <b>Tips & Panduan</b>

<b>5 Tips untuk Semua Gamer:</b>

1️⃣ <b>Pelajari mekanik</b> — luangkan 30 menit untuk tutorial, hemat berjam-jam bermain setelahnya dengan pemahaman yang benar

2️⃣ <b>Atur sensitivitas</b> — pengaturan kontrol yang tepat menentukan setengah dari performa bermain kamu

3️⃣ <b>Ambil jeda rutin</b> — setiap 1,5 jam. Reaksi dan konsentrasi menurun signifikan tanpa istirahat

4️⃣ <b>Tonton dan analisis replay</b> — analisis kesalahanmu seperti dalam olahraga profesional

5️⃣ <b>Bermain dengan nyaman</b> — pencahayaan ruangan, postur duduk, dan headset berkualitas mempengaruhi hasil gameplay

<b>Tips Bonus:</b>
- Jangan bermain dalam keadaan lelah atau emosi tinggi
- Atur brightness monitor sesuai pencahayaan ruangan
- Gunakan mouse pad yang cukup besar untuk game FPS"""

NEWS_TEXT = """📰 <b>Berita Gaming</b>

🔥 <b>GTA VI</b>
Rockstar Games mengkonfirmasi rilis di 2025. Berlatar di Miami, dua karakter utama yang dapat ditukar, open world yang revolusioner dengan teknologi terbaru.

🔥 <b>Nintendo Switch 2</b>
Konsol generasi baru telah rilis di 2025. Kompatibilitas mundur dengan library Switch, layar OLED yang ditingkatkan, Joy-Con baru dengan fitur magnetik.

🔥 <b>Xbox Game Pass</b>
Microsoft terus menambahkan game AAA di hari rilis. Koleksi terus berkembang dengan franchise besar dari studio Microsoft dan partner lainnya.

🔥 <b>Indie Scene 2025</b>
Era emas game indie terus berlanjut. Steam Next Fest menampilkan ratusan game indie berkualitas tinggi yang patut untuk dicoba."""

ABOUT_TEXT = """<b>Tentang Bot Ini</b>

Bot gaming ini dibuat untuk memberikan informasi mendalam tentang dunia gaming tanpa iklan komersial atau sponsor yang mengganggu.

<b>Konten Kami:</b>
✓ Ulasan game yang objektif dan detail
✓ Tips gameplay dari pemain berpengalaman
✓ Berita industri gaming terkini
✓ Rekomendasi game berdasarkan preferensi

<b>Komitmen Kami:</b>
Memberikan konten berkualitas yang benar-benar membantu gamer menemukan game favorit mereka dan meningkatkan pengalaman bermain.

Setiap konten dikurasi dengan cermat oleh tim yang passionate tentang gaming."""

CONTACT_TEXT = """<b>Hubungi Kami</b>

Untuk pertanyaan, saran, atau feedback tentang bot ini:

📧 Email: contact@gameaibot.com
🔗 Telegram Channel: t.me/GameAIBot
💬 Support: @GameAIBot_Support

Kami menghargai setiap masukan dari komunitas gaming kami. Feedback kamu membantu kami terus berkembang dan memberikan konten yang lebih baik.

Bergabunglah dengan komunitas gamer kami dan dapatkan update terbaru tentang game dan tips gaming!"""

HELP_TEXT = """<b>Apa yang Bisa Bot Lakukan?</b>

Bot ini menyediakan berbagai fitur untuk membantu perjalanan gaming kamu:

🕹️ <b>Ulasan Game</b> — Dapatkan ulasan mendalam tentang game populer dengan rating dan detail gameplay

📖 <b>Tips & Panduan</b> — Pelajari tips dari pemain berpengalaman untuk meningkatkan skill kamu

📰 <b>Berita Gaming</b> — Tetap update dengan berita terbaru dari dunia gaming dan industri game

ℹ️ <b>Tentang Bot</b> — Pelajari lebih lanjut tentang misi dan komitmen bot ini

📞 <b>Hubungi Kami</b> — Temukan cara untuk menghubungi tim kami atau bergabung dengan komunitas

Gunakan menu di bawah untuk mengakses fitur-fitur ini dan nikmati pengalaman gaming yang lebih baik!"""


def start_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("Menu Utama", callback_data="main_menu"))
    return kb

def main_menu_kb():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🕹 Ulasan game", callback_data="reviews"),
        InlineKeyboardButton("📖 Tips & panduan", callback_data="guides"),
        InlineKeyboardButton("📰 Berita gaming", callback_data="news"),
        InlineKeyboardButton("ℹ️ Tentang bot", callback_data="about"),
        InlineKeyboardButton("📞 Hubungi kami", callback_data="contact"),
        InlineKeyboardButton("❓ Apa yang bisa bot?", callback_data="help"),
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

@dp.callback_query_handler(lambda c: c.data == "about")
async def cb_about(callback: types.CallbackQuery):
    await callback.message.answer(ABOUT_TEXT, parse_mode="HTML", reply_markup=back_kb())
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "contact")
async def cb_contact(callback: types.CallbackQuery):
    await callback.message.answer(CONTACT_TEXT, parse_mode="HTML", reply_markup=back_kb())
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data == "help")
async def cb_help(callback: types.CallbackQuery):
    await callback.message.answer(HELP_TEXT, parse_mode="HTML", reply_markup=back_kb())
    await callback.answer()

@dp.message_handler()
async def handle_message(message: types.Message):
    await message.answer("Gunakan menu untuk navigasi 👇", reply_markup=start_kb())


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)