import discord
from discord.ext import commands
import platform
 
bot=commands.Bot(command_prefix="Z")
invitelink="https://discord.com/api/oauth2/authorize?client_id=789562515268042772&permissions=8&scope=bot"
welcomechannel=789560577512570920
leavechannel=789020543214551073
 
async def owner(ctx):
    return ctx.author.id==your discord id
    
@bot.event
async def on_ready():
    print("Bot is running!")
    game=discord.Game("Ｚｏｎａ異世界 | Prefix : Z")
    await bot.change_presence(status=discord.Status.online,activity=game)
    
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if(message.author==bot.user):
        return
    elif(bot.user.mentioned_in(message)):
        await message.channel.send("Prefix is Z")
 
@bot.event
async def on_member_join(member):
    channel=discord.utils.get(member.guild.text_channels,id=welcomechannel)
    server=member.guild
    await channel.send(f"{member.name} just joined {server.name}")
    
@bot.event
async def on_member_remove(member):
    channel=discord.utils.get(member.guild.text_channels,id=leavechannel)
    server=member.guild
    await channel.send(f"{member.name} just left {server.name}")
    
@bot.command()
async def question(ctx):
    await ctx.send("For more info pls dm my lord <@655235246404403213>")
    
@bot.command()
async def ping(ctx):
    pingtime=bot.latency
    await ctx.send(f"Ping is {pingtime}")
 
@bot.command()
async def add(ctx,a:int,b:int):
    await ctx.send(a+b)
    
@bot.command()
async def sub(ctx,a:int,b:int):
    await ctx.send(a-b)
    
@bot.command()
async def multiply(ctx,a:int,b:int):
    await ctx.send(a*b)
    
@bot.command()
async def divide(ctx,a:int,b:int):
    await ctx.send(a/b)
        
@bot.command()
async def info(ctx,user:discord.User=None):
    if(user):
        name=f"{user.name}"
        id=f"{user.id}"
        e=discord.Embed(color=0x000000)
        e.add_field(name="Name",value=name)
        e.add_field(name="Id",value=id)
        e.set_footer(text="Made by DansTzy#0909")
        await ctx.send(embed=e)
    
@bot.command()
async def binfo(ctx):
    pyv=platform.python_version()
    botos=platform.system()
    discordv=discord.__version__
    e=discord.Embed(color=0x000000)
    e.add_field(name="Python version",value=pyv)
    e.add_field(name="OS",value=botos)
    e.add_field(name="Discord version",value=discordv)
    e.set_footer(text="Made by DansTzy#0909")
    await ctx.send(embed=e)
    
@bot.command()
async def invite(ctx):
    await ctx.send(invitelink)
 
@bot.command()
@commands.check(owner)
async def kick(ctx,user:discord.Member=None):
    if(user):
        await ctx.send(f"{user.name} was kicked!")
        await user.kick()
        
@bot.command()
@commands.check(owner)
async def ban(ctx,user:discord.Member=None):
    if(user):
        await ctx.send(f"{user.name} was banned!")
        await user.ban()
 
@bot.command()
@commands.check(owner)
async def nick(ctx,member:discord.Member,*,name):
    await member.edit(nick=name)
    await ctx.send(f"Renamed {member} to {name}")
    
@bot.command()
async def avatar(ctx,member:discord.Member):
    await ctx.send(member.avatar_url)
    
bot.remove_command("help")
@bot.command()
async def help(ctx):
    e=discord.Embed(color=0x000000)
    e.add_field(name="🏓 Fun commands 🏓",value="- `Zping (Shows bot latency)`")
    e.add_field(name="📃 Math commands 📃",value="- `Zadd {1} {2}`, - `Zsub {1} {2}`, - `Zmultiply {1} {2}`, - `Zdivide {1} {2}`")
    e.add_field(name="🔎 Info commands 🔎",value="- `Zinvite`, - `Zinfo`, - `Zbinfo`, - `Znick`, - `Zavatar`")
    e.add_field(name="🛠 Administrator commands 🛠",value="- `Zkick {@mention}`, - `Zban {@mention}`")
    e.add_field(name="🗺 Special commands 🗺",value="- `Zquestion`")
    e.set_footer(text="🛠 Made by DansTzy#0909 🛠")
    await ctx.send(embed=e)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
bot.run("you bot token")
