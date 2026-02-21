import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\nThere are", data["number"], "people in space right now.\n")

    for person in data["people"]:
        print(f"{person['name']} is aboard {person['craft']}")
else:
    print("Failed to retrieve astronaut data.")