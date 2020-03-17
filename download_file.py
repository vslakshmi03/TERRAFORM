import requests
url = 'https://readthedocs.org/projects/python-guide/downloads/pdf/latest/'
file = requests.get(url, allow_redirects=True)
open('c:/users/LikeGeeks/documents/hello.pdf', 'wb').write(file.content)

