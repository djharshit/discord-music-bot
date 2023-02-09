import random
from discord.utils import get
from commands.speech_synthesis import tts
import discord
import time

import importlib
import commands.speech_synthesis

on_tts = False

######### Bot Commands #########
# @bot.event
async def on_message(message, bot):
    if message.author == bot.user: return

    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'[{channel}] {username}: {user_message}')

    random_reply_q = random.randint(1, 100)
    random_reply_b = random.randint(1, 100)
    random_reply_o = random.randint(1, 100)

    if (random_reply_q == 1):       await message.channel.send('?')
    
    elif (random_reply_q == 2):     await message.channel.send('why')
    
    elif "Hello" in user_message:
        if username == 'MRTx':      await message.channel.send('Wow! Isnt this Teacher!')
        elif 'Nancy' in username:   await message.channel.send('Wow! Isnt this Nancy not revealing!')
        elif 'Maze' in username:    await message.channel.send('Wow! father!')
        else:                       await message.channel.send('I do not know you')
    
    # elif "pinch" in user_message:      await message.channel.send('pinch')
    
    elif ("Is it" in user_message or "Well" in user_message) and random_reply_q == 3:
        reply_msg = user_message.replace("Is it", "ah").replace("Well", "ah").replace("？", "！")
        
        if "you" in reply_msg:       reply_msg = reply_msg.replace("you", "I")
        elif "I" in reply_msg:     reply_msg = reply_msg.replace("I", "you")
        await message.channel.send(reply_msg)
    
    elif ("?" in user_message or "？" in user_message) and random_reply_q == 10:    await message.channel.send('?')
    
    elif "I want" in user_message and random_reply_b == 1:    await message.channel.send('I play! Dont!')
    
    elif ("Original" in user_message or "O" in user_message or "p" in user_message or "P" in user_message or "o" in user_message):
        if "Tony" in username and random_reply_o == 1:     await message.channel.send('I play! There is OP!')

    if on_tts:
        voice = get(bot.voice_clients, guild=message.guild)
        if voice and voice.is_connected():
            importlib.reload(commands.speech_synthesis)
            from commands.speech_synthesis import tts

            if (await tts(message)):
                voice.play(discord.FFmpegPCMAudio("voices/test.mp3"))
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.5
                while voice.is_playing():
                    time.sleep(1)
                voice.stop()
                return

    await bot.process_commands(message)
##################################
