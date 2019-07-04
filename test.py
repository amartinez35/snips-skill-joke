import requests

r = requests.get('https://blague.xyz/joke/random')
joke = r.json().get('joke')

print(joke)