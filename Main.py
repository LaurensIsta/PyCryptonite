import discord
import asyncio
import os
from CryptoniteFunctions import MessageHandler
print("Creating bot client...")
client = discord.Client()
print("Creation completed.")


@client.event
async def on_ready():
    
    print("Bot name: " + client.user.name + "\n Bot ID: " + client.user.id)
    print("Ready to receive commands!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    
    #prefix determined here ($$)
    elif message.content.startswith("$$"):
        returnValue = MessageHandler(message.content,message.author)
        if returnValue == "exit":
            exit()
            await client.send_message(message.channel, "Bot shutting down.")
            

        else:
            await client.send_message(message.channel, embed=returnValue)

client.run("NDE0NzIyMjk1MzMyODY0MDA4.DeMfSw.FgPjlC741zffo7QZrvLD9CiwypI")
