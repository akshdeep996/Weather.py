#! usr/bin/python3
# simple current weather report

import requests
from bs4 import BeautifulSoup

print("Please enter ur City name")
city = str(input())
print("Please wait.... while we get u ur weather report")
res = requests.get("https://www.google.co.in/search?q=weather+" + city)

soup = BeautifulSoup(res.content,"lxml")

print(soup.find_all("span",{"class":"wob_t"})[0].text)
