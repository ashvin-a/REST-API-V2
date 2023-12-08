import requests

endpoint = "http://localhost:8000/api/products/7/update/"

data = {
    "title": "Work aavum goys(updated)",
    "price": 420420,
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
