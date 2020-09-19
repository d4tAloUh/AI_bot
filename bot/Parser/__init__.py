import random

from ..config import totalDict, pizzasTemplates, missTemplates

'''
1. check if key exists in sentence -> " i dont understand you"
2. get type of key
3. get collection of type
4. get template string
'''


def parse_sentence(sentence: str):
    sentence = sentence.lower().split(" ")
    for word in sentence:
        try:
            template = random.choice(totalDict[word])
            return template.format(word.capitalize())
        except KeyError:
            continue
    return random.choice(missTemplates)
