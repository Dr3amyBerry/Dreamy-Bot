"""
BOT de discord hecho por Dr3amyB3rry.
Super ejemplo y super mega sencillo con funciones basicas.
Eres libre de modificar lo que te de la gana de igual manera siempre la gente roba codigo.
Espero que te ayude a aprender.
10/10/22
"""

import re
import os
import pytube
import requests
import aiohttp
import urllib
import discord
import json
import pyshorteners
from discord.ext import commands
from requests import get
from googlesearch import search
from datetime import datetime, timezone, timedelta
from urllib import parse, request
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='PREFIX AQUI', intents=intents)
bot.remove_command("help")
TOKEN = 'TOKEN AQUI'

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Mmmm.. Creo que lo haz escrito mal.", delete_after=5.0)
        await ctx.message.delete(delay=5)
        print(
            f"\nMal escrito\n{datetime.now(timezone(timedelta(hours=+3))).time()}")
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Mmmmmm aun no se hacer eso.", delete_after=5.0)
        await ctx.message.delete(delay=5)
        print(
            f"\nComando no encontrado\n{datetime.now(timezone(timedelta(hours=+3))).time()}")
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Esperate hermano aun faltan {error.retry_after:0.1f} segundos.", delete_after=5.0)
        await ctx.message.delete(delay=5)
        print(
            f"\nCooldown\n{datetime.now(timezone(timedelta(hours=+3))).time()}")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("No tienes permisos para eso mi amigo querido", delete_after=5.0)
        await ctx.message.delete(delay=5)
        print(
            f"\nNo tenia permisos\n{datetime.now(timezone(timedelta(hours=+3))).time()} ")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="> ayuda 😉"))
    print(
        f"\nBot online.\n{datetime.now(timezone(timedelta(hours=+3))).time()}")

def checkYoutube(url, lengthYoutube):
    if pytube.YouTube(url).length > lengthYoutube:
        return False
    else:
        return True


def downloadYoutube(url):
    pytube.YouTube(url).streams.get_by_itag(
        18).download(filename="savevideo.mp4")


@bot.command()
@commands.cooldown(1, 15, commands.BucketType.default)
async def video(ctx, url):
    async with ctx.typing():
        if "youtu" in url:
            try:
                if checkYoutube(url, 60):
                    downloadYoutube(url)
                    await ctx.send(content=f"Video enviado por {ctx.message.author.mention}", file=discord.File(fp="savevideo.mp4"))
                    await ctx.message.delete()
                    os.remove("savevideo.mp4")
                    print(
                        f"\nVideo enviado por {ctx.message.author.mention}\n{url}\n{datetime.now(timezone(timedelta(hours=+3))).time()}")
                else:
                    await ctx.send("Tu video es muy largo\\Razon del error :\nhttps://github.com/discord/discord-api-docs/issues/2037", delete_after=5.0)
                    await ctx.message.delete(delay=5)
                    print(
                        f"\nError 60.\n{url}\n{datetime.now(timezone(timedelta(hours=+3))).time()}")
            except BaseException:
                await ctx.send("Hubo un error, Notifica al staff")
                print(
                    f"\nError.\n{url}\n{datetime.now(timezone(timedelta(hours=+3))).time()}")
                os.remove("savevideo.mp4")
        else:
            await ctx.send("Plataforma no soportada ", delete_after=5.0)
            await ctx.message.delete(delay=5)
            print(
                f"\nError Plataforma.\n{url}\n{datetime.now(timezone(timedelta(hours=+3))).time()}")


@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(
        title="Dr3amy Bot",
        description="Estoy en Desarrollo suplico paciencia :D.\nPrefix = (>)",
        colour=discord.Color.blurple())
    embed.add_field(
        name='**> ayuda**',
        value="Manda esta Sensual Ayuda.",
        inline=False)
    embed.add_field(
        name='**> info**',
        value="Muestra Sensual Información.",
        inline=False)
    embed.add_field(
        name='**> video <Link>**',
        value="Descarga Videos De YTshorts\n(Por ahora Solo 60 secs).",
        inline=False)
    embed.add_field(
        name='**> buscar <Tu Búsqueda>**',
        value="Busca lo que sea usando Google.",
        inline=False)
    embed.add_field(
        name='**> acortar <Link>**',
        value="Acorta una Url.",
        inline=False)
    embed.add_field(
        name='**> saluda**',
        value="Te doy un Saludo <3.",
        inline=False)
    embed.add_field(
        name="**> comandosAdmins**",
        value="Commandos para admins.",
        inline=False)
    embed.add_field(name='TikTok', value='No disponible aun')
    embed.add_field(name='Dios Todo Poderoso:', value='Dr3amy')
    embed.add_field(name="Invitacion :", value='https://clck.ru/33AXmw')
    embed.set_thumbnail(url="https://i.hizliresim.com/68ya3cf.jpg")
    print(f"\nhelp\n{datetime.now(timezone(timedelta(hours=+3))).time()}")
    await ctx.send(embed=embed)
    await ctx.message.delete()

