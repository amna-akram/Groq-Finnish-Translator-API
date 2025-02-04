import requests

response = requests.post('http://127.0.0.1:5000/translate', json={'text': 'Hello, how are you?'})
print(response.json())
