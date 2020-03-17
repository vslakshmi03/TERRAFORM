import requests
url = 'https://en.wikipedia.org/wiki/Flower#/media/File:Flower_poster_2.jpg'
file = requests.get(url, allow_redirects=True)
open('flower.jpg', 'wb').write(file.content)
