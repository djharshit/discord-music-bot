from help_functions.help_text import *
from help_functions.help_time import *
from help_functions.help_queue import *
import random

async def randomQueue(ctx, bot):
    msg = await ctx.send(embed = str_loading_song)
    if ctx.guild.id not in song_queue or len(song_queue[ctx.guild.id]) <= 1:
        song_queue[ctx.guild.id] = []
        str_random_queue = discord.Embed(title='Shuffle Queue', description='The queue is too short to be randomized', color=0x487B60)
    else:
        random.shuffle(song_queue[ctx.guild.id])
        str_random_queue = discord.Embed(title='Shuffle Queue', description='queue has been randomized', color=0x487B60)
    await msg.edit(embed=str_random_queue)
