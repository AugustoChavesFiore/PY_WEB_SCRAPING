
import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

for post in data:
    print(post['title'])
    print(post['body'])
    print()