import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit

response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
with open(f"{sys.argv[1]}.json", "w") as file:
    file.write(json.dumps(response.json(), indent=2))