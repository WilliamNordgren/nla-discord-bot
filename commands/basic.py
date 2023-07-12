from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Homo command lol
    @commands.command(pass_context=True)
    async def homo(self, ctx):
        await ctx.send(f"oot homo { ctx.message.author }")
        await ctx.message.delete()

    # Flip the table
    @commands.command(pass_context=True)
    async def tableflip(self, ctx):
        await ctx.send("(╯°□°)╯︵ ┻━┻")

    # Despacito
    @commands.command(pass_context=True)
    async def despacito(self, ctx):
        await ctx.send("despacito")

    # Clear the chat
    @commands.command(pass_context=True)
    async def clear(self, ctx, num):
        await ctx.send('Clearing messages...')
        await ctx.channel.purge(limit=int(num)+2)


# Setup cog for main.py.
def setup(client):
    client.add_cog(Basic(client))
