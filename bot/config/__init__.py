pizzasTemplates = [
    'I love {} pizza',
    'Ooh yea, {}, the taste is so good',
    '{} is my favorite pizza',
    'You say no more about that horrible pizza',
]

feelingsTemplates = [
    'What exactly do you {} about it?',
    'Tell me more about it',
    'Oh, I know that feeling...'
]

questionTemplate = [
    'Why are you asking?',
    'Do you think I know everything?',
    'I`m not really sure about that',
    'I think it`s better to ask Google'
]

missTemplates = [
    'I don\'t understand you. Try to talk about pizza...',
    'What\'s the matter with it'
]

totalDict = {
    'margherita': pizzasTemplates,
    'chicago': pizzasTemplates,
    'greek': pizzasTemplates,
    'new-york': pizzasTemplates,
    'sicilian': pizzasTemplates,
    'california': pizzasTemplates,
    'carbonara': pizzasTemplates,
    'prosciutto': pizzasTemplates,
    'gorgonzola': pizzasTemplates,
    'francescana': pizzasTemplates,
    'mimosa': pizzasTemplates,
    'bbq': pizzasTemplates,
    'barbeque': pizzasTemplates,

    'love': feelingsTemplates,
    'prefer': feelingsTemplates,
    'like': feelingsTemplates,
    'enjoy': feelingsTemplates,
    'hate': feelingsTemplates,
    'dislike': feelingsTemplates,

    'is': questionTemplate,
    'are': questionTemplate,
    'do': questionTemplate,
    'does': questionTemplate,
    'why': questionTemplate,
    'what': questionTemplate,
    'where': questionTemplate,
    'when': questionTemplate,
    'how': questionTemplate,
    '?': questionTemplate,

    'want': ['Have you tried BBQ pizza'],
    'pizza': ['I love pizza']
}
