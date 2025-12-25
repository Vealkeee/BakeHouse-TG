import requests
import asyncio
import time
import re

from playwright.async_api import async_playwright

class get_assorti():
    async def get_bakes():
            async with async_playwright() as s:
                browser = await s.chromium.launch()
                page = await browser.new_page()
                await page.goto('https://www.greggs.com/menu?category=savouries-bakes')
                await page.screenshot(path='./img/bakes.png', full_page=True)

                bakes = await page.get_by_text("Bake").all_inner_texts()

                for _ in range(3):
                    bakes.pop(0)

                await browser.close()

                return bakes

    async def get_pizza():
            async with async_playwright() as s:
                browser = await s.chromium.launch()
                page = await browser.new_page()
                await page.goto('https://www.greggs.com/menu?category=savouries-bakes')
                await page.screenshot(path='./img/bakes.png', full_page=True)

                pizza = await page.get_by_text("Pizza").all_inner_texts()

                await browser.close()

                return pizza
# If holly playwright won't help:

# from bs4 import BeautifulSoup

# response = requests.get("https://jollyposhfoods.com/collections/savoury-pies?srsltid=AfmBOopTgRpEmH-59rHJxhT1ya20TA9WFiRg_nWJuIEfcE30MkRtoJcg")
# soup = BeautifulSoup(response.text, 'lxml')
# names = soup.find_all(class_="grid-product__title")

# stopwords = ["14oz", "10oz", "8oz"]

# all_names = ""

# for name in names:
#     all_names += name.text + "\n"

# str = all_names.split('\n')

# for word in str:
#     sorted = filter(lambda w: w not in stopwords, re.split(r'\W+', word.lower()))
#     print(list(sorted))