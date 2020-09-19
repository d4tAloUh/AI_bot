import random
import re
from ..config import totalDict, questionTemplate, missTemplates, changeThemeTemplates

'''
1. check if key exists in sentence -> " i dont understand you"
2. get type of key
3. get collection of type
4. get template string
'''
used: set = {""}
usedSetChangeSubject: set = {""}


def parse_sentence(sentence: str):
    sentence = sentence.replace('?', ' ?')
    # split the sentence into words
    wordList = sentence.lower().split(" ")
    if '?' in wordList:
        return random.choice(questionTemplate)
    for word in wordList:
        try:
            template = random.choice([i if i not in used else None for i in totalDict[word]])
            used.add(template.format(word))
            return template.format(word)
            # return template.format(word.capitalize())
        except KeyError:
            continue
        #     this except means there is no unused templates
        except AttributeError:
            answer = random.choice([i if i not in used else None for i in changeThemeTemplates])
            usedSetChangeSubject.add(answer)
            if len(usedSetChangeSubject) == len(changeThemeTemplates):
                usedSetChangeSubject.clear()
            return answer

    return random.choice(missTemplates)
