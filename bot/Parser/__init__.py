import random
import re
from ..config import keyWords, totalDict, questionTemplate, missTemplates

'''
1. check if key exists in sentence -> " i dont understand you"
2. get type of key
3. get collection of type
4. get template string
'''


def sentence_transformation(wordList):
    formatted = []
    for i, word in enumerate(wordList):
        if word in keyWords:
            formatted.append(word)
        elif len(formatted) > 0 and formatted[len(formatted) - 1] == "*":
                continue
        else:
            formatted.append("*")
    return ' '.join(formatted)


def parse_sentence(sentence: str):
    sentence = sentence.replace('?', ' ?')
    # split the sentence into words
    wordList = sentence.lower().split(" ")
    if '?' in wordList:
        return random.choice(questionTemplate)
    return random.choice(totalDict[sentence_transformation(wordList)])

    # for word in wordList:
    #     try:
    #         template = random.choice(totalDict[word])
    #         return template.format(word)
    #         # return template.format(word.capitalize())
    #     except KeyError:
    #         continue
    return random.choice(missTemplates)
