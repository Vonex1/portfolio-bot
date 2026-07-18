import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from aiohttp import web

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def get_main_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛠 Что я умею (Навыки)", callback_data="skills")],
        [InlineKeyboardButton(text="📁 Моё портфолио (GitHub)", url="https://github.com/Vonex1")],
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
        "• Библиотека: Aiogram 3.x\n"
        "• Базы данных: SQLite / PostgreSQL\n"
        "• Инструменты: Git, GitHub, VS Code\n\n"
        "Готов разработать бота любой сложности!"
    )
    
    await callback.message.answer(text=skills_text, reply_markup=get_main_keyboard())

async def handle(request):
    return web.Response(text="Бот работает!")

async def web_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

async def main():
    asyncio.create_task(web_server())
    print("Бот успешно запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())