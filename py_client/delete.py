import requests
from getpass import getpass

endpoint = "http://localhost:8000/api/auth/"
username = input("Enter username : ")
password = getpass()
get_response = requests.post(endpoint,
                             json={"username": username,"password":password})

if get_response.status_code == 200:
    i = input("Enter the id of post to be deleted : ")
    endpoint = f"http://localhost:8000/api/products/{i}/delete/"
    token = get_response.json()['token']
    header = {
        "Authorization" : f"Token {token}"
    }
    get_response = requests.delete(endpoint,headers=header)
    print(f'Entry no {i} deleted succesfully')
