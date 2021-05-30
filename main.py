


import discord
import os
import urllib.request
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(aliases=['emp', 'Emp'])
async def EMP(ctx):
    await ctx.send(
        f'@everyone EMP is under attack!!  Please all join EMP immediately!!!')


@client.command(aliases=['rvn', 'RVN', 'RM', 'Rvn', 'Rm'])
async def rm(ctx):
    await ctx.send(
        f'@everyone RVN is under attack!!  Please all join RVN immediately!!!')


@client.command(aliases=['sod', 'Sod'])
async def SOD(ctx):
    await ctx.send(
        f'@everyone SOD is under attack!!  Please all join SOD immediately!!!')


@client.command(aliases=['959'])
async def dealta(ctx):
    await ctx.send(
        f'@everyone 959 is under attack!!  Please all join 959 immediately!!!')


keep_alive()
client.run(os.getenv('TOKEN'))
