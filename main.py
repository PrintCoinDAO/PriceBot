import discord, config, requests, time

def getPrice():
    r = requests.get("https://api.traderjoexyz.com/priceusd/0xf4625148efa2d3e160399b3ffb22230c9a4544ed")
    return '$' + str(round(int(r.text) * 0.1 ** 18, 2))

bot = discord.Client()

@bot.event
async def on_ready():
    print('logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game(name=getPrice()))

if __name__ == '__main__':
    bot.run(config.discord)
    while True:
        time.sleep(60)
        bot.dispatch("on_ready")
