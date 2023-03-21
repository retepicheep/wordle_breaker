import json
from random import randint, choice

data = json.load(open("dict.json"))
# words = list(data.items())

def get_word():
    word = choice(data)
    return word

get_word()

