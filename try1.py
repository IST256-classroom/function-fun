import random

random_words= [
        "milanese",
        "roscius",
        "broch",
        "postseason",
        "imbuing",
        "razorfish",
        "elasticity",
        "universalizer",
        "sedged",
        "spiegel",
    ]


def get_random_words():
    computer = random.randint(0, len(random_words))
    print(computer)
    return random_words[computer]


output = get_random_words()

print(output)
