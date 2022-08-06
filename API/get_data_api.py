import requests

response = requests.get('http://127.0.0.1:5000/api/students/all')
print(response.json())