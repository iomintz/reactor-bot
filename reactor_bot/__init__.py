#!/usr/bin/env python3
# encoding: utf-8

"""reactor_bot - The best dang Discord poll bot around™"""

__version__ = '4.4.0'
__author__ = 'Benjamin Mintz <bmintz@protonmail.com>'

import sys

import discord
from discord.ext import commands

from reactor_bot import emoji_utils as emoji
from reactor_bot.cogs.poll import Poll

prefixes = [capitalization + ':' for capitalization in ('Poll', 'poll', 'POLL')]
bot = commands.Bot(command_prefix=commands.when_mentioned_or(*prefixes))


@bot.event
async def on_ready():
	message = 'Logged in as: %s' % bot.user
	separator = '━' * len(message)
	print(separator, message, separator, sep='\n')
	await bot.change_presence(game=discord.Game(name='poll:help'))


# since discord.py doesn't allow for commands with no name,
# (poll: foo) we have to process them manually in that case
@bot.event
async def on_message(message):
	context = await bot.get_context(message)

	if context.prefix or bot.user in message.mentions:
		if context.command:
			await bot.process_commands(message)
		else:
			await Poll.reaction_poll(message)


@bot.event
async def on_message_edit(before, after):
	if any(reaction.me for reaction in before.reactions):
		await before.clear_reactions()
	await on_message(after)
