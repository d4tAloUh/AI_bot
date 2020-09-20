pizzasTemplates = [
    'I love {} pizza',
    'Ooh yea, {}, the taste is so good',
    '{} is my favorite pizza',
    'You say no more about that horrible pizza',
]

changeThemeTemplates = [
    # 'Have you ever thought about, why we enjoy eating?',
    'Whatever. By the way, do you like pizza? Which one is your favourite?',
    # 'I think you have something on your face. I almost forgot to ask you whether you have any dog? Cause i want one but can not decide on breed 🐶',
    'Please, let\'s change topic of our conversation. Maybe lets talk about pizza? Margarita is my favourite :)',
    'I dont want to talk about that. How is your family doing?',
    # 'I hate talking about that. Tell me about your programming skills more 🧑‍💻👩‍💻',
    'Please, let\'s change the direction of our conversation. Tell me about your best friend.',
    'Dont want to talk about that for now, tell me about how is your job doing?',
    # 'Thats a taboo topic. You should better tell me more about your relationships 💞.',
    # 'This is off-limits. Do you think Trump is going to become a president for the second time and why?',
    'What about the weather? Is it quite sunny today?',
    'Btw, do you like running?',
    'By the by, I want to try a new recipe today, do you have any suggestions?',
    # 'Apart from that, your English sounds really professional! Where did you earn that skill?',
    'Aside, i`m planning on watching a film tonight? Any recommendations?',
    'Btw, is there anything you particularly enjoy doing these days?',
    # 'By the by, what are your plans for the weekends?',
    # 'Apart from that, I really believe it would be better if you studied now rather than chatted with me...?',
    'Aside, do you love travelling?'
]

feelingsTemplates = [
    'What exactly do you {} about it?',
    'What else do you {} ?'
    'Tell me more about it',
    # 'Oh, I know that feeling...',
    # 'I have the same feeling as you, believe me 🤥',
    # 'You should speak about it to some of your friend, not me 🥴',
    # 'I am not your personal psychologist, i will be only if you pay me some cash 💵'
]

questionTemplate = [
    'Why are you asking?',
    # 'Do you think I know everything?',
    'I`m not really sure about that',
    'I think it`s better to ask Google',
    'What do you mean by that?',
    # 'That\'s a tough question 🧐',
    # 'To be honest, you should ask this someone smarter than me 🤪',
    # 'I am pretty dumb ass, and I don\'t know the answer :) ',
    # 'You are just like Neznayka 😁',
    'Use BING searcher for that 😋'
]

suggestionsTemplates = [
    'Dou you really need my opinion? I think you should know this much better 😊',
    'Maybe you don\'t need it at all? Go and have a bottle of beer. 🍺',
    'I am not a part of you, don\'t ask me for help, i am too busy for that 🙄.',
    'Am i your personal adviser? I dont remember when you paid me last time 🤑',
    'I don\'t think you can afford that 💸'
]

adjectiveTemplates = [
    'Why is it {} ?'
    'Mmm... couldn`t agree more. Is it really {} ?',
    # 'That`s true! But i have friends that would not agree on that.',
    # 'I also think that! But my family thinks that I am dumb, because i have these opinion.',
    # 'Absolutely disagree. Maybe our opinions will coincide on another thing.',
    # 'We are of one mind!',
    # 'I think you are not ordinary.',
    'Why you have such opinion ?',
    'What made you think so?',
    # 'That\'s a negative'
]

greetingTemplates = [
    'Oh hi there! How do you feel today?',
    'Greetings! How are you?',
    'Do we know each other?',
    'Oh, hy dear! You look much better than the last time I saw you 🙈',
    'Hello beauty! How are you?',
    'Hi pretty human being! How do you feel today?',
    'Hello darling! How do you feel today?',
    'You look stunning today!',
    'Haven`t heard from you for a while.. How is it going?'
]

missTemplates = [
    'I don\'t understand you',
    'What`s the matter with that',
    "Try to specify the subject",
    "Does that really matter?",
    # 'I am not qualified enough to have any opinion on what you just said 🤫',
    'That requires a bit more research first. By the way, what\'s your favorite pizza?',
    'Tell me more about it 😈',
    # 'I want to hear more about this',
    'The weather is nice today, isn`t it?',
    'Let`s talk about something else..',
    'I think you can be more specific',
]

confidenceTemplates = [
    # 'Why are you {}'
    'Are you sure about that?',
    'Do you doubt that?',
    # 'Why are you so sure about that? 🤨',
    'Does it really matter?',
    'I dont think so, but whatever. Tell me what\'s your favorite pizza?',
    # 'My mommy doesn\'t think so',
    # 'Nice to hear it, but i would doubt that 😏',
    # 'Ok boss!',
    # 'Well i think that... Ok, whatever...',
    # 'Doesn\'t matter for me 😉',
    # 'Glad to hear that. (no)'
]

