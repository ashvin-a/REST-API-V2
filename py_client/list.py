import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"
username = input("Enter username : ")
password = getpass()
get_response = requests.post(endpoint,
                             json={"username": username,"password":password})

if get_response.status_code == 200:
    endpoint = "http://localhost:8000/api/products/"
    token = get_response.json()['token']
    header = {
        "Authorization" : f"Token {token}"
    }
    get_response = requests.get(endpoint,headers=header)
    print(get_response.json())