import random

from ..config import totalDict, pizzasTemplates

'''
1. check if key exists in sentence -> " i dont understand you"
2. get type of key
3. get collection of type
4. get template string
'''


def parse_sentence(sentence: str):
    template = ''
    for word in sentence.split(" "):
        try:
            template = random.choice(totalDict[word])
            return template.format(word)
        except KeyError:
            continue
    return "i dont understand you"
