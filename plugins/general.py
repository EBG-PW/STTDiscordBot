from discord.ext import commands
from discord.utils import get
import asyncio
import time

from main import Tokens

TOKEN = Tokens.TOKEN
GUILD = Tokens.GUILD
my_region = Tokens.LOL_REGION


def __init__(self, bot):
    self.bot = bot


def setup(bot):
    bot.add_command(list)
    bot.add_command(generaterules)
    bot.add_command(generatelanes)
    bot.add_command(generatemain)
    bot.add_command(generateclash)
    bot.add_command(listemojis)


@commands.command(name='list', hidden=True)
@commands.dm_only()
async def list(ctx):
    for guild in ctx.bot.guilds:
        if guild.id == Tokens.GUILD:
            break

    user = ctx.message.author

    for member in guild.members:
        for role in member.roles:
            if role.name == "Schildkröte":
                await ctx.send(member.nick + " " + "`" + str(member.id) + "`")


@commands.command(name='generaterules', hidden=True)
@commands.has_role('Social Media Manager')
async def generaterules(ctx):
    pool = ctx.bot.pool

    message = await ctx.send("FUCKING LANGER RULES TEXT BLA BLA BLA \n"
                             "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, \n"
                             "sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, \n"
                             "sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. \n"
                             "Stet clita kasd gubergren,\n"
                             "Zu Risiken und Nebenwirkungen lesen Sie die Packungsbeilage und fragen Sie Ihren Gott "
                             "oder Geo\n "
                             "Mit der Reaktion auf die Nachricht treten sie sämtliche Rechte ihres Lebens ab.")
    await message.add_reaction('✅')

    await asyncio.sleep(2)

    async with pool.acquire() as conn:
        await conn.execute('INSERT INTO reactions VALUES ($1, $2)', message.id, "RULES")
    print("test")


@commands.command(name='generatelanes', hidden=True)
@commands.has_role('Social Media Manager')
async def generatelanes(ctx):
    pool = ctx.bot.pool

    message = await ctx.send('Reagiere bitte auf diese Nachricht welche Lanes du in League spielst.')
    await message.add_reaction('<:TopLane:777326001964974080>')
    await message.add_reaction('<:Jungle:777326001965105162>')
    await message.add_reaction('<:MidLane:777326001902059561>')
    await message.add_reaction('<:BotLane:777326001877286922>')
    await message.add_reaction('<:Support:777326002061180928>')

    await asyncio.sleep(2)

    async with pool.acquire() as conn:
        await conn.execute('INSERT INTO reactions VALUES ($1, $2)', message.id, "LANES")


@commands.command(name='generatemain', hidden=True)
@commands.has_role('Social Media Manager')
async def generatemain(ctx):
    pool = ctx.bot.pool

    message = await ctx.send('Reagiere bitte auf diese Nachricht welche Lane du primär Spielst.')
    await message.add_reaction('<:TopLane:777326001964974080>')
    await message.add_reaction('<:Jungle:777326001965105162>')
    await message.add_reaction('<:MidLane:777326001902059561>')
    await message.add_reaction('<:BotLane:777326001877286922>')
    await message.add_reaction('<:Support:777326002061180928>')

    await asyncio.sleep(2)

    async with pool.acquire() as conn:
        await conn.execute('INSERT INTO reactions VALUES ($1, $2)', message.id, "MAINLANE")


@commands.command(name='generateclash', hidden=True)
@commands.has_role('Social Media Manager')
async def generateclash(ctx):
    pool = ctx.bot.pool
    message = await ctx.send('Reagiere bitte auf diese Nachricht wenn du bei Organisierten Clash Events teilnehmen '
                             'möchtest. \n**Wichtig du musst dazu bereits einen verknüpften und auch verifzierten '
                             'League Account haben!**')
    await message.add_reaction('<:clash:783486810760282193>')

    await asyncio.sleep(2)

    async with pool.acquire() as conn:
        await conn.execute('INSERT INTO reactions VALUES ($1, $2)', message.id, "ROLES")


@commands.command(name='listemojis', hidden=True)
@commands.has_role('Social Media Manager')
async def listemojis(ctx):
    for emoji in ctx.guild.emojis:
        await ctx.send(emoji.name + " " + str(emoji.id))
        await ctx.send(emoji)
    return
