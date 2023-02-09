from datetime import datetime, timedelta
from youtube_dl import YoutubeDL

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

def calc_time(time):
    now = datetime.now()
    new_time = now - time
    return str(new_time).split('.')[0]

def check_time(cur):
    info = cur['info']
    time = cur['time']
    new_time = timedelta(seconds=info["duration"])
    cur_time = calc_time(time)
    duration = str(new_time).split('.')[0]

    return cur_time, duration


# check_time()
# now = datetime.now()
# timer = now - timedelta(hours = 1)

# print(now)
# print(calc_time(timer))