import requests
url="https://official-joke-api.appspot.com/random_joke"
response=requests.get(url)
if response.status_code==200:
    joke=response.json()
    print("random joke")
    print("-"*30)
    print("setup:",joke["setup"])
    print("punchline:",joke["punchline"])
else:
    print("failed to fetch joke")