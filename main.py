import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Бот {bot.user} успешно запущен!")

@bot.command()
async def визитка(ctx):
    визитка_текст = """
    **👤 Визитка**
    - Фамилия: Канатов
    - Имя: Бауыржан
    - Возраст: 19 лет
    - Номер: 8 707 246 1531
"""
    await ctx.send(визитка_текст)

# Запуск бота
bot.run(TOKEN)