agreeTemplates = [
    'Wow! Me too! Let`s talk about it!',
    'Can`t agree more!',
    'That`s great!'
]

welcomeTemplates = [
    'No worries! Let`s talk about something else! Do you like pizza?',
    'Your welcome! Let`s talk about something else! What do you like?',
    'Let`s talk about something else! Do you like dancing?',
    'Let`s talk about something else! Is there something you hate?',
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
    'barbecue': pizzasTemplates,

    'pizza': ['I love pizza. Let`s talk about it!'],

    'recommend': suggestionsTemplates,
    'recommended': suggestionsTemplates,
    'suggest': suggestionsTemplates,
    'suggested': suggestionsTemplates,
    'want': suggestionsTemplates,
    'wanted': suggestionsTemplates,
    'advise': suggestionsTemplates,
    'advised': suggestionsTemplates,

    'how about': suggestionsTemplates,
    'what about': suggestionsTemplates,

    '* love *': feelingsTemplates,
    'i love *': agreeTemplates,

    'love':feelingsTemplates,
    'prefer': feelingsTemplates,
    'like': feelingsTemplates,
    'enjoy': feelingsTemplates,
    'hate': feelingsTemplates,
    'dislike': feelingsTemplates,

    'is * ?': questionTemplate,
    'are * ?': questionTemplate,
    'do * ?': questionTemplate,
    'does * ?': questionTemplate,
    'why * ?': questionTemplate,
    'what * ?': questionTemplate,
    'where * ?': questionTemplate,
    'when * ?': questionTemplate,
    'how * ?': questionTemplate,
    '?': questionTemplate,

    '* is * ?': questionTemplate,
    '* are * ?': questionTemplate,
    '* do * ?': questionTemplate,
    '* does * ?': questionTemplate,
    '* why * ?': questionTemplate,
    '* what * ?': questionTemplate,
    '* where * ?': questionTemplate,
    '* when * ?': questionTemplate,
    '* how * ?': questionTemplate,
    '* ?': questionTemplate,

    'is': questionTemplate,
    'are': questionTemplate,
    'do': questionTemplate,
    'does': questionTemplate,
    'why': questionTemplate,
    'what': questionTemplate,
    'where': questionTemplate,
    'when': questionTemplate,
    'how': questionTemplate,

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
    'likely': confidenceTemplates,

    'no': confidenceTemplates,
    'yes': confidenceTemplates,

    'of course': confidenceTemplates,
    'for sure': confidenceTemplates,
    'no doubt': confidenceTemplates,
    '* doubt *': confidenceTemplates,
    'i doubt *': confidenceTemplates,
    'i doubt that': confidenceTemplates,
    'not sure': confidenceTemplates,
    'true': confidenceTemplates,
    'that`s true': confidenceTemplates,
    'thats true': confidenceTemplates,

    'thank you': welcomeTemplates,
    'thanks': welcomeTemplates,

    'how are you': ['Fine, thanks for asking. Let`s talk about something else! What`s the weather like today?'],
}

# adverbs
pastAdverbs = ['yesterday', 'a year ago', 'a while ago', 'last week', 'before', 'early', 'earlier']
futureAdverbs = ['tomorrow', 'next year', 'later', 'tonight', 'next']
adverbsOfTime = pastAdverbs + futureAdverbs + ['today', 'now']

# verbs
emotionVerbs = ['feel', 'love', 'prefer', 'like', 'enjoy', 'hate', 'dislike', ]
verbs = emotionVerbs + ['recommend', 'suggest', 'want', 'want', 'advise', 'is', 'are', 'do', 'does']

# adjectives
adjectives = [
    'good', 'great', 'amazing', 'awesome', 'best', 'favourite', 'delicious', 'breathtaking', 'tasty', 'mouth-watering',
    'appetizing', 'flavoursome', 'delectable', 'disgusting', 'awful', 'terrible', 'tasteless', 'horrific', 'bad', 'sad',
    'disappointed'
]

questionWords = ['why', 'what', 'where', 'when', 'how',
                 'is', 'are', 'do', 'does', '?']

keyWords = verbs + adjectives + adverbsOfTime + questionWords + [
    'pizza', 'i', 'you', 'yes', 'no', 'thank', 'thanks',
    "hello", "hi", "greetings", "morning", "afternoon", "evening", "howdy",
    "maybe", "definitely", 'certain', 'probably', 'might', 'perhaps', 'possible', 'likely',
]
