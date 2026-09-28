import requests

url = "https://www.ttwars.com/international/calendar"

response = requests.get(url, timeout=20)

print("STATUS:", response.status_code)
print("LENGTH:", len(response.text))

for line in response.text.splitlines():
    low = line.lower()
    if any(x in low for x in ["api", "calendar", "event", ".json", "script"]):
        print(line[:1000])
