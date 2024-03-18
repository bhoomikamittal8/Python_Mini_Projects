import requests
import json

# api_key = '33e89693458d47b58f5163254241703'

city = input("Enter city: ")

url = requests.get(f"https://api.weatherapi.com/v1/current.json?key=33e89693458d47b58f5163254241703&q={city}")

print(url.text)
w_dic = json.loads(url.text)


