from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://finance.naver.com/marketindex/")
soup = BeautifulSoup(target, "html.parser", from_encoding='utf-8')

for tag in soup.select(".data_lst li"):
    print(tag.select_one(".blind").string.split(" ")[-1], ":", tag.select_one(".value").string)
