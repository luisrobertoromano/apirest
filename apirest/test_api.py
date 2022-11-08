import requests
api_url = "http://127.0.0.1:8000/api/lista"
response = requests.get(api_url)
print(response.json())