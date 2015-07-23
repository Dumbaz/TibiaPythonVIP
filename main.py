import html_getter
import character_parser

char_html = html_getter.get_url("https://secure.tibia.com/community/?subtopic=characters&name=Ziar+Shadowdeath")

character_info = character_parser.parse_single_char(char_html)
print character_info
