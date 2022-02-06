
import discord
import random
import codecs


TOKEN= "NDY4OTMwODY5MTU1ODU2NDA0.W06D5w.OcgCFSRQn6NphLJ8U-cPLCUSQz8"

client = discord.Client()

@client.event

async def on_ready():
    print("Giriş yapıldı{0.user}".format(client),encoding="utf-8")


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str (message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if user_message.startswith("nabıyon"):
        await message.channel.send(f"ii sen nabiyon {username}!")
        return
    else:
        user_message = (user_message.lower()).split()
        for i in user_message:
            if i.startswith("allah"):
                await message.channel.send(f"{username} buranın allahı @Trigo#7451 !")
                return






client.run(TOKEN)