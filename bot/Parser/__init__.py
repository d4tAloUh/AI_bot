import random
import re
from ..config import totalDict, keyWords, questionTemplate, missTemplates, changeThemeTemplates, \
    adjectives, emotionVerbs, adverbsOfTime, futureAdverbs, pastAdverbs, questionWords

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
    for questionWord in questionWords:
        if formattedComb.find(questionWord) != -1:
            return random.choice(questionTemplate)

    for verb in emotionVerbs:
        if formattedComb.find('i ' + verb) != -1:
            return 'What else do you ' + verb + '?'

    for adverbOfTime in adverbsOfTime:
        if (formattedComb.find(adverbOfTime) != -1) and (adverbOfTime in futureAdverbs):
            return 'Interesting! Tell me more! What else is going to happen ' + adverbOfTime + '?'
        elif (formattedComb.find(adverbOfTime) != -1) and (adverbOfTime in pastAdverbs):
            return 'What else happened ' + adverbOfTime + '?'
        elif (formattedComb.find(adverbOfTime) != -1) and (adverbOfTime == 'today'):
            return 'What else happened today?'

    for adjective in adjectives:
        if formattedComb.find('i feel ' + adjective) != -1:
            return 'Why do you feel ' + adjective + '?'
        elif (formattedComb.find('is ' + adjective) != -1) \
                or (formattedComb.find('are  ' + adjective) != -1) \
                or (formattedComb.find('be  ' + adjective) != -1):
            return 'Why do you think that`s' + adjective + '?'

    if formattedComb in totalDict:
        return random.choice(totalDict[formattedComb])

    return ''


def parse_sentence(sentence: str):
    # adds to dictionary all combinations of keyValues and *
    sentence = sentence.replace('?', ' ?')

    # split the sentence into words
    wordList = sentence.lower().split(" ")
    if '?' in wordList:
        return random.choice(questionTemplate)

    formattedComb = sentence_transformation(wordList)
    print(formattedComb)
    answer = check_combinations(formattedComb)
    print(answer)
    if answer != '':
        return answer

    # otherwise returns related template
    for word in wordList:
        try:
            template = random.choice([i if i not in used else None for i in totalDict[word]])
            used.add(template.format(word))
            return template.format(word)
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
