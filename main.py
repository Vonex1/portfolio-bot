import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def get_main_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛠 Что я умею (Навыки)", callback_data="skills")],
        [InlineKeyboardButton(text="📁 Моё портфолио (GitHub)", url="https://github.com")],
        [InlineKeyboardButton(text="💬 Написать мне в ЛС", url="https://t.me/qqslp")]
    ])
    return keyboard

@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    welcome_text = (
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Я - бот-визитка Vonex1. 🚀\n"
        "Я создаю быстрых, надежных и функциональных Telegram-ботов для бизнеса и личных проектов на Python.\n\n"
        "Используй кнопки ниже, чтобы узнать подробнее о моих навыках или связаться со мной!"
    )
    await message.answer(text=welcome_text, reply_markup=get_main_keyboard())

@dp.callback_query(F.data == "skills")
async def show_skills(callback: asyncio.Task):
    await callback.answer()
    
    skills_text = (
        "🛠 Мой технологический стек:\n\n"
        "• Язык: Python 🐍\n"
        "• Библиотека: Aiogram 3.x (самая современная и быстрая)\n"
        "• Базы данных: SQLite / PostgreSQL (для хранения данных пользователей)\n"
        "• Инструменты: Git, GitHub, VS Code\n\n"
        "Готов разработать бота любой сложности: от простых визиток до магазинов и сложных систем автоматизации!"
    )
    
    await callback.message.answer(text=skills_text, reply_markup=get_main_keyboard())

async def main():
    print("Бот успешно запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())