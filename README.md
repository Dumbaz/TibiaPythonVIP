#TibiaPythonVIP

A small tool that should be run on a webserver
to collect character data from the MMORPG Tibia.

Currently it uses Flask, and you can use the tibiaVIP.py
script to run the small server. If you then visit the adress

```
http://localhost:5000/get_character?character=character+name
```

it will give you a JSON with the character information of the
character you've given in the query string which you could find
on the Tibia website.

#Requirements

Currently all you should need is Python 2.7 and the BeautifulSoup
and Flask libs.
