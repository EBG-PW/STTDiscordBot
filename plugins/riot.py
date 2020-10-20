from discord.ext import commands
from asyncpg.pool import Pool
import re

from main import Tokens, watcher

from pyot.models import lol
from pyot.utils import loop_run
from pyot.core import Gatherer

TOKEN = Tokens.TOKEN
GUILD = Tokens.GUILD
my_region = Tokens.LOL_REGION


def __init__(self, bot):
    self.bot = bot


def setup(bot):
    bot.add_command(matchcount)
    bot.add_command(mc)


@commands.command()
async def matchcount(ctx, summonername):
    gameIds = []
    partId: int
    goldSum: int = 0
    kills: int = 0
    deaths: int = 0
    summoner = watcher.summoner.by_name(my_region, summonername)
    matchlist = watcher.match.matchlist_by_account(my_region, summoner['accountId'])
    for match in matchlist['matches']:
        gameIds.append(match['gameId'])

    for match in gameIds:
        gameData = watcher.match.by_id(my_region, match)
        for participant in gameData['participantIdentities']:
            if summonername == participant['player']['summonerName']:
                partId = int(participant['participantId'])
        goldSum += int(gameData['participants'][partId - 1]['stats']['goldEarned'])
        kills += int(gameData['participants'][partId - 1]['stats']['kills'])
        deaths += int(gameData['participants'][partId - 1]['stats']['deaths'])
    await ctx.send("Gold Earned: " + goldSum + "\n"
                   "Total Kills: " + kills + "\n"
                   "Total Deaths: " + deaths + "\n")


@commands.command()
async def mc(ctx, summonername):
    summoner = await lol.Summoner(name=summonername, platform="EUW1").get()
    matchlist = await lol.MatchHistory(summoner.account_id).get()
    for match in matchlist.matches:
        responses = match.role
    for r in responses:
        await ctx.send(r)
