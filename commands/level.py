from discord.ext import commands
import discord

from manager import unitils
from manager.user import User


class Level(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Leveling command.
    @commands.command(pass_context=True)
    async def level(self, ctx):

        user = User(ctx.message.author)

        lvl = user.getLevel()
        xp = user.getXP()
        max = user.getMaxXP()

        embed = discord.Embed(title=f"Progression", description=f"{ctx.message.author.display_name}", color=0x00ff00)
        
        embed.add_field(name=f"Level {lvl}", value=f"{xp}/{max} XP", inline=False)
        embed.add_field(name="Total time", value=f"{unitils.convertSeconds(user.getTime())}", inline=False)
        
        if user.getCurrentMillis() != 0:
            time = user.getCurrentCallTimeFormatted()
            embed.add_field(name="Current call duration", value=f"{time}", inline=False)
        
        await ctx.send(embed=embed)


# Setup cog for main.py.
def setup(client):
    client.add_cog(Level(client))
