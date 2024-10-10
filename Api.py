import requests

api_url = 'https://api.giphy.com/v2/emoji?api_key=xBR3N15OwGA4RgIu9R1gTp2Hdcw1l9uN&limit=25&offset=0'
api_key = 'mykey'

headers = {
    'Authorization': 'Bearer ' + api_key
}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)