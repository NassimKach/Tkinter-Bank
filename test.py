import json


dyData = {
    "ne": "dy",
    "age": 18,
    "hobby": ["sing", "dance", "basketball"],
    "color": ["red", "blue", "green"]
}

with open("data\\agent.json", 'r') as f:
    agent = json.load(f)


with open("data\\clients.json", 'w') as out_file:
    json.dump(dyData, out_file, indent=2)
