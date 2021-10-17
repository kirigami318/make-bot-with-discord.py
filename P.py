import discord
import asyncio
import random
import datetime
import time
import os

from replit import db
from keep_alive import keep_alive
from discord.ext import commands
from discord.utils import get
from random import choice
from discord import File
from datetime import datetime

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)
bot.remove_command('help')

#activity of bot
@bot.event
async def on_ready():
  print('im ready')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=".help | discord.gg/rd4nqNYHBW"),status=discord.Status.dnd)

@bot.event
async def on_member_remove(member):
	guild = bot.get_guild(725523893829369939)
	embed = discord.Embed(
	    title=f'Goodbye {member.name}!',
	    description='Semoga Sehat Selalu :)',
	    colour=member.colour,
	)
	embed.set_image(url=member.avatar_url)
	channel = guild.get_channel(754147700672561192)
	await channel.send(embed=embed)

@bot.event
async def on_member_join(member):
	guild = bot.get_guild(725523893829369939)
	embed = discord.Embed(
	    title=f'Welcome {member.name}!',
	    description=f'Selamat Datang di {member.guild}',
	    colour=member.colour,
	)
	embed.set_image(url=member.avatar_url)
	channel = guild.get_channel(754147700672561192)
	await channel.send(embed=embed)

#command
@bot.command()
async def help(ctx):
	gene = f"help\nwhois(wi)\nserverinfo(si)\navatar(av)\nping"
	embed = discord.Embed(title='Help Command',
	                      description='Prefixnya adalah(.)',
	                      colour=ctx.author.colour)
	embed.add_field(name='genreal', value=''.join(gene))
	embed.set_thumbnail(url=ctx.guild.icon_url)
	await ctx.send(embed=embed)

@bot.command(aliases=['wi'])
async def whois(ctx, member: discord.Member):
	roles = [role for role in member.roles]
	embed = discord.Embed(colour=member.colour,
	                      timestamp=ctx.message.created_at)
	embed.set_author(name=f"Who is {member}?")
	embed.set_image(url=member.avatar_url)
	embed.set_footer(text=f'Requested by {ctx.author}',
	                 icon_url=ctx.message.author.avatar_url)

	embed.add_field(name='Name', value=member.display_name)
	embed.add_field(name='ID', value=member.id, inline=False)

	embed.add_field(
	    name='Created at',
	    value=member.created_at.strftime('%a, %#d, %B %Y, %I:%M %p'),
	    inline=False)
	embed.add_field(
	    name='Joined at',
	    value=member.joined_at.strftime('%a, %#d, %B %Y, %I:%M %p'),
	    inline=False)

	embed.add_field(name=f'Roles ({len(roles)})',
	                value=' '.join([role.mention for role in roles]),
	                inline=False)

	await ctx.send(embed=embed)

@whois.error
async def whois_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		roles = [role for role in ctx.author.roles]
		embed = discord.Embed(colour=ctx.author.colour,
		                      timestamp=ctx.message.created_at)
		embed.set_author(name=f'Who is {ctx.author}?')
		embed.set_image(url=ctx.author.avatar_url)
		embed.set_footer(text=f'Requested by {ctx.author}',
		                 icon_url=ctx.message.author.avatar_url)

		embed.add_field(name='Name', value=ctx.author.display_name)
		embed.add_field(name='ID', value=ctx.author.id, inline=False)

		embed.add_field(
		    name='Created at',
		    value=ctx.author.created_at.strftime('%a, %#d, %B %Y, %I:%M %p'),
		    inline=False)
		embed.add_field(
		    name='Joined at',
		    value=ctx.author.joined_at.strftime('%a, %#d, %B %Y, %I:%M %p'),
		    inline=False)

		embed.add_field(name=f'Roles ({len(roles)})',
		                value=' '.join([role.mention for role in roles]),
		                inline=False)

		await ctx.send(embed=embed)

@bot.command(aliases=['av'])
async def avatar(ctx, member: discord.Member):
	embed = discord.Embed(
	    title=f'{member}',
      description=f"[***avatar url***]({member.avatar_url})",
	    colour=member.colour,
	)
	embed.set_image(url='{}'.format(member.avatar_url))
	embed.set_footer(text=f'requested by {ctx.author}',
	                 icon_url=ctx.message.author.avatar_url)
	await ctx.send(embed=embed)

