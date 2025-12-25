import requests
import time
import re

from playwright.sync_api import sync_playwright, expect

def sync():
    with sync_playwright() as s:
        browser = s.chromium.launch()
        page = browser.new_page()
        page.goto('https://www.greggs.com/menu?category=savouries-bakes')
        page.screenshot(path='./img/bakes.png', full_page=True)

        bakes = page.get_by_text("Bake").all_inner_texts()

        for _ in range(3):
            bakes.pop(0)

        for i in range(len(bakes)):
            print(bakes[i])

        browser.close()

sync()

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