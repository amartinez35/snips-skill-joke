#!/usr/bin/env python3
# coding: utf-8

import requests

r = requests.get('https://blague.xyz/joke/random')
joke = r.json().get('joke')

print(joke)