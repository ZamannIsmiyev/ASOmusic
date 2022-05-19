from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# YarasaMusic tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://te.legra.ph/file/ce31f843b674aeb14064a.jpg",
                caption=(f"""**Salam {message.from_user.mention} 🎵\nBen {bot}!\nSesli sohbetlerde musiqi oxuyan botam. Ban yetkisiz, Sesli yetkisi verib, /gel yazaraq Asistanı gruba atın.\n\nDüzen Tasarım [ASO Music Bot 🎙️](https://t.me/Asomusicbot).**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Məni Grupa At ❱ ➕", url=f"https://t.me/ASOmusicbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👨‍🔧ASO Rəsmi", url="https://t.me/ASOresmi"
                    ),
                    InlineKeyboardButton(
                        "💬 ASO Paytaxt", url="https://t.me/ASOSonZirve"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Menyu" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "ASO Rəsmi 🇦🇿", url=f"https://t.me/ASOresmi"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{ASOmusicbot}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Not:\n Botun aktif işləməsi üçün yetkiye ehtiyac vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔴 Hamı üçün menyu", callback_data="herkes")
                 ],[                     
                     InlineKeyboardButton(
                         "⚫ Adminler için menyu", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Baş Menyu🏠", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "⚙ Sahibim", url="https://t.me/ismiyev95")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Not:\nBotun aktif işləməsi üçün yetkiye ehtiyacı vardır:\n- Mesaj silme yetkisi,\n- Bağlantı ile davet etme yetkisi,\n- Sesli sohbeti yönetme yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "✨Herkes için Menyu", callback_data ="herkes")
        ],
        [
          InlineKeyboardButton(
            "👑Adminlər Menyusu",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🏠Baş Səhifə", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "⚙ Sahibim", url="https://t.me/ismiyev95")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun herkes üçün işləmə menüsü 😉\n\n ▶️ /play - musiqi oxumaq üçün youtube url'sine veya musiqi dosyasına yanıt verme\n ▶️ /play <song name> - istediyiniz musiqini yazın\n 🔴 \n 🎵 /tap <song name> - istediyiniz musiqiləri tez bir zamanda tapın\n 🎵 /vtap istediyiniz videoları tez bir zamanda tapın\n 🔍 /axtar <query> - youtube'da ayrıntıları içeren videoları arama\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Sahibim", url="https://t.me/ismiyev95")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminler için işləmə menüsü 🤩\n\n ▶️ /davam - musiqi oxumaqa davam et\n ⏸️ /dayan - oxuyan parçayı dayandırmaq üçün\n 🔄 /kec- Sırada olan müsiqi parçasını dəyişər.\n ⏹ /dur - müsiqi oxumağı durdurma\n 🔼 /ver bot sadeceler yöneticiler üçün işlədə bilər adminler işlədə bilməsi üçün  yetki ver\n 🔽 /al botun yönetici menyusunu işlədə bilen userin yetkisini al\n\n ⚪ /gel - Musiqi asistanı grubunuza qatılır.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Sahibim", url="https://t.me/ismiyev95")
                 ],
                 [
                     InlineKeyboardButton(
                         "⬅️ Geri ⬅️", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Merhaba {query.from_user.mention} 🎵\nBen {bot}!\nSesli sohbetlerde müzik çalabilen botum. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz.\n\nDüzen Tasarım [Yarasa Music 🎙️](https://t.me/YarasaMMC).**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Məni Grupa At ❱ ➕", url=f"https://t.me/Asomusicbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "👨‍🔧 ASO Rəsmi", url="https://t.me/ASOrəsmi"
                    ),
                    InlineKeyboardButton(
                        "💬 ASO Paytaxt", url="https://t.me/ASOSonZirve"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🌀 Menyular" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "ASO Rəsmi 🇦🇿", url=f"https://t.me/AsoRəsmi"
                    )
                ]
                
           ]
        ),
    )
