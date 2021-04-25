#READPLS
#If you need to make reaction bot and embed help dm my discord
#and any question dm me too
#you can delete this 4 line info at your code
import discord
import asyncio
import random
import datetime
import time
import os

from discord.ext import commands
from discord.utils import get
from random import choice
from discord import File
from datetime import datetime

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="Your Prefix", intents=intents)#example prefix = "," "!"

#activity of bot
@bot.event
async def on_ready():
  print('im ready')
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="hello"))

@bot.event
async def on_member_remove(member):
	guild = bot.get_guild()#put your guild id here
  if guild == :#put your guild id
	  embed = discord.Embed(
	     title=f'Goodbye {member.name}!',
	      description='Maybe we meet again :^)',
	      colour=member.colour,
	  )
	  embed.set_image(url=member.avatar_url)
	  channel = guild.get_channel()#put your channel id where the bot send message
	  await channel.send(embed=embed)

@bot.event
async def on_member_join(member):
	guild = bot.get_guild()#put your guild id
  if guild == :#put your guild id
	  embed = discord.Embed(
	      title=f'Welcome {member.name}!',
	      description=f'Welcome to the {member.guild}',
	      colour=member.colour,
	  )
	  embed.set_image(url=member.avatar_url)
	  channel = guild.get_channel()#put your channel id where the bot send message
	  await channel.send(embed=embed)

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

bot.run("put your token here")

while True:
	time.sleep(1)
