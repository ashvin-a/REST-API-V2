import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title":"Testing blah",
    "price": 9824787,
    "content": None
}

get_response = requests.post(endpoint,json=data)
print(get_response.json())