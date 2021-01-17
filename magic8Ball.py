import random

messages = ("It is certain",
            "It is decidedly so",
            "Yes",
            "Reply hazy try again",
            "Ask again later",
            "Concentrate and ask again",
            "My reply is no",
            "Outlook not so good",
            "Very doubtful")

fortune = messages[random.randint(0, len(messages)-1)]
print(fortune)

