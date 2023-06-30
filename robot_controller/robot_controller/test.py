import json

with open('../../../arquivo.json', 'r') as f:
    file = json.load(f)
    print(file["read"])
