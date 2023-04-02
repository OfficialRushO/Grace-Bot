import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio
import subprocess
import os
from random import randint

class VoiceChanger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def voicechanger(self, ctx, voice=None):
        """
        Change your voice to one of the available options.
        """
        try:
            if not voice:
                # Send a message showing the available options
                voices = ["vader", "robot", "alien", "female", "male", "echo", "underwater", "chipmunk", "slow", "fast",
                          "monster", "tremolo", "darthvader", "backwards", "oldman", "jigsaw", "bird", "flanger", "muted"]
                await ctx.send("Available voice options: " + ", ".join(voices))
                return

            # Check if the user is in a voice channel
            if not ctx.author.voice:
                await ctx.send("You are not in a voice channel.")
                return

            # Connect to the user's voice channel
            voice_channel = ctx.author.voice.channel
            vc = await voice_channel.connect()

            # Set the voice changer effect based on the user's choice
            effect = f"voices/{voice}.pcm"
            if not os.path.exists(effect):
                await ctx.send("That voice option is not available.")
                await vc.disconnect()
                return

            # Play an audio file with the selected effect
            audio_file = f"voices/{randint(1, 6)}.mp3"
            subprocess.call(["ffmpeg", "-i", audio_file, "-af", f"af=aphaser=0.5:decay=1:offset=0.3:depth=0.7:stereo=1, "\
                            f"rubberband=pitch-scale={randint(1, 100)}", "-f", "s16le", "-ar", "48000", "-ac
