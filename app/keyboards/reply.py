from aiogram.utils.keyboard import ReplyKeyboardBuilder


def reply_send_phone_number():
    reply_keyboard = ReplyKeyboardBuilder()

    reply_keyboard.button(text="Send phone", request_contact=True)

    return reply_keyboard.as_markup()
