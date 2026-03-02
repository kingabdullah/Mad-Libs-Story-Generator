import random

# Word bank for random mode
word_bank = {
    "noun": ["dragon", "robot", "pirate", "penguin", "wizard"],
    "verb": ["explode", "dance", "teleport", "whisper", "juggle"],
    "adjective": ["crazy", "sparkly", "gigantic", "mysterious", "sleepy"],
    "adverb": ["wildly", "gracefully", "awkwardly", "dramatically", "silently"],
    "place": ["Paris", "Tokyo", "Mars", "New York", "Atlantis"],
    "name": ["Oliver", "Zara", "Max", "Luna", "Theo"]
}

# Definitions + examples
definitions = {
    "noun": "A noun is a person, place, or thing. Example: dog, school, car.",
    "verb": "A verb is an action word. Example: run, jump, eat.",
    "adjective": "An adjective describes a noun. Example: big, funny, scary.",
    "adverb": "An adverb describes a verb (usually ends in -ly). Example: quickly, slowly.",
    "place": "Enter a place. Example: New York, beach, school.",
    "name": "Enter a person's name. Example: John, Sarah."
}

# Story templates
stories = {
    "1": """
============================================================
                        EPIC ADVENTURE
============================================================

In the powerful kingdom of {place}, there lived a {adjective} {noun}
named {name}.

One day, {name} discovered a mysterious message that said:
"You must {verb} {adverb} to save everything."

Without hesitation, {name} accepted the challenge.

Mountains trembled.
Storms filled the sky.
Enemies appeared from nowhere.

But with bravery and determination, {name} continued to {verb}
until peace finally returned to {place}.

From that day on, songs were written about the legendary {noun}
named {name}.
""",

    "2": """
============================================================
                            FUNNY STORY
============================================================

Everything was normal in {place}...

Until a {adjective} {noun} named {name}
suddenly started to {verb} {adverb}
right in the middle of town.

At first, people were confused.
Then someone started laughing.
Then everyone started laughing.

Soon, a crowd formed.
Someone began recording.
A news reporter showed up.

By sunset, {name} was officially known as
"That {adjective} {noun} Who Loves to {verb}."

And honestly, nobody could stop talking about it.
""",

    "3": """
============================================================
                            SCARY STORY
============================================================

It was past midnight in {place}.

A {adjective} {noun} named {name}
slowly began to {verb} {adverb}
in the darkness.

The streetlights flickered.
A cold wind whispered through the air.
Footsteps echoed... but no one was there.

{name} suddenly stopped.

Something was standing behind them.

Breathing.

Waiting.

And whatever it was...
it was not human.
"""
}

# Print instructions once
print("\n" + "=" * 60)
print("            MAD LIBS STORY GENERATOR")
print("=" * 60)
print("\nInstructions:")
print("- Choose a story type (Epic, Funny, or Scary).")
print("- Enter your own words or choose random mode.")
print("- If you are unsure, examples will be shown.")
print("- You can play again after the story ends.\n")


# Collect user words (with examples)
def collect_user_input():
    words = {}
    word_types = ["noun", "verb", "adjective", "adverb", "place", "name"]

    print("\nEnter your words below:\n")

    for word in word_types:
        print(definitions[word])  # shows definition + example
        user_input = input(f"Enter a {word}: ").strip()

        while user_input == "":
            user_input = input(f"You must enter a {word}: ").strip()

        if word in ["place", "name"]:
            user_input = user_input.title()

        words[word] = user_input
        print()  # small space for readability

    return words


# Random mode
def generate_random_words():
    words = {}
    for category in word_bank:
        words[category] = random.choice(word_bank[category])
    return words


# Build story
def build_story(choice, words):
    return stories[choice].format(
        noun=words["noun"],
        verb=words["verb"],
        adjective=words["adjective"],
        adverb=words["adverb"],
        place=words["place"],
        name=words["name"]
    )

#========================================
# Main game loop
#========================================

while True:

    print("\nChoose a Story Type:")
    print("1. Epic Adventure")
    print("2. Funny")
    print("3. Scary")

    choice = input("Enter 1, 2, or 3: ")

    while choice not in stories:
        choice = input("Please enter 1, 2, or 3: ")

    print("\nChoose Mode:")
    print("1. Enter your own words")
    print("2. Random words")

    mode = input("Enter 1 or 2: ")

    while mode not in ["1", "2"]:
        mode = input("Please enter 1 or 2: ")

    if mode == "1":
        words = collect_user_input()
    else:
        words = generate_random_words()
        print("\nRandom words selected.\n")

    final_story = build_story(choice, words)

    
    print(final_story)

    again = input("\nWould you like to play again? (yes/no): ").lower()

    while again not in ["yes", "y", "no", "n"]:
        again = input("Please enter yes or no: ").lower()

    if again in ["no", "n"]:
        print("\nThanks for playing. Goodbye!")
        break