import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

class Cartoon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cartoon(self, ctx, *, query):
        """
        Search for a cartoon and return its title, summary, and image.
        """
        try:
            # Use the query to search for cartoons
            query = query.replace(" ", "+")
            url = f"https://www.thewatchcartoononline.tv/search?keyword={query}"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all("div", {"class": "item"})
            result = results[0]

            # Extract the title, summary, and image of the first result
            title = result.find("h3", {"class": "title"}).text
            summary = result.find("div", {"class": "summary"}).text.strip()
            image_url = result.find("div", {"class": "poster"}).find("img")["src"]

            # Send an embed with the information
            embed = discord.Embed(title=title, description=summary, color=discord.Color.green())
            embed.set_image(url=image_url)
            await ctx.send(embed=embed)

        except:
            await ctx.send("Could not find any results for that query.")

def setup(bot):
    bot.add_cog(Cartoon(bot))
