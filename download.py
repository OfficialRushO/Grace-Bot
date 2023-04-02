import discord
from discord.ext import commands
import youtube_dl
import asyncio

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class Download(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mp3download')
    async def mp3_download(self, ctx, *, search_query):
        async with ctx.typing():
            try:
                search_query = search_query.strip()
                await ctx.send(f"Downloading audio for: {search_query}")
                url = f"ytsearch:{search_query}"
                info = ytdl.extract_info(url, download=False)
                URL = info['formats'][0]['url']
                filename = info['title']
                await ctx.send(f"Downloading {filename}...")
                loop = asyncio.get_running_loop()
                await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=True))
                await ctx.send(f"Downloaded {filename} successfully!")
                await ctx.send(f"Uploading {filename} to Discord...")
                with open(f"{filename}.mp3", 'rb') as f:
                    song = discord.File(f, filename=f"{filename}.mp3")
                    await ctx.send(file=song)
            except Exception as e:
                await ctx.send(f"Error: {str(e)}")

def setup(bot):
    bot.add_cog(Download(bot))
