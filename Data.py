from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo {}

━━━━━━━━━━━━━━━━━━━━━━━━
 {} di buat untuk Membantu anda Untuk Mengambil String Session Telegram dengan Mudah dan AMAN!
━━━━━━━━━━━━━━━━━━━━━━━━
Jika anda Tidak Mempercayai Bot ini:
1. Jangan dibaca Pesan ini
2. Hapus Pesan dan Blokir Bot ini
━━━━━━━━━━━━━━━━━━━━━━━━
Managed With ☕️ By @IdNyaZonk
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ", callback_data="generate")],
        [InlineKeyboardButton(text="ᴋᴇᴍʙᴀʟɪ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ", callback_data="generate")],
        [InlineKeyboardButton("⚡ᴊᴏɪɴ ꜰʀᴅs ᴘʀᴏᴊᴇᴄᴛ⚡", url="https://t.me/frdsproject")],
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("🔥ɢʀᴏᴜᴘ sᴜᴘᴘᴏʀᴛ"🔥, url="https://t.me/frdssupport")],
    ]

    # Help Message
    HELP = """
✨ Perintah Yang Tersedia

 × /start - Mulai Bot
 × /about - Tentang Bot ini
 × /ping - Untuk Mengecek Ping Bot
 × /id - Untuk Mendapatkan User ID
 × /generate - Mulai Pengambilan String
 × /cancel - Membatalkan Proses Pengambilan String
 × /restart - Merestart Proses Pengambilan String
"""

    # About Message
    ABOUT = """
Tentang Bot ini:

 {} di buat untuk Membantu anda Untuk Mengambil String Session Telegram dengan Simple dan Mudah!

 • Group Support: @frdssupport
 • Framework: Pyrogram
 • Language: Python

👨‍💻 Develoved by @IdNyaZonk
    """
