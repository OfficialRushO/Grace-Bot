import discord
import requests
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('/movie'):
        search = message.content.split("/movie ", 1)[1]
        search = search.replace(" ", "+")
        url = f'https://www.imdb.com/find?q={search}&ref_=nv_sr_sm'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        try:
            movie_title = soup.find_all("td", {"class": "result_text"})[0].find("a").text
            movie_year = soup.find_all("td", {"class": "result_text"})[0].find("span", {"class": "lister-item-year text-muted unbold"}).text
            movie_rating = soup.find_all("td", {"class": "result_text"})[0].find("span", {"class": "rating"}).text
            movie_link = soup.find_all("td", {"class": "result_text"})[0].find("a")["href"]
            embed = discord.Embed(title=movie_title, description=f"{movie_rating} | {movie_year}", url=f'https://www.imdb.com{movie_link}')
            await message.channel.send(embed=embed)
        except:
            await message.channel.send("No results found.")
