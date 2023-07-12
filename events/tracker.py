import discord
from discord.ext import commands

from manager import unitils
from manager.user import User


class Tracker(commands.Cog):
    def __init__(self, client):
        self.client = client

    # on voice channel connect/disconnect/mute/deafen event.
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        # Check if user is connecting or disconnecting from voice channel.
        # User is connecting to the voice channel.
        if before.channel is None and after.channel is not None:
            for channel in self.client.get_all_channels():
                user = User(member)
                user.startTime()

        # If user is disconnecting from the voice channel.
        if before.channel is not None and after.channel is None:
            user = User(member)
            user.stopTime()

            seconds = user.getStoppedTime()
            earned = int(seconds/1000/60)
            
            lvl = user.getLevel()
            xp = user.getXP()
            max = user.getMaxXP()

            for channel in self.client.get_all_channels():
                if str(channel.type) == "text" and channel.name.lower() == 'progression':
                    embed = discord.Embed(title=f"Progression update", description=f"{member.display_name}", color=0x00ff00)
                    embed.add_field(name="Call duration", value=f"{unitils.convertSeconds(seconds)}", inline=True)
                    embed.add_field(name="Earned XP", value=f"{earned} XP", inline=True)
                    embed.add_field(name="Total time", value=f"{unitils.convertSeconds(user.getTime())}", inline=True)
                    embed.add_field(name="Progression", value=f"Level: {lvl}\nExperiences: {xp}/{max}", inline=False)
                    await channel.send(embed=embed)


# Setup cog for main.py.
def setup(client):
    client.add_cog(Tracker(client))
