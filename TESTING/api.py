import requests

API_URL = "your-prefered-model-url"
API_KEY = "your-api-key"
headers = {
    "Authorization": f"Bearer {API_KEY}",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

response = query({
    "inputs": "What is 1+1?"
})

print(response)
