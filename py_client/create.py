import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title":"Ketti data",
    "price": 9824787,
    "content":"Bluhuhaha"
}

get_response = requests.post(endpoint,json=data)
print(get_response.json())