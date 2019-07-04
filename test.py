#!/usr/bin/env python3
# coding: utf-8

import requests

r = requests.get('https://chucknorrisfacts.fr/api/get?data=nb:1;type:txt;tri:alea')
joke = r.json()[0].get('fact')

print(joke)