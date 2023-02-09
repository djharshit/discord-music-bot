from discord.utils import get
from help_functions.help_text import *
from help_functions.help_time import *
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from help_functions.help_queue import *
from commands.cmd_play import play_music

async def search(ctx, request, bot):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice is None:
        await ctx.send(embed=str_not_in_voice_channel)
        return
    elif voice.channel != ctx.message.author.voice.channel:
        await ctx.send(embed=str_not_in_same_channel)
        return
    
    msg = await ctx.send(embed=str_loading_song)
    
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{request}", download=False)['entries'][0]
        except:
            info = ydl.extract_info(request, download=False)
        
        if not info:
            embedVar = discord.Embed(title=f'I cant find this song. Hey!', description="", color=0x8B4C39)
            await msg.edit(content = '', embed=embedVar)
            return

        await addToQueue(ctx.guild, url = info['webpage_url'])
        await play_music(ctx, voice, msg, 1)

        # url = info['url']
        # source = FFmpegPCMAudio(url, **FFMPEG_OPTIONS)
        # if not voice.is_playing():
        #     voice.play(source, after=lambda x=0: check_queue(ctx, ctx.guild.id))
        #     temp = {}; temp['info'] = info; temp['time'] = datetime.now()
        #     current_song[ctx.guild.id] = temp
        #     timer = check_time(temp)
        #     embedVar = discord.Embed(title=f'I'm going to play this song!', description=f'{info["title"]}\n[{timer[0]}/{timer[1]}]\n{info["webpage_url"]}', color=0x8B4C39)
        #     await msg.edit(content = '',  embed=embedVar)
        # else:
        #     await addToQueue(ctx.guild, info)
        #     embedVar = discord.Embed(title=f'I added this song to my playlist!', description=f'[{len(song_queue[ctx.guild.id])}] - {info["title"]}', color=0x8B4C39)
        #     await msg.edit(content = '', embed=embedVar)
