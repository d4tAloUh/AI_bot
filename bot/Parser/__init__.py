import random
from ..config import totalDict, keyWords, questionTemplate, missTemplates, changeThemeTemplates, \
    adjectives, adverbsOfTime, futureAdverbs, pastAdverbs

used: set = {""}
usedSetChangeSubject: set = {""}


def sentence_transformation(wordList):
    formatted = []
    for word in wordList:
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

    if formattedComb in totalDict:
        return random.choice([i if i not in used else None for i in totalDict[formattedComb]])

    return ''


def parse_sentence(sentence: str):
    # remove ./, from sentence and add space to question mark
    sentence = sentence.replace('?', ' ?')
    sentence = sentence.replace(',', '')
    sentence = sentence.replace('.', '')

    # split the sentence into words
    wordList = sentence.lower().split(" ")

    if len(wordList) < 2:
        return "I want to hear more from you..."

    if '?' in wordList:
        return random.choice(questionTemplate)

    formattedComb = sentence_transformation(wordList)
    answer = check_combinations(formattedComb)

    if answer != '' and answer is not None:
        used.add(answer)
        return answer.format(formattedComb)

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
            used.clear()
            answer = random.choice([i if i not in used else None for i in changeThemeTemplates])
            usedSetChangeSubject.add(answer)
            if len(usedSetChangeSubject) == len(changeThemeTemplates):
                usedSetChangeSubject.clear()
            return answer

    return random.choice(missTemplates)
