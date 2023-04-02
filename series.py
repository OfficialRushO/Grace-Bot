import discord
import requests
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('/series'):
        search = message.content.split("/series ", 1)[1]
        search = search.replace(" ", "+")
        url = f'https://www.imdb.com/find?q={search}&ref_=nv_sr_sm'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        try:
            series_title = soup.find_all("td", {"class": "result_text"})[0].find("a").text
            series_year = soup.find_all("td", {"class": "result_text"})[0].find("span", {"class": "lister-item-year text-muted unbold"}).text
            series_rating = soup.find_all("td", {"class": "result_text"})[0].find("span", {"class": "rating"}).text
            series_link =
