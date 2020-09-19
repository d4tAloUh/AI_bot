import random
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
    # adds to dictionary all combinations of keyValues and *
    sentence = sentence.replace('?', ' ?')

    # split the sentence into words
    wordList = sentence.lower().split(" ")
    # if '?' in wordList:
    #     return random.choice(questionTemplate)

    # checks whether there is a given combination in dictionary
    # -> if not returns one of  missing templates
    formattedComb = sentence_transformation(wordList)
    if not (formattedComb in totalDict):
        return random.choice(missTemplates)

    # otherwise returns related template
    return random.choice(totalDict[formattedComb])


    # previous code

    # for word in wordList:
    #     try:
    #         template = random.choice(totalDict[word])
    #         return template.format(word)
    #         # return template.format(word.capitalize())
    #     except KeyError:
    #         continue
    # return random.choice(missTemplates)
