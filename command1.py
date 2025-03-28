import discord
from discord.ext import commands
#esto le da permisos al bot

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def activo():
    print(f'Hemos iniciado sesion con el {bot.user}')

@bot.command
async def repetir(ctx, *, message:str):
    await ctx.send(message)


@bot.command()
async def chatbot(ctx, *, mensaje: str):
    if  "hola" in mensaje:
        await ctx.send("¡Hola! ¿Cómo estás? 😁")
    elif "adios" or "adiós":
        await ctx.send("¡Hasta luego!")

bot.run("")