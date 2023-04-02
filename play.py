import discord
from discord.ext import commands
import youtube_dl

class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, *, query):
        voice_channel = ctx.author.voice.channel
        if not voice_channel:
            return await ctx.send("You are not connected to a voice channel")

        vc = ctx.voice_client
        if not vc:
            vc = await voice_channel.connect()

        if vc.is_playing():
            vc.stop()

        ydl_opts = {
            'format': 'bestaudio/best',
            'quiet': True,
            'outtmpl': 'song.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
            url = info['url']

        vc.play(discord.FFmpegPCMAudio(url))
        await ctx.send(f"Now playing: {info['title']}")

    @commands.command()
    async def stop(self, ctx):
        vc = ctx.voice_client
        if not vc:
            return await ctx.send("I am not currently playing anything")

        if vc.is_paused() or vc.is_playing():
            vc.stop()
            await ctx.send("Playback stopped")

    @commands.command()
    async def pause(self, ctx):
        vc = ctx.voice_client
        if not vc:
            return await ctx.send("I am not currently playing anything")

        if vc.is_playing():
            vc.pause()
            await ctx.send("Playback paused")

    @commands.command()
    async def resume(self, ctx):
        vc = ctx.voice_client
        if not vc:
            return await ctx.send("I am not currently playing anything")

        if vc.is_paused():
            vc.resume()
            await ctx.send("Playback resumed")

def setup(bot):
    bot.add_cog(Play(bot))
