import requests
import re

from bs4 import BeautifulSoup

response = requests.get("https://jollyposhfoods.com/collections/savoury-pies?srsltid=AfmBOopTgRpEmH-59rHJxhT1ya20TA9WFiRg_nWJuIEfcE30MkRtoJcg")
soup = BeautifulSoup(response.text, 'lxml')
names = soup.find_all(class_="grid-product__title")

stopwords = ["14oz", "10oz", "8oz",]

all_names = ""

for name in names:
    all_names += name.text + ","

str = all_names.split(',')

for word in str:
    sorted = filter(lambda w: w not in stopwords, re.split(r'\W+', word.lower()))
    print(list(sorted))

# I've stolen this
# reduced = filter(lambda w: w not in stopwords, re.split(r'\W+', sentence.lower()))