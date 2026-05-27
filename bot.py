import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔐 Купить VPN")],
        [KeyboardButton(text="📅 Моя подписка")],
        [KeyboardButton(text="📖 Инструкция")],
        [KeyboardButton(text="💬 Поддержка")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "🔥 Добро пожаловать в DEVICE VPN\n\n"
        "Тариф: 100₽ / 30 дней",
        reply_markup=menu
    )

@dp.message()
async def menu_handler(message: types.Message):
    text = message.text

    if text == "🔐 Купить VPN":
        await message.answer(
            "💳 Оплата скоро будет подключена.\n\n"
            "DEVICE VPN\n100₽ / 30 дней"
        )

    elif text == "📅 Моя подписка":
        await message.answer("📅 Подписка пока не найдена.")

    elif text == "📖 Инструкция":
        await message.answer(
            "📲 После покупки бот выдаст VLESS ссылку и QR."
        )

    elif text == "💬 Поддержка":
        await message.answer(
            "Поддержка: @fix_device"
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
