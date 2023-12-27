import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"
username = input("Enter username : ")
password = getpass()
get_response = requests.post(
    endpoint,
    json={"username": username, "password": password},
)
if get_response.status_code == 200:
    i = input("Enter id of entry to update: ")
    endpoint = f"http://localhost:8000/api/products/{i}/update/"

    token = get_response.json()["token"]
    header = {"Authorization": f"Token {token}"}

    data = {
        "title": "Work aavum goys(updated)",
        "price": 420420,
        "email": "blah@lskdj.com",
    }

    get_response = requests.put(endpoint, headers=header, json=data)
    print(get_response.json())
