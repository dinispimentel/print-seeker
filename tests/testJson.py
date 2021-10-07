import json
ft = []

with open('../config/keywords.json') as f:
    ft = json.load(f)

print(ft[0])

