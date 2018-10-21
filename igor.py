from discord.ext.commands import Bot
import os, sys, mim
import discord, asyncio
import random, time

bot = Bot(command_prefix="ii")
client = discord.Client()
bot.remove_command("help")

fed = 50
drunk = 50
slep = 100

# I want to die

obwaga = discord.Object(id='503295426359853056')

@bot.event
async def on_ready():
    global voice
    print('Игорь заселился.')
    await check()

@bot.command(pass_context=True)
async def help(ctx):
    await bot.say('iifeed - Покормить\niidrink - Побухать\niisleep - Поспать\niistat - Статы')

@bot.command(pass_context=True)
async def feed(ctx):
    global fed, drunk, slep
    if fed <= 95:
        fed+=5
        await bot.say('Спасибо, пожрал.')
    else:
        await bot.say('Не хочу хавать.')

@bot.command(pass_context=True)
async def drink(ctx):
    global fed, drunk, slep
    if drunk <= 95:
        drunk+=5
        await bot.say('Спасибо, побухал.')
    else:
        await bot.say('БлЯ нЕ нАдО бОлЬШе')

    if drunk>50:
        if random.randint(0,4) == 2:
            await asyncio.sleep(5)
            await bot.say(mim.q[int(random.randint(0,len(mim.q)-1))])

@bot.command(pass_context=True)
async def sleep(ctx):
    global fed, drunk, slep
    if slep <= 95:
        slep+=5
        await bot.say('Спац.')
    else:
        await bot.say('Я бодр и готов бухать.')

@bot.command(pass_context=True)
async def stat(ctx):
    global fed, drunk, slep
    await bot.say('Голод - '+str(fed)+'%\nБухлометр - '+str(drunk)+'%\nЭнергия - '+str(slep)+'%')

@bot.command(pass_context=True)
async def okno(ctx):
    await bot.say('https://cdn.discordapp.com/attachments/502943649437319168/502947081309388811/Kommuna_Kult_43_01.jpg')

async def check():
    global fed, drunk, slep
    fed=abs(fed-2)
    drunk=abs(drunk-5)
    slep=abs(slep-2)
    if fed < 25:
        await bot.send_message(obwaga,'Хочу кушац.')
    if drunk < 25:
        await bot.send_message(obwaga,'Хочу бухатц.')
    if slep < 25:
        await bot.send_message(obwaga,'Хочу спатц')
    if fed < 20 and drunk < 20 and slep < 20:
        await asyncio.sleep(600)
    else:
        await asyncio.sleep(60)
    await check()

bot.run(os.environ.get('TTK', None)) #commit die u stupid fuk >:(
