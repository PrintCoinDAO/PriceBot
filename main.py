import discord, config, requests, time, sys

def getPrice():
    # Function to get the current USD/PRINT price from Trader Joe XYZ
    r = requests.get("https://api.traderjoexyz.com/priceusd/0xf4625148efa2d3e160399b3ffb22230c9a4544ed")
    return '$' + str(round(int(r.text) * 0.1 ** 18, 2))

bot = discord.Client()

@bot.event
async def on_ready():
    print('logged in as {0.user}'.format(bot))
    # Set status to price on startup
    await bot.change_presence(activity=discord.Game(name=getPrice()))

@bot.event
async def on_message(message):
    # Update status every time a message is sent
    await bot.change_presence(activity=discord.Game(name=getPrice()))

if __name__ == '__main__':
    try:
        bot.run(config.discord)
    except KeyboardInterrupt:
        print("zoo wee mama")
        sys.exit(0)
