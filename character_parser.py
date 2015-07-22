from bs4 import BeautifulSoup
import re
from json import dumps

def parse_single_char(plain_html):
	#Create BeautifulSoup Object
	soup = BeautifulSoup(plain_html)

	#all the important information is in 3 seperate tables
	tables = soup.findAll('table')

	for table in tables:
		# general character information is in this table
		# print table
		tr_list = table.findAll('tr')
		if tr_list[0].text == "Character Information":
			char_information_table = table


	char_dict = {}

	for elem in char_information_table.findAll('tr'):
		if elem.text != "Character Information":
			a = elem.findAll('td')
			char_dict[a[0].text[:-1]] = a[1].text

	print char_dict['Name']
	print char_dict['Level']
