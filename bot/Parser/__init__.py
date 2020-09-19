import random
import re
from ..config import totalDict, pizzasTemplates, missTemplates

'''
1. check if key exists in sentence -> " i dont understand you"
2. get type of key
3. get collection of type
4. get template string
'''


def parse_sentence(sentence: str):
    # leave only words, remove every special character
    cleanSentence = re.sub('\W+', ' ', sentence)
    # split the sentence into words
    wordList = cleanSentence.lower().split(" ")
    for word in wordList:
        try:
            template = random.choice(totalDict[word])
            return template.format(word.capitalize())
        except KeyError:
            continue
    return random.choice(missTemplates)
