import json


with open("words.txt", "r") as f:
    data = f.readlines()

words = [w.strip() for w in data if len(w.strip()) == 5]

with open("dict.json", "w") as f:
    json.dump(words, f)
