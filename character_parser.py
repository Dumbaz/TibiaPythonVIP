from bs4 import BeautifulSoup
import re

def parse_single_char(plain_html):
	#Create BeautifulSoup Object
	soup = BeautifulSoup(plain_html)

	#all the important information is in 3 seperate tables
	tables = soup.findAll('table')

	for table in tables:
		# general character information is in this table
		# print table
		tr_list = table.findAll('tr')
		print tr_list[0].text