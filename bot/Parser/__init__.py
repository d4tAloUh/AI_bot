import random

from ..config import totalDict, pizzasTemplates, missTemplates

'''
1. check if key exists in sentence -> " i dont understand you"
2. get type of key
3. get collection of type
4. get template string
'''


def parse_sentence(sentence: str):
    template = ''
    sentence = sentence.lower().split(" ")
    stopWords = []
    sentence = [i for i in sentence if not i in stopWords]
    for word in sentence:
        try:
            template = random.choice(totalDict[word])
            return template.format(word.capitalize())
        except KeyError:
            continue
    return random.choice(missTemplates)
