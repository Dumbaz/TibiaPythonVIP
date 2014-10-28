from __future__ import print_function
from bs4 import BeautifulSoup
import urllib2

world = raw_input("Enter World Name: ")
print("Checking world ", world)

url="http://www.tibia.com/community/?subtopic=worlds&world=" + world + "&order=level_desc"
# print(url + character)

page=urllib2.urlopen(url)

soup = BeautifulSoup(page.read())

soup = soup.find_all("div", class_="InnerTableContainer")

print(soup)