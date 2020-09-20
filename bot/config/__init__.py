pizzasTemplates = [
    'I love {} pizza',
    'Ooh yea, {}, the taste is so good',
    '{} is my favorite pizza',
    'You say no more about that horrible pizza',
]

changeThemeTemplates = [
    'Have you ever thought about, why we enjoy eating?'
]

feelingsTemplates = [
    'What exactly do you {} about it?',
    'What else do you {}'
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

changeTopicTemplates = [
    'What about the weather? Is it quite sunny today?',
    'Btw, do you like running?',
    'By the by, I want to try a new recipe today, do you have any suggestions?',
    'Apart from that, your English sounds really professional! Where did you earn that skill?',
    'Aside, i`m planning on watching a film tonight? Any recommendations?',
    'Btw, is there anything you particularly enjoy doing these days?',
    'By the by, what are your plans for the weekends?',
    'Apart from that, I really believe it would be better if you studied now rather than chatted with me...?',
    'Aside, do you love travelling?',
]

greetingTemplates = [
    'Oh hi there!',
    'Greetings!',
    'It`s nice to see you!',
    'Again you? You should not be there',
    'Do we know each other?',
    'Do i know you?',
    'Nice to meet you',
    'Halo!',
    'I missed you!',
    'Oh, hy dear! You look much better than the last time I saw you 🙈',
    'Wow, what a strange voice transformation you have, i havent heard you just for a little',
    'Hi again, i hope next time we will not meet each other 😣',
    'Hello beauty!',
    'Hi pretty human being',
    'Hello darling!',
    'Hi gorgeous!',
    'Ciao!',
    'You look stunning today!',
    'Haven`t heard from you for a while.. How is it going?'
]

missTemplates = [
    'I don\'t understand you',
    'What`s the matter with that',
    "Try to specify the subject",
    "Does that really matter?",
    'You sound strange, are you drunk? Say it again 😏',
    'I am not qualified enough to have any opinion on what you just said 🤫',
    'Do you speak english good enough? Try it in other words',
    'I’m probably not the best person to ask for that information😟',
    'That requires a bit more research first. By the way, what\'s your favorite pizza?',
    'I\'ll get back to you on that ✉️',
    'I\'ll send you an email later on that',
    'Tell me more about it 😈',
    'I want to hear more about this',
    'I\'ll call you later about that 📱'
    'The weather is nice today, isn`t it?',
    'Let`s talk about something else.. Tell me about your day',
    'I think you can be more specific',
]

confidenceTemplates = [
    'Are you sure about that?',
    'Do you doubt that?',
    'Why are you so sure about that? 🤨',
    'Does it really matter?',
    'I dont think so, but whatever. Tell me what\'s your favorite pizza? I would like to cook it 🍕',
    'My mommy doesn\'t think so',
    'Nice to hear it, but i would doubt that 😏',
    'Ok boss!',
    'Well i think that... Ok, whatever...',
    'Doesn\'t matter for me 😉',
    'Glad to hear that. (no)'
]

agreeTemplates = [
    'Wow! Me too! Let`s talk about it!',
    'Can`t agree more!',
    'That`s great!'
]

welcomeTemplates = [
    'Your welcome! Let`s talk about something else! What`s your favourite meal?',
    'No worries! Let`s talk about something else! Do you like pizza?',
    'Let`s talk about something else! What`s the weather like today?',
    'Let`s talk about something else! Cats or dogs?',
    'Let`s talk about something else! Have you ever tried snowboarding?',
    'Let`s talk about something else! Do you like dancing?',
    'Let`s talk about something else! What plans do you have for tomorrow?',
]

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
    'appetizing', 'flavoursome', 'delectable', 'disgusting', 'awful', 'terrible', 'tasteless', 'horrific', 'bad'
]

keyWords = verbs + adjectives + adverbsOfTime + [
    'pizza', 'i', 'you', 'why', 'what', 'where', 'when', 'how', '?', 'yes', 'no',
    "hello", "hi", "greetings", "morning", "afternoon", "evening", "howdy",
    "maybe", "definitely", 'certain', 'probably', 'might', 'perhaps', 'possible', 'likely',
    'thank', 'thanks'
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

    'i feel *': ['Why do you feel that way?'],
    'i * feel *': ['Why do you feel that way?'],

    '* love *': feelingsTemplates,
    'i love *': agreeTemplates,
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
    'how about': suggestionsTemplates,
    'what about':suggestionsTemplates,

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
