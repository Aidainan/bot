from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton


async def start_markup():
    about_us=InlineKeyboardButton(
        text='about us',
        callback_data='about_us'
    )
    menu=InlineKeyboardButton(
        text='menu',
        callback_data='menu'
    )
    review=InlineKeyboardButton(
        text='review',
        callback_data='review'
    )
    send_review=InlineKeyboardButton(
        text='send review',
        callback_data='send_review'
    )
    serial=InlineKeyboardButton(
        text='serial',
        callback_data='serial'

    )
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [about_us],
            [menu],
            [review],
            [send_review],
            [serial]
        ]
    )
    return markup


