import asyncio, re, yt_dlp

from crowgram import config
from pyrogram.types import Audio, Voice
from pyrogram.types import Video, VideoNote
from pytgcalls.types import AudioQuality, VideoQuality
from pytgcalls.types import MediaStream
from pytgcalls.types.raw import AudioParameters
from pytgcalls.types.raw import VideoParameters
from typing import Union
from youtubesearchpython.__future__ import VideosSearch


def get_audio_name(audio: Union[Audio, Voice]):
    try:
        file_name = (
            audio.file_unique_id
            + "."
            + (
                (audio.file_name.split(".")[-1])
                if (not isinstance(audio, Voice))
                else "ogg"
            )
        )
    except:
        file_name = audio.file_unique_id + "." + ".ogg"
        
    return file_name


def get_video_name(video: Union[Video, VideoNote]):
    try:
        file_name = (
            video.file_unique_id
            + "."
            + (video.file_name.split(".")[-1])
        )
    except:
        file_name = video.file_unique_id + "." + "mp4"
    
    return file_name
    

# Get Details Of Youtube Video
async def get_stream_info(vidid, query):
    url = (
        f"https://www.youtube.com/watch?v={vidid}"
        if vidid else None
    )
    search = url if url else query
    results = VideosSearch(search, limit=1)
    for result in (await results.next())["result"]:
        try:
            title = result["title"]
            title = re.sub("\W+", " ", title)
            title = title.title()[:18]
        except:
            title = "Unsupported Title"
        vidids = vidid if vidid else result["id"]
        vidurl = url if url else result["link"]
        try:
            duration = result["duration"] + " Mins"
        except:
            duration = "Unknown Mins"
    
    return [vidids, vidurl, title, duration]



# Direct Link From YouTube
async def get_stream_link(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "bestvideo+bestaudio/best",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    links = stdout.decode().split('\n')
    return links[0], links[1]


# Stream Using PyTgCalls
async def get_stream_data(
    media, audio: None, type: str
):
    if type == "Audio":
        if audio:
            stream = MediaStream(
                media_path=audio,
                video_flags=MediaStream.IGNORE,
                audio_parameters=AudioQuality.STUDIO,
            )
        else:
            stream = MediaStream(
                media_path=media,
                video_flags=MediaStream.IGNORE,
                audio_parameters=AudioQuality.STUDIO,
            )
    elif type == "Video":
        if audio:
            stream = MediaStream(
                media_path=media,
                audio_path=audio,
                audio_parameters=AudioQuality.STUDIO,
                video_parameters=VideoQuality.HD_720p,
            )
        else:
            stream = MediaStream(
                media_path=media,
                audio_parameters=AudioQuality.STUDIO,
                video_parameters=VideoQuality.HD_720p,
            )
            
    return stream
            
            
