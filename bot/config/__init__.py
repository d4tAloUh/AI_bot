pizzasTemplates = [
    'I love {} pizza',
    'Ooh yea, {}, the taste is so good',
    '{} is my favorite pizza',
    'You say no more about that horrible pizza',
]

feelingsTemplates = [
    'What exactly do you {} about it?',
    'Tell me more about it',
    'Oh, I know that feeling...',
    'I have the same feeling as you, believe me 🤥',
    'You should speak about it to some of your friend, not me 🥴',
    'I am not your personal psychologist, i will be only if you pay me some cash 💵'
]

questionTemplate = [
    'Why are you asking?',
    'Do you think I know everything?',
    'I`m not really sure about that',
    'I think it`s better to ask Google',
    'What do you mean by that?',
    'That\'s a tough question 🧐',
    'To be honest, you should ask this someone smarter than me 🤪',
    'I am pretty dumb ass, and I don\'t know the answer :) ',
    'You are just like Neznayka 😁',
    'Use BING searcher for that 😋'
]

suggestionsTemplates = [
    'Have you tried BBQ pizza?',
    'Have you tried Mimosa pizza?',
    'Have you tried California pizza?',
    'I think you might like Chicago pizza',
    'Try any pizza with mushrooms. It`s considered to be the second best topping in the world!',
    'What about topping with black olives?'
]

adjectiveTemplates = [
    'Mmm... couldn`t agree more. Is there any pizza you think is overrated?',
    'That`s true! What do you think about pizzas with pineapple in it?',
    'I also think that! Do you know that the best pizza in the world is considered to be Pepperoni?',
    'Absolutely disagree. Maybe our opinions will coincide on another thing.',
    'We are of one mind! Btw, fun fact: the word pizza dates back to 997 CE.'
]

greetingTemplates = [
    'Oh hi there!',
    'Greetings!',
    'It`s nice to see you!',
]

missTemplates = [
    'I don\'t understand you',
    'What`s the matter with that',
    "Try to specify the subject",
    "Does that really matter?",
    'You sound strange, are you drunk? Say it again 😏',
    'It is definitely not what you should tell me, I am not qualified enough to have any opinion on what you just said 🤫',
    'Do you speak english good enough? Try it in other words',
    'I’m probably not the best person to ask for that information😟',
    'That requires a bit more research first. By the way, what\'s your favorite pizza?',
    'I\'ll get back to you on that ✉️',
    'I\'ll send you an email later on that',
    'Tell me more about it 😈',
    'I want to hear more about this',
    'I\'ll call you later about that 📱'
    # 'Do you know that americans eat approximately 350 slices per second? Crazy, isn`t it?',
    # 'Fun fact: 36% of all pizza orders want their pizza topped with pepperoni.',
    # 'Btw, over 5 billion pizzas are sold worldwide each year.',
    # 'Do you know that October has been celebrated as National Pizza month since 1987?',
    # 'Fun fact: Women are more likely to order vegetarian options as opposed to men.'
]

confidenceTemplates = [
    'Are you sure about that?',
    'Do you doubt that?',
]

totalDict = {
    'margarita': pizzasTemplates,
    'chicago': pizzasTemplates,
    'greek': pizzasTemplates,
    'new-york': pizzasTemplates,
    'sicilian': pizzasTemplates,
    'california': pizzasTemplates,
    'carbonara': pizzasTemplates,
    'prosciutto': pizzasTemplates,
    'gorgonzola': pizzasTemplates,
    'francesca': pizzasTemplates,
    'mimosa': pizzasTemplates,
    'bbq': pizzasTemplates,
    'barbeque': pizzasTemplates,

    'love': feelingsTemplates,
    'prefer': feelingsTemplates,
    'like': feelingsTemplates,
    'enjoy': feelingsTemplates,
    'hate': feelingsTemplates,
    'dislike': feelingsTemplates,

    'pizza': ['I love pizza. Let`s talk about it!'],

    'recommend': suggestionsTemplates,
    'recommended': suggestionsTemplates,
    'suggest': suggestionsTemplates,
    'suggested': suggestionsTemplates,
    'want': suggestionsTemplates,
    'wanted': suggestionsTemplates,
    'advise': suggestionsTemplates,
    'advised': suggestionsTemplates,

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

    'good': adjectiveTemplates,
    'great': adjectiveTemplates,
    'amazing': adjectiveTemplates,
    'awesome': adjectiveTemplates,
    'best': adjectiveTemplates,
    'favourite': adjectiveTemplates,
    'delicious': adjectiveTemplates,
    'breathtaking': adjectiveTemplates,
    'tasty': adjectiveTemplates,
    'mouth-watering': adjectiveTemplates,
    'appetizing': adjectiveTemplates,
    'flavoursome': adjectiveTemplates,
    'delectable': adjectiveTemplates,
    'disgusting': adjectiveTemplates,
    'awful': adjectiveTemplates,
    'terrible': adjectiveTemplates,
    'tasteless': adjectiveTemplates,
    'horrific': adjectiveTemplates,
    'bad': adjectiveTemplates,

    "hello": greetingTemplates,
    "hi": greetingTemplates,
    "greetings": greetingTemplates,
    "morning": greetingTemplates,
    "afternoon": greetingTemplates,
    "evening": greetingTemplates,
    "howdy": greetingTemplates,

    "maybe": confidenceTemplates,
    "definitely": confidenceTemplates,
    'certain': confidenceTemplates,
    'probably': confidenceTemplates,
    'might': confidenceTemplates,
    'perhaps': confidenceTemplates,
    'possible': confidenceTemplates,
    'likely': confidenceTemplates

}
