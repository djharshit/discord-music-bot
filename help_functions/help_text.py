import discord

YDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'ytsearch',
        'source_address': '0.0.0.0',
    }
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

str_not_in_voice_channel = discord.Embed(title="You are not in the channel! Why did you ask me to come! Type/join and let me come to your channel!", description="", color=0xD0B8A0)
str_not_in_same_channel = discord.Embed(title="I'm not even on your channel! Why did you ask me to come! Type/join and let me come to your channel!", description="", color=0xD0B8A0)
str_no_netease = discord.Embed(title="Currently does not support Netease cloud pinch!", description="", color=0xD0B8A0)
str_join_channel = discord.Embed(title="I'm coming to your channel! Let me heal you", description="", color=0x487B60)
str_loading_song = discord.Embed(title=f'Loading song..', description='', color=0x8B4C39)
str_not_song_playing = discord.Embed(title=f'I have no songs to play!', description='', color=0x487B60)
str_exceds_songs = discord.Embed(title=f'I dont have that many songs to play pinch!', description='', color=0x487B60)
str_no_song_next = discord.Embed(title=f'I have no songs to play next!', description='', color=0x487B60)
str_not_playlist = discord.Embed(title=f'This is not a playlist pinch!', description='', color=0x487B60)
str_invalid_url = discord.Embed(title=f'This is not a valid link pinch!', description='', color=0x487B60)
