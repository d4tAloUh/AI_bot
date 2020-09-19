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

suggestionsTemplates = [
    'Have you tried BBQ pizza?',
    'Have you tried Mimosa pizza?',
    'Have you tried California pizza?',

]

missTemplates = [
    'I don\'t understand you. Try to talk about pizza...',
    'Do you know that americans eat approximately 350 slices per second? Crazy, isn`t it?',
    'Fun fact: 36% of all pizza orders want their pizza topped with pepperoni.',
    'Btw, over 5 billion pizzas are sold worldwide each year.',
    'Do you know that October has been celebrated as National Pizza month since 1987?',
    'Fun fact: Women are more likely to order vegetarian options as opposed to men.'
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

    'recommend': suggestionsTemplates,
    'recommended': suggestionsTemplates,
    'suggest': suggestionsTemplates,
    'suggested': suggestionsTemplates,
    'want': suggestionsTemplates,
    'wanted': suggestionsTemplates,
    'advise': suggestionsTemplates,
    'advised': suggestionsTemplates,

    'pizza': ['I love pizza']
}