@avatar.error
async def avatar_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		embed = discord.Embed(
		    title=f'{ctx.author}',
        description=f"[***avatar url***]({ctx.author.avatar_url})",
		    colour=ctx.author.colour,
		)
		embed.set_image(url='{}'.format(ctx.author.avatar_url))
		embed.set_footer(text=f'requested by {ctx.author}',
		                 icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
	msg = await ctx.send('**Calculating...**')
	await asyncio.sleep(1)
	await msg.edit(content=f'Latency: {round(bot.latency*1000)}ms')

@bot.command(aliases=['si'])
async def serverinfo(ctx):
	name = str(ctx.guild.name)
	owner = str(ctx.guild.owner.mention)
	ide = str(ctx.guild.id)
	region = str(ctx.guild.region)
	membercount = str(ctx.guild.member_count)
	icon = str(ctx.guild.icon_url)
	chanz = ctx.guild.text_channels
	voic = ctx.guild.voice_channels
	but = [bot.mention for bot in ctx.guild.members if bot.bot]

	embed = discord.Embed(title=name + " Server Information",
	                      colour=ctx.author.colour,
	                      timestamp=ctx.message.created_at)
	embed.add_field(name='Owner', value=owner, inline=False)
	embed.add_field(name='Server ID', value=ide, inline=True)
	embed.add_field(name='Server Region', value=region, inline=True)
	embed.add_field(name='Verification-Level',
	                value=ctx.guild.verification_level,
	                inline=False)
	embed.add_field(name='Member Count', value=membercount, inline=True)
	embed.add_field(name='Bot Count', value=len(but), inline=True)
	embed.add_field(name='Human Count',
	                value=str(int(membercount) - int(len(but))),
	                inline=True)
	embed.add_field(name='Text Channels', value=len(chanz), inline=True)
	embed.add_field(name='Voice Channels', value=len(voic), inline=True)
	embed.add_field(
	    name='Created at',
	    value=str(ctx.guild.created_at.strftime('%a, %#d, %B %Y, %I:%M %p')),
	    inline=False)
	embed.set_thumbnail(url=icon)

	await ctx.send(embed=embed)

#reaction
@bot.command()
async def moji(ctx):
	embed = discord.Embed(colour=discord.Colour.blue(),
	                      title="Pick Your Favourite Role",
	                      timestamp=ctx.message.created_at)
	astra = discord.utils.get(ctx.guild.roles, id=819456076289540116)
	reyna = discord.utils.get(ctx.guild.roles, id=819456087719411712)
	phoenix = discord.utils.get(ctx.guild.roles, id=819456085617541130)
	raze = discord.utils.get(ctx.guild.roles, id=819493761645936662)
	kj = discord.utils.get(ctx.guild.roles, id=819456089380356108)
	viper = discord.utils.get(ctx.guild.roles, id=819494765346553896)
	skye = discord.utils.get(ctx.guild.roles, id=819489234947407892)
	sage = discord.utils.get(ctx.guild.roles, id=819456090885718026)
	jett = discord.utils.get(ctx.guild.roles, id=819493931166335017)
	sova = discord.utils.get(ctx.guild.roles, id=819498699351785472)
	tes = f'<:astra:819504243584008234> : {astra.mention}\n<:reyna:819504299145953280> : {reyna.mention}\n<:phoenix:819504265252569098> : {phoenix.mention}\n<:raze:819504224274219029> : {raze.mention}\n<:kj:819504200634728448> : {kj.mention}\n<:viper:819504150853320745> : {viper.mention}\n<:skye:819504177066934273> : {skye.mention}\n<:sage:819503962146996255> : {sage.mention}\n<:jett:819504127037538315> : {jett.mention}\n<:sova:819503833020629002> : {sova.mention}'
	embed.add_field(name='Pick One!', value=''.join(tes))
	ressss = 10
	mojiee = [
	    '<:astra:819504243584008234>', '<:reyna:819504299145953280>',
	    '<:phoenix:819504265252569098>', '<:raze:819504224274219029>',
	    '<:kj:819504200634728448>', '<:viper:819504150853320745>',
	    '<:skye:819504177066934273>', '<:sage:819503962146996255>',
	    '<:jett:819504127037538315>', '<:sova:819503833020629002>'
	]
	msg = await ctx.send(embed=embed)
	for i in range(ressss):
		await msg.add_reaction(mojiee[i])

@bot.command()
async def moji22(ctx):
	embed = discord.Embed(
	    colour=discord.Colour.blue(),
	    title="Pick Your Roles",
	    description=
	    "react <a:Akuq:799618942808490064> untuk mendapatkan role member!")
	msg = await ctx.send(embed=embed)
	await msg.add_reaction('<a:Akuq:799618942808490064>')

@bot.event
async def on_raw_reaction_add(payload):
	message_id = payload.message_id
	if message_id == 819517607278936064:
		guild_id = payload.guild_id
		guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

		if payload.emoji.name == 'astra':
			role = discord.utils.get(guild.roles, name="Cosmic Divide")
		elif payload.emoji.name == 'reyna':
			role = discord.utils.get(guild.roles, name='Devour')
		elif payload.emoji.name == 'phoenix':
			role = discord.utils.get(guild.roles, name='Blaze')
		elif payload.emoji.name == 'raze':
			role = discord.utils.get(guild.roles, name='Showstopper')
		elif payload.emoji.name == 'kj':
			role = discord.utils.get(guild.roles, name='Lockdown')
		elif payload.emoji.name == 'viper':
			role = discord.utils.get(guild.roles, name='Biohazard')
		elif payload.emoji.name == 'skye':
			role = discord.utils.get(guild.roles, name='Seeker')
		elif payload.emoji.name == 'sage':
			role = discord.utils.get(guild.roles, name='Warden')
		elif payload.emoji.name == 'jett':
			role = discord.utils.get(guild.roles, name='Blade Storm')
		elif payload.emoji.name == 'sova':
			role = discord.utils.get(guild.roles, name='Hunter')

		if role is not None:
			member = discord.utils.find(lambda m: m.id == payload.user_id,
			                            guild.members)
			if member is not None:
				await member.add_roles(role)
				print(f'{member} get {role}')

	if message_id == 819815121954144286:
		guild_id = payload.guild_id
		guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

		if payload.emoji.name == 'Akuq':
			role = discord.utils.get(guild.roles, name="Member")
		if role is not None:
			member = discord.utils.find(lambda m: m.id == payload.user_id,
			                            guild.members)
			if member is not None:
				await member.add_roles(role)
				print(f'{member} get {role}')

@bot.event
async def on_raw_reaction_remove(payload):
	message_id = payload.message_id
	if message_id == 819517607278936064:
		guild_id = payload.guild_id
		guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)

		if payload.emoji.name == 'astra':
			role = discord.utils.get(guild.roles, name="Cosmic Divide")
		elif payload.emoji.name == 'reyna':
			role = discord.utils.get(guild.roles, name='Devour')
		elif payload.emoji.name == 'phoenix':
			role = discord.utils.get(guild.roles, name='Blaze')
		elif payload.emoji.name == 'raze':
			role = discord.utils.get(guild.roles, name='Showstopper')
		elif payload.emoji.name == 'kj':
			role = discord.utils.get(guild.roles, name='Lockdown')
		elif payload.emoji.name == 'viper':
			role = discord.utils.get(guild.roles, name='Biohazard')
		elif payload.emoji.name == 'skye':
			role = discord.utils.get(guild.roles, name='Seeker')
		elif payload.emoji.name == 'sage':
			role = discord.utils.get(guild.roles, name='Warden')
		elif payload.emoji.name == 'jett':
			role = discord.utils.get(guild.roles, name='Blade Storm')
		elif payload.emoji.name == 'sova':
			role = discord.utils.get(guild.roles, name='Hunter')

		if role is not None:
			member = discord.utils.find(lambda m: m.id == payload.user_id,
			                            guild.members)
			if member is not None:
				await member.remove_roles(role)
				print(f'{member} remove {role}')

#admin
@bot.command()
@commands.has_permissions(administrator=True)
async def admin_help(ctx):
  embed= discord.Embed(
    title="Commands for Admin",
    colour=ctx.author.colour
  )
  embed.add_field(name="about member", value="".join("Ban\nKick"))
  await ctx.author.send(embed=embed)
  await ctx.message.add_reaction('<a:Akuq:799618942808490064>')

@admin_help.error
async def admin_help_error(ctx,error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.message.add_reaction("❌")

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member, *, reason: None):
	await member.ban(reason=reason)
	await ctx.send(f'{member} has been banned by {ctx.author}')

@ban.error
async def ban_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.mention}You Cant Do That ❌',delete_after=3)

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member,*,reason: None):
  await member.kick(reason=reason)
  await ctx.send(f"{member} has been kicked by {ctx.author}")

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.MissingPermissions):
    await ctx.send(f'{ctx.author.mention}You Cant Do That ❌',delete_after=3)

keep_alive()
bot.run(os.getenv('TOKEN'))

while True:
	time.sleep(0.5)