@bot.command()
@commands.has_permissions(administrator=True)
async def comandosAdmins(ctx):
    embed = discord.Embed(
        title="Dr3amy Bot",
        description="Comandos para Admins.\nBot aun en Desarrollo :3.\nPrefix = (>)",
        colour=discord.Color.blurple())
    embed.add_field(
        name="**> ban**",
        value="Banea a un usuario.",
        inline=False)
    embed.add_field(
        name="**> unban**",
        value="Desbanea a un usuario.",
        inline=False)
    embed.add_field(
        name="**> repite**",
        value="El bot repite lo que tu digas.",
        inline=False)
    embed.add_field(name='TikTok', value='No disponible aun')
    embed.add_field(name='Dios Todo Poderoso:', value='Dr3amy')
    embed.add_field(name="Invitacion :", value='https://clck.ru/33AXmw')
    embed.set_thumbnail(url="https://i.hizliresim.com/68ya3cf.jpg")
    print(f"\nadmin-help\n{datetime.now(timezone(timedelta(hours=+3))).time()}")
    await ctx.send(embed=embed)
    await ctx.message.delete()


@bot.command()
async def saluda(ctx):
    embed = discord.Embed(
        title="Holaaa Soy un Nuevo bot en Desarrollo!",
        description="Por ahora, Solo puedo descargar Videos de Youtube Shorts\nEstoy Escrito en Python <3🐍\nMi Creador @Dr3amyBerry",
        colour=discord.Color.blurple())
    await ctx.send(embed=embed)
    print(
        f"\nLe di un saludo a alguien\n{datetime.now(timezone(timedelta(hours=+3))).time()}")


@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title=f"Nombre Del Servidor: **{ctx.guild.name}**",
        description="Informacion del Servidor",
        colour=discord.Color.blurple())
    embed.add_field(name="Fecha de Creacion", value=f"{ctx.guild.created_at}", inline=False)
    embed.add_field(name="Bot Owners", value=f"Dreamy-Srglowstone", inline=False)
    embed.add_field(name="ID Servidor", value=f"{ctx.guild.id}", inline=False)
    embed.add_field(name="Ping:", value=f"{round(bot.latency * 1000)}ms", inline=False)
    embed.add_field(name="Servidores:", value=f"{len(bot.guilds)}", inline=False)
    embed.set_thumbnail(url="https://i.hizliresim.com/jfx5fda.png")
    await ctx.send(embed=embed)
    await ctx.message.delete()


@bot.command(pass_context=True)
async def acortar(ctx, link):
    s = pyshorteners.Shortener()
    x = s.clckru.short(link)
    async with ctx.typing():
        await ctx.send(f"\n:point_right: {x}")
        await ctx.message.delete()


@bot.command()
async def buscar(ctx, *, query):
    autor = ctx.author.mention
    await ctx.channel.send(f"Buscando...{autor}")
    async with ctx.typing():
        for j in search(query, tld="co.in", num=2, stop=2, pause=2):
            await ctx.send(f"\n:point_right: {j}")
        await ctx.message.delete()


@bot.command()
@commands.has_permissions(administrator=True)
async def repite(ctx, *, arg):
    await ctx.send(arg)
    await ctx.message.delete()

@bot.command()
@commands.is_owner()
async def nuke(ctx, channel: discord.TextChannel = None):

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="https://imgur.com/LIyGeCR")
        await nuke_channel.delete()
        await new_channel.send("https://imgur.com/LIyGeCR")
        await ctx.send("Listo :)")

    else:
        await ctx.send(f"No encontre ese canal.!")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, user: discord.User):
    guild = ctx.guild
    embed = discord.Embed(
        title= "Hecho.",
        description= f"{user} Ya lo bote del server!."
    )
    await ctx.send(embed=embed)
    await guild.ban(user=user)


@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user: discord.User):
    embed = discord.Embed(
        title= "Hecho.",
        description= f"{user} Desbaneado!."
    )
    await ctx.send(embed=embed)
    await ctx.guild.unban(user=user)

bot.run(TOKEN)
