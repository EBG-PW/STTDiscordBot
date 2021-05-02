import asyncio

from discord.ext import commands

from main import Tokens

TOKEN = Tokens.TOKEN
GUILD = Tokens.GUILD
my_region = Tokens.LOL_REGION


class GeneralCog(commands.Cog, name='Admin'):
    """Admin Stuff"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='list', hidden=True)
    @commands.dm_only()
    @commands.is_owner()
    async def listmembers(self, ctx):
        guild = ""
        for guild in ctx.bot.guilds:
            if guild.id == Tokens.GUILD:
                break

        for member in guild.members:
            for role in member.roles:
                if role.name == "Schildkröte":
                    await ctx.send(member.nick + " " + "`" + str(member.id) + "`")

    @commands.command(name='generaterules', hidden=True)
    @commands.has_role('Social Media Manager')
    async def generaterules(self, ctx):
        pool = ctx.bot.pool

        message = await ctx.send("**REGELN**\n\n"
                                 "DEUTSCHSPRACHIGER SERVER / GERMAN SPEAKING SERVER\n"
                                 "1. Einhaltung der Netiquette \n"
                                 "2. Kanalbeschreibungen lesen! Topics nur in die dafür vorgesehenen Kanäle \n"
                                 "3. Streaming ist, zum Schutz der Privatsphäre unserer Mitglieder, nur im dafür vorgesehenen Bereich erlaubt.\n"
                                 "4. Das einladen von Freunden oder Bekannten ist jeder Schildkröte erlaubt.\n"
                                 "5. Um Schildkröte zu werden, und Zugriff auf den Server zu erhalten reagiere bitte auf diese Regeln.\n\n"
                                 "Anschließend kannst du mit unserem Bot <@757955495251279954> deine Name auf dem Server ändern, Rollen erhalten und "
                                 "deinen League of Legends Account verknüpfen.\n ")
        await message.add_reaction('✅')

        await asyncio.sleep(2)

        async with pool.acquire() as conn:
            await conn.execute('INSERT INTO reactions VALUES ($1, $2)', message.id, "RULES")
        print("test")

    @commands.command(name='generatelanes', hidden=True)
    @commands.has_role('Social Media Manager')
    async def generatelanes(self, ctx):
        pool = ctx.bot.pool

        message = await ctx.send('Reagiere bitte auf diese Nachricht welche Lanes du in League spielst.')
        await message.add_reaction('<:TopLane:748296960586416168>')
        await message.add_reaction('<:Jungle:748296968295677993>')
        await message.add_reaction('<:MidLane:748296979322241145>')
        await message.add_reaction('<:BotLane:807773264184737814>')
        await message.add_reaction('<:Support:748296949689483385>')

        await asyncio.sleep(2)

        async with pool.acquire() as conn:
            await conn.execute('INSERT INTO reactions VALUES ($1, $2)', message.id, "LANES")

    @commands.command(name='generatemain', hidden=True)
    @commands.has_role('Social Media Manager')
    async def generatemain(self, ctx):
        pool = ctx.bot.pool

        message = await ctx.send('Reagiere bitte auf diese Nachricht welche Lane du primär Spielst.')
        await message.add_reaction('<:TopLane:748296960586416168>')
        await message.add_reaction('<:Jungle:748296968295677993>')
        await message.add_reaction('<:MidLane:748296979322241145>')
        await message.add_reaction('<:BotLane:807773264184737814>')
        await message.add_reaction('<:Support:748296949689483385>')

        await asyncio.sleep(2)

        async with pool.acquire() as conn:
            await conn.execute('INSERT INTO reactions VALUES ($1, $2)', message.id, "MAINLANE")

    @commands.command(name='generateclash', hidden=True)
    @commands.has_role('Social Media Manager')
    async def generateclash(self, ctx):
        pool = ctx.bot.pool
        message = await ctx.send('Reagiere bitte auf diese Nachricht wenn du bei Organisierten Clash Events teilnehmen '
                                 'möchtest. \n**Wichtig du musst dazu bereits einen verknüpften und auch verifzierten '
                                 'League Account haben!**')
        await message.add_reaction('<:clash:807773305440436245>')

        await asyncio.sleep(2)

        async with pool.acquire() as conn:
            await conn.execute('INSERT INTO reactions VALUES ($1, $2)', message.id, "ROLES")

    @commands.command(name='generateroles')
    @commands.has_role('Social Media Manager')
    async def generateroles(self, ctx):
        """Generiert eine Nachricht für die Rolen """
        pool = ctx.bot.pool

        message = await ctx.send('**ROLLEN**')

        async with pool.acquire() as conn:
            await conn.execute('INSERT INTO reactions VALUES ($1, $2)', message.id, "GAMES")

    @commands.command(name='addrole')
    @commands.has_role('Oberkröte (Mod)')
    async def addrole(self, ctx, *args):
        pool = ctx.bot.pool

        async with pool.acquire() as conn:
            reactionmsg = await conn.fetchrow("SELECT * FROM reactions WHERE type = 'GAMES'")

        message = await ctx.channel.fetch_message(reactionmsg['message_id'])
        await message.add_reaction(args[0])

        await asyncio.sleep(2)

        emojiSTEP1 = args[0]
        emojiSTEP2 = emojiSTEP1.split(':')
        emojiSTEP3 = emojiSTEP2[2].split('>')
        emojiID = int(emojiSTEP3[0])
        print(ctx.message.role_mentions[0].name)
        async with pool.acquire() as conn:
            await conn.execute("INSERT INTO roles VALUES ($1, $2, $3)", ctx.message.raw_role_mentions[0], emojiID, ctx.message.role_mentions[0].name)

    @commands.command(name='listemojis', hidden=True)
    @commands.has_role('Social Media Manager')
    async def listemojis(self, ctx):
        for emoji in ctx.guild.emojis:
            await ctx.send(emoji.name + " " + str(emoji.id))
            await ctx.send(emoji)
        return


def setup(bot):
    bot.add_cog(GeneralCog(bot))