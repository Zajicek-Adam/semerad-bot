import discord
import os
import random
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '?', intents = intents, help_command=None)

messages = ('Vážení rodiče, vážení žáci, zdechněte na rakovinu slinivky', 'Semeradím ti, aby ses nezdráhal zasebevraždit', 'Moje škola za moc nestojí, i tak je tvoje máma levnější.','Okusili jste lahodného cementu ze školního cumomatu?','Po téhle škole nebudeš úplně semerád.')

#newsletterId = 927191411739213864
newsletterId = 821505298463981608

@client.event
async def on_ready():
    print('Semerád jde semeradit!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Semeráding through life ?help"))
@client.event
async def on_member_join(member):
    channel = client.get_channel(newsletterId)
    await channel.send(f"Vážení rodiče, vážení žáci, uvítejte mezi námi nového žáka '{member}'. Nechť má dobrý prospěch a je tu celkově semerád.")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(newsletterId)
    await channel.send(f"Všude dobře, na Bojišti nejlépe, '{member}' už není Semerád.")

@client.command()
async def mail(ctx, user:discord.Member, *, message=None):
    i = random.randint(0, 4)
    messageToSend = messages[i] # Do not confuse message with messageToSend, messageToSend is created by me
    message = messageToSend
    embed = discord.Embed(title=message)
    await user.send(embed=embed)

@client.command()
async def help(ctx):
    await ctx.send('```list všech příkazů \n ')

client.run(os.getenv('TOKEN'));
