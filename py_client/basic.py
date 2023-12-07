import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint,json={"blah":"work aavumo gooys?"})
print(get_response.json())
