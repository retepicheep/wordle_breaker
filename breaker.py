import json
from random import randint

data = json.load(open("dict.json"))

def get_word():
    wordnum = randint(len(data))
    print(data.index(wordnum)

get_word()

