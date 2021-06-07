import discord
import sys
import os

# args: > python script.py (Discord token) (discord channel) (build name)

uploadfolder = os.getcwd() + '/dist/'

client = discord.Client()


channelID = int(sys.argv[2])
discordtoken = sys.argv[1]

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print('------')
    
	area=client.get_channel(channelID)
	entries = os.listdir(uploadfolder)
	for entry in entries:
        await area.send(file=discord.File(uploadfolder + entry, filename=f"{entry}.zip"))

	await client.close()



client.run(discordtoken)


