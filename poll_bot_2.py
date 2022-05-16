import discord 
from discord.ext import commands

client = commands.Bot(command_prefix = "%")

@client.event 
async def on_ready():
  print("Poll Bot is online.")


@client.command()
async def poll(ctx,*,message):
  emb=discord.Embed(title="Poll ", description=f"{message}")
  if message.strip() == "":
    print("You need to write something you bozo")
  else:
      
    msg=await ctx.channel.send(embed=emb)
    await ctx.send("Thumbs up for yes, thumbs down for no.")
    await ctx.send("@here")


client.run("")
#Input the bot client ID in the client.run section
