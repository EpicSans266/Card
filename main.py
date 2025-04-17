import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Бот {bot.user} успешно запущен!")

@bot.command()
async def card(ctx):
    card_text = """
    **👤 Визитка**
    - Фамилия: Канатов
    - Имя: Бауыржан
    - Возраст: 19 лет
    - Номер: 8 707 246 1531
"""
    await ctx.send(card_text)

@bot.command()
async def skills(ctx):
    myskills = """
    **Мои навыки**
    HTML, CSS, JS, Python
"""
    await ctx.send(myskills)

# Запуск бота
bot.run(TOKEN)

