from discord.utils import get
from help_functions.help_text import *
from help_functions.help_time import *
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from help_functions.help_queue import *


async def play(ctx, url, bot, msg = None):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice is None:   await ctx.send(embed=str_not_in_voice_channel); return
    elif voice.channel != ctx.message.author.voice.channel: await ctx.send(embed=str_not_in_same_channel);  return
    elif 'music.163.com' in url:    await ctx.send(embed=str_no_netease);   return

    if not msg: msg = await ctx.send(embed=str_loading_song)   

    new_song_len = await addToQueue(ctx.guild, url = url)
    
    if not new_song_len:    await msg.edit(content='', embed=str_invalid_url)
    else:                   await play_music(ctx, bot, msg, new_song_len)

    # if "entries" not in info:
    #     url = info['url']
    #     source = FFmpegPCMAudio(url, **FFMPEG_OPTIONS)
    #     if not voice.is_playing():
    #         voice.play(source, after=lambda x=0: check_queue(ctx, ctx.guild.id))
    #         temp = {}; temp['info'] = info; temp['time'] = datetime.now()
    #         current_song[ctx.guild.id] = temp
    #         timer = check_time(temp)
    #         embedVar = discord.Embed(title=f'I'm going to play this song!', description=f'{info["title"]}\n[{timer[0]}/{timer[1]}]\n{info["webpage_url"]}', color=0x8B4C39)
    #         await msg.edit(content='', embed=embedVar)
    #     else:
    #         await addToQueue(ctx.guild, info)
    #         temp_len = len(song_queue[ctx.guild.id])
    #         if temp_len == 0: temp_len = 1
    #         else: temp_len += 2
    #         embedVar = discord.Embed(title=f'I added this song to my playlist!', description=f'[{temp_len}]\t{info["title"]}\n{info["webpage_url"]}', color=0x8B4C39)
    #         await msg.edit(content='', embed=embedVar)
    # else:


async def play_music(ctx, bot, msg, new_song_len):
    voice = get(bot.voice_clients, guild=ctx.guild)
    
    cur_len = len(song_queue[ctx.guild.id])
    is_edit_msg = False

    if not voice.is_playing():
        cur_info = song_queue[ctx.guild.id].pop(0)

        with YoutubeDL(YDL_OPTIONS) as ydl: cur_info = ydl.extract_info(cur_info.watch_url, download=False)

        temp = {}; temp['info'] = cur_info; temp['time'] = datetime.now()
        current_song[ctx.guild.id] = temp
        timer = check_time(temp)
        source = FFmpegPCMAudio(cur_info['url'], **FFMPEG_OPTIONS)
        voice.play(source, after=lambda x=0: check_queue(ctx, ctx.guild.id))
        embedVar = discord.Embed(title=f'Im going to play this song!', description=f'{cur_info["title"]}\n[{timer[0]}/{timer[1]}]\n{cur_info["webpage_url"]}', color=0x8B4C39)
        await msg.edit(content='', embed=embedVar)
        is_edit_msg = True
    
    elif new_song_len == 1:
        new_song = song_queue[ctx.guild.id][cur_len - 1]
        embedVar = discord.Embed(title=f'I added this song to my playlist!', description=f'[{cur_len}]\t{new_song.title}\n{new_song.watch_url}', color=0x8B4C39)
        await msg.edit(content='', embed=embedVar)
        is_edit_msg = True
    
    if new_song_len > 1:
        # embedVar = discord.Embed(title=f'The album {info["title"]} neutral {len(info["entries"])}The song has been added to the playlist!', description="", color=0x8B4C39)
        embedVar = discord.Embed(title=f'already {new_song_len} The song has been added to the playlist!', description="", color=0x8B4C39)
        if is_edit_msg: await msg.channel.send(content = '', embed=embedVar)
        else:           await msg.edit(content='', embed=embedVar)
