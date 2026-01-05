import requests


## Making a POST request to the simple starting app

response = requests.post("http://localhost:8003/create_book/", json={"title": "7 Habits of Highly Effective People", "author": "Stephen R. Covey"})
# print(response.json())
