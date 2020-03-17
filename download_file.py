#In this code, the first step we specify the URL. Then we use the get method of the requests module to fetch the URL. In the get method, we set the allow_redirects to True which will allow redirection in the URL and the content after redirection will be assigned to the variable myfile. Finally, we open a file to write the fetched content.
import requests
url = 'https://readthedocs.org/projects/python-guide/downloads/pdf/latest/'
file = requests.get(url, allow_redirects=True)
open('c:/users/LikeGeeks/documents/hello.pdf', 'wb').write(file.content)

