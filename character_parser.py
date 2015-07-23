from bs4 import BeautifulSoup
import re
from json import dumps
from time import strptime

def replace_unicode(u_string):
    return u_string.encode('utf-8').replace("\xa0", " ").replace("\xc2", "")

def parse_single_char(plain_html):
    #Create BeautifulSoup Object
    soup = BeautifulSoup(plain_html)

    #all the important information is in 3 seperate tables
    tables = soup.findAll('table')
    char_dict = {}
    for table in tables:
        # general character information is in this table
        # print table
        tr_list = table.findAll('tr')
        if tr_list[0].text == "Character Information":
            char_information_table = table


        

        for elem in char_information_table.findAll('tr'):
            if elem.text != "Character Information":
                a = elem.findAll('td')
                char_dict[replace_unicode(a[0]\
                                .text[:-1]\
                                .lower())\
                                .replace(" ", "_")] = replace_unicode(a[1].text)
    char_dict['level'] = int(char_dict['level'])
    char_dict['achievement_points'] = int(char_dict['achievement_points'])
    char_dict['last_login'] = strptime(char_dict['last_login'], '%b %d %Y, %H:%M:%S %Z')
    return char_dict
