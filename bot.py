import discord
from dotenv import load_dotenv
from os import getenv
import time
startDT = time.ctime().replace(':', ';') #start datetime
load_dotenv()
TOKEN = getenv("DISCORD_TOKEN")
GUILD = getenv("DISCORD_GUILD")
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
firstConn = True
logQueue = []
file = open(f"data/logs/{startDT}.txt", 'w')
file.close()

def log(*args, save=False):
    global logQueue
    logMessage = f"[{time.ctime()}] {''.join(str(arg) for arg in args)}"
    print(logMessage)
    logQueue.append(logMessage)
    if len(logQueue) > 5 or save == True:
        file = open(f"data/logs/{startDT}.txt", 'a')
        file.write(''.join(logMsg+'\n' for logMsg in logQueue))
        logQueue = []
        file.close()

log("Starting techoholic's Blood Moon Bot v0.1...")

@client.event
async def on_ready():
    global firstConn
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    log(client.user, " is connected to the following guild: ", guild.name, " (id: ", guild.id, ')')
    if firstConn:
        log("Guild members:")
        for member in guild.members:
            log('~', member, " // ", member.id)
        firstConn = False
    log('')

@client.event
async def on_member_join(member):
    log(member, " joined ", guild.name, '!')

@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return
    await message.channel.send("Pleasant sunrise, Earth being.")
    if message.content == ";stop":
        await client.logout()

client.run(TOKEN)
log("Logged out of Discord. Goodbye!", save=True)
