import random

# ==============================================================
# Word Bank Dictionary
# ==============================================================

word_bank = {
    "noun": ["dragon", "robot", "pirate", "penguin", "wizard"],
    "verb": ["explode", "dance", "teleport", "whisper", "juggle"],
    "adjective": ["crazy", "sparkly", "gigantic", "mysterious", "sleepy"],
    "adverb": ["wildly", "gracefully", "awkwardly", "dramatically", "silently"],
    "place": ["Paris", "Tokyo", "Mars", "New York", "Atlantis"],
    "name": ["Oliver", "Zara", "Max", "Luna", "Theo"]
}

# ==============================================================
# Story Templates
# ==============================================================

stories = {
    "1": """
------------------------------------------------
 Adventure Story
------------------------------------------------
In the magical land of {place}, a {adjective} {noun} named {name}
decided to {verb} {adverb}.

Suddenly, the ground started shaking!
But {name} bravely continued to {verb} and saved the day.

The people of {place} will never forget the heroic {noun}.
------------------------------------------------
""",

    "2": """
------------------------------------------------
 Funny Story
------------------------------------------------
One morning in {place}, a {adjective} {noun} named {name}
started to {verb} {adverb} in the middle of the street.

Everyone stared.
Someone screamed.
A pigeon fainted.

By sunset, {name} was trending everywhere.
------------------------------------------------
""",

    "3": """
------------------------------------------------
 Spooky Story
------------------------------------------------
Late at night in {place}, a {adjective} {noun} named {name}
began to {verb} {adverb} under the full moon.

A cold wind blew.
Strange whispers echoed.
Something was watching...

And no one ever saw {name} the same way again.
------------------------------------------------
"""
}

# ==============================================================
# Functions
# ==============================================================

def show_welcome():
    print("\n" + "=" * 64)
    print("            WELCOME TO THE MAD LIBS STORY GENERATOR")
    print("=" * 64)
    print("\nHow to play:")
    print("Enter words or choose random mode to generate a story.")
    print("^" * 64 + "\n")


def collect_user_input():
    noun = input("Enter a singular noun: ")
    verb = input("Enter a verb (base form): ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb (ends in -ly): ")
    place = input("Enter a place: ").title()
    name = input("Enter a name: ").title()
    return noun, verb, adjective, adverb, place, name


def generate_random_story():
    return (
        random.choice(word_bank["noun"]),
        random.choice(word_bank["verb"]),
        random.choice(word_bank["adjective"]),
        random.choice(word_bank["adverb"]),
        random.choice(word_bank["place"]),
        random.choice(word_bank["name"])
    )


def build_story(choice, noun, verb, adjective, adverb, place, name):
    return stories[choice].format(
        noun=noun,
        verb=verb,
        adjective=adjective,
        adverb=adverb,
        place=place,
        name=name
    )

# ==============================================================
# Main Program
# ==============================================================

while True:
    show_welcome()

    print("Choose a story type:")
    print("1. Adventure")
    print("2. Funny")
    print("3. Spooky")

    choice = input("Enter 1, 2, or 3: ")
    while choice not in stories:
        choice = input("Please enter 1, 2, or 3: ")

    print("\nChoose mode:")
    print("1. Enter your own words")
    print("2. Random words")

    mode = input("Enter 1 or 2: ")
    while mode not in ["1", "2"]:
        mode = input("Please enter 1 or 2: ")

    if mode == "1":
        words = collect_user_input()
    else:
        words = generate_random_story()
        print("\nRandom words selected!")

    print("\nHere is your Mad Libs story:")
    print(build_story(choice, *words))

    again = input("Play again? (yes/no): ").lower()
    if again not in ["yes", "y"]:
        break

    print("\n" + "=" * 70 + "\n")

print("Thanks for playing! Goodbye!")