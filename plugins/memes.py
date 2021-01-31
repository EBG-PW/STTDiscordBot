from discord.ext import commands

from main import Tokens

TOKEN = Tokens.TOKEN
GUILD = Tokens.GUILD
my_region = Tokens.LOL_REGION


def __init__(self, bot):
    self.bot = bot


def setup(bot):
    bot.add_command(geo)
    bot.add_command(schmidi)
    bot.add_command(gott)
    bot.add_command(sudo)


@commands.command(name='geo', alias=('geozukunft', 'viktor', 'meister', 'erde'), hidden=True)
async def geo(ctx):
    await ctx.send("AHH DER DEFINTIV BESTE SOCIAL MEDIA MANAGER UND ADC FARM GOTT :innocent: ")


@commands.command(name='schmidi', alias=('schmidi49', 'erik', 'schlechtersupport'), hidden=True)
async def schmidi(ctx):
    await ctx.send("Du hast dich vermutlich verschrieben meintest du nicht `!gott` ?")


@commands.command(name='gott', hidden=True)
async def gott(ctx):
    await ctx.send("Meintest du womöglich `!schmidi`?")


@commands.command(name='sudo', hidden=True)
async def sudo(ctx):
    await ctx.send("Glückwunsch Sie haben soeben den Server gelöscht der Anwaltsbrief kommt dann nächste Woche!")
