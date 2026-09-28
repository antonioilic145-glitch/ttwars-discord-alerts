import requests

url = "https://www.ttwars.com/international/calendar"

response = requests.get(url, timeout=20)

print("STATUS:", response.status_code)
print("LENGTH:", len(response.text))
print(response.text[:1000])
