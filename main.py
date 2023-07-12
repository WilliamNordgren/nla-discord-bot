from discord.ext import commands
from manager import unitils, bot


dev = False
if dev:
    token = "*"
else:
    token = "*"


client = commands.Bot(command_prefix='!')

client.load_extension("commands.basic")
client.load_extension("commands.level")
client.load_extension("commands.music")
client.load_extension("commands.tracker")
client.load_extension("events.tracker")


@client.event
async def on_ready():
    guild_count = 0

    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1

    if dev:
        print("DevHuora is in " + str(guild_count) + " guilds.")
    else:
        print("botHuora is in " + str(guild_count) + " guilds.")


@client.event
async def on_message(message):
    await client.process_commands(message)

    sender_id = message.author.id
    sender_name = message.author.name
    msg = message.content.lower()
    channel = message.channel

    # Checking if message is nettix url, if so then direct to nettimauto.
    if str(channel).lower() != "nettimauto":
        if unitils.isNettiauto(msg):
            await message.delete()
            channel = client.get_channel(788403517231595571)
            await bot.sendMsg(message, channel, msg)

    # Checking if message is code, if so then direct to nörttiluola.
    if str(channel).lower() != "nörttiluola":
        if unitils.isCode(msg):
            await message.delete()
            channel = client.get_channel(755053446763380767)
            await bot.sendMsg(message, channel, msg)

client.run(token)

