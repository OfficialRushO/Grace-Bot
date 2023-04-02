import discord
import requests
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('/anime'):
        search = message.content.split("/anime ", 1)[1]
        search = search.replace(" ", "+")
        url = f'https://www.crunchyroll.com/search?from=&q={search}'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        anime_title = soup.find_all("a", {"class": "text-link ellipsis"})
        anime_description = soup.find_all("div", {"class": "short-description ellipsis"})
        anime_link = soup.find_all("a", {"class": "portrait-element block-link titlefix"})
        for title, description, link in zip(anime_title, anime_description, anime_link):
            embed = discord.Embed(title=title.text, description=description.text, url=f'https://www.crunchyroll.com{link["href"]}')
            await message.channel.send(embed=embed)
