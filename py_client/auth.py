import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"

password = getpass()
get_response = requests.post(endpoint, json={"username": "root", "password": password})
print(get_response.json())
