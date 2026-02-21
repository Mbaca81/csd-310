import requests

print("=== Testing Connection to PokéAPI ===")

# Test basic connection
url = "https://pokeapi.co/api/v2/pokemon/charizard"
response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Connection successful!\n")
else:
    print("Connection failed.\n")

# ---------------------------------------------------
# Print RAW response (no formatting)
# ---------------------------------------------------

print("=== Raw Response ===")
print(response.text)

# ---------------------------------------------------
# Print FORMATTED response (clean output)
# ---------------------------------------------------

if response.status_code == 200:
    data = response.json()

    print("\n=== Formatted Output ===")
    print(f"Name: {data['name'].capitalize()}")
    print(f"ID: {data['id']}")
    print(f"Height: {data['height']}")
    print(f"Weight: {data['weight']}")

    print("Abilities:")
    for ability in data['abilities']:
        print("-", ability['ability']['name'])
else:
    print("Could not retrieve Pokémon data.")