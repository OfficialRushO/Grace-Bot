import discord
from discord.ext import commands
from levels import LevelingSystem
from play import MusicPlayer
from download import MusicDownloader
from anime import AnimeSearcher
from movie import MovieSearcher
from series import SeriesSearcher
from cartoon import CartoonSearcher
from voice_changer import VoiceChanger
from notification import SocialMediaNotifier
from moderation import Moderation

# Set up bot client
bot = commands.Bot(command_prefix='/')

# Add commands
leveling_system = LevelingSystem(bot)
bot.add_cog(leveling_system)

music_player = MusicPlayer(bot)
bot.add_cog(music_player)

music_downloader = MusicDownloader(bot)
bot.add_cog(music_downloader)

anime_searcher = AnimeSearcher(bot)
bot.add_cog(anime_searcher)

movie_searcher = MovieSearcher(bot)
bot.add_cog(movie_searcher)

series_searcher = SeriesSearcher(bot)
bot.add_cog(series_searcher)

cartoon_searcher = CartoonSearcher(bot)
bot.add_cog(cartoon_searcher)

voice_changer = VoiceChanger(bot)
bot.add_cog(voice_changer)

notifier = SocialMediaNotifier(bot)
bot.add_cog(notifier)

moderation = Moderation(bot)
bot.add_cog(moderation)

# Run the bot
bot.run('your_bot_token')
