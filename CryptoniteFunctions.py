import requests
import discord

def MessageHandler(messageContent,messageAuthor):
    print(messageAuthor)
    messageContent = messageContent.lower()
    splitContentArray = messageContent.split(" ")
    if len(splitContentArray) >= 3:
        function = (splitContentArray[1])
        argument= (splitContentArray[2])
        author = str(messageAuthor)
        return FunctionHandler(function,argument,author)
    
    else:
        return SendError("Invalid input, the format of the command should be: [ <Prefix> Function Argument ]")
    #
def FunctionHandler(function,argument,author):
    if function == "get":   
        return GetCoinEUR(argument)
    if function == "exit" and author == "Laurens#4279":
        return ShutDownBot()

def GetCoinEUR(coinToken):
    coinImg = "https://www.cryptocompare.com"
    requestedCoinData = requests.get("https://api.cryptonator.com/api/ticker/"+ coinToken + "-eur")
    requestedCoinJson = requestedCoinData.json()
    requestedCoinImg  = requests.get("https://www.cryptocompare.com/api/data/coinlist/")
    requestedImgJson  = requestedCoinImg.json()
    
    if requestedCoinJson["success"] == False:
        return CreateEmbed(Title="The coin you've requested has not been found.")

    else:
        coinPrice = requestedCoinJson["ticker"]["price"]
        coinPrice = coinPrice[:-6]
        coinImg   = coinImg + requestedImgJson["Data"][coinToken.upper()]["ImageUrl"]
        return CreateEmbed("Coin price", Description=coinPrice, Colour= discord.Color.dark_green(),Thumbnailimg=coinImg)


def CreateEmbed(Title = "",Style ="rich",Description="",Colour= discord.Color.dark_red(),Thumbnailimg=""):
    
    embed = discord.Embed(title=Title,style=Style,description=Description,colour=Colour)
    embed.set_thumbnail(url=Thumbnailimg)
    return embed


def ShutDownBot():
    print ("returning EXIT")
    return "exit"

def SendError(errorMessage):
    ##send to JSON file for evaluation of most made errors
    
    return errorMessage
