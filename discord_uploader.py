import discord
import sys
import os

# args: > python script.py (Discord token) (discord channel) (build name)

uploadfile = os.getcwd() + '/dist/' + sys.argv[3] + ".zip"

client = discord.Client()


channelID = int(sys.argv[2])
discordtoken = sys.argv[1]

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print('------')
    
	area=client.get_channel(channelID)
	for filename in sys.argv[3:]:
        await area.send(file=discord.File(uploadfile, filename=f"{filename}.zip"))

	await client.close()



client.run(discordtoken)


