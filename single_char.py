from __future__ import print_function
from bs4 import BeautifulSoup
import urllib2

character = raw_input("Enter Character Name: ").replace(' ', '+')
print("Hello, ", character)

url="http://www.tibia.com/community/?subtopic=characters&name=" + character
# print(url + character)

page=urllib2.urlopen(url)

soup = BeautifulSoup(page.read()).find(class_="BoxContent")
table = soup.find("table")

	# 1 	= Name
	# 2		= Sex
	# 3		= Vocation
	# 4		= Level
	# 5		= Accountchievments?
	# 6		= World
	# 7		= Residence
	# 8		= Some kind of Error?
	# 9		= Comment
	# 10	= Account Status

# rows = table.findAll('tr')[1]
# cols = rows.findAll('td')

# name = str(cols[1].find(text=True))
# print("Name: " + name)

# data= []
# rows = table.find_all('tr')
# for row in rows:
#     cols = row.find_all('td')
#     cols = [ele.text.strip() for ele in cols]
#     data.append([ele for ele in cols if ele]) # Get rid of empty values
#     print(row.text)

data= []
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    # print(cols)
    cols = [ele.text.strip() for ele in cols]
    # if len(cols) == 2:
    # 	print(cols[1])
    data.append([ele for ele in cols if ele]) # Get rid of empty values
    print(row.text)

# interesting = soup.find("div", class_="BoxContent")

# BoxContent = soup('div', class_="BoxContent")
# # print [td.text for td in BoxContent]
# # for td in BoxContent:
# # 	print(td.text)

# # print(soup.find_all('td', text=['Character Information']))

# # for td in BoxContent:
# # 	if (td.contains("Character Information")):


# # 		print(td.text)

# print(BoxContent)
















