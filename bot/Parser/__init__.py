import random
import re
from ..config import totalDict, keyWords, questionTemplate, missTemplates, changeThemeTemplates, \
    adjectives, adverbsOfTime, futureAdverbs, pastAdverbs

used: set = {""}
usedSetChangeSubject: set = {""}


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


def check_combinations(formattedComb: str):
    for adjective in adjectives:
        if (formattedComb.find('i feel ' + adjective) != -1) \
                or (formattedComb.find('i am ' + adjective) != -1):
            return f'Why do you feel {adjective}?'
    for adverbOfTime in adverbsOfTime:
        if (formattedComb.find(adverbOfTime) != -1) and (adverbOfTime in futureAdverbs):
            return 'Interesting! Tell me more! What else is going to happen ' + adverbOfTime + '?'
        elif (formattedComb.find(adverbOfTime) != -1) and (adverbOfTime in pastAdverbs):
            return 'What else happened ' + adverbOfTime + '?'
        elif (formattedComb.find(adverbOfTime) != -1) and (adverbOfTime == 'today'):
            return 'What else happened today?'

    if formattedComb in totalDict:
        return random.choice([i if i not in used else '' for i in totalDict[formattedComb]["array"]])

    return ''


def parse_sentence(sentence: str):
    # adds to dictionary all combinations of keyValues and *
    sentence = sentence.replace('?', ' ?')
    sentence = sentence.replace(',', '')
    sentence = sentence.replace('.', '')

    # split the sentence into words
    wordList = sentence.lower().split(" ")

    if '?' in wordList:
        return random.choice(questionTemplate)

    formattedComb = sentence_transformation(wordList)
    answer = check_combinations(formattedComb)

    if answer != '':
        used.add(answer)
        return answer.format(formattedComb)

    priority = -1
    # otherwise returns related template
    for word in wordList:
        try:
            template = random.choice([i if i not in used else None for i in totalDict[word]["array"]])
            if totalDict[word]["priority"] > priority:
            # used.add(template.format(word))
                answer = template.format(word)
            # return template.format(word)
        except KeyError:
            continue
        #     this except means there is no unused templates
        except AttributeError:
            used.clear()
            answer = random.choice([i if i not in used else None for i in changeThemeTemplates["array"]])
            usedSetChangeSubject.add(answer)
            if len(usedSetChangeSubject) == len(changeThemeTemplates["array"]):
                usedSetChangeSubject.clear()
            return answer
    print(priority, answer)
    if answer != '':
        used.add(answer)
        return answer
    else:
        return random.choice(missTemplates)
