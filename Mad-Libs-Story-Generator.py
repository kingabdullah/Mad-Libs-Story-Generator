#introduction function to welcome the user and explain the game
def show_welcome():    
    print()
    print("=" * 64)
    print("            WELCOME TO THE MAD LIBS STORY GENERATOR")
    print("=" * 64)
    print()
    print("How to play:")
    print("You will be asked for words like nouns, verbs, and adjectives.")
    print("Your answers will be used to build a funny custom story.")
    print()
    print("Let's get started!")
    print("^" * 64)
    print()
    
#function to collect user input
def collect_user_input():
    noun = input("Enter a singular noun (like: dragon, teacher, car): ")
    verb = input("Enter a verb in base form (like: run, fight, jump): ")
    adjective = input("Enter an adjective (like: big, scary, funny): ")
    adverb = input("Enter an adverb (usually ends in -ly, like: quickly, loudly): ")
    place = input("Enter a place (like: Paris, school, Mars): ").title()
    name = input("Enter a name (like: Alex, Maria): ").title()
    return {
    "noun": noun,
    "verb": verb,
    "adjective": adjective,
    "adverb": adverb,
    "place": place,
    "name": name
    } 



#list of words for random story generation
import random
nouns = ["dragon", "robot", "pirate", "penguin", "wizard"]
verbs = ["explode", "dance", "teleport", "whisper", "juggle"]
adjectives = ["crazy", "sparkly", "gigantic", "mysterious", "sleepy"]
adverbs = ["wildly", "gracefully", "awkwardly", "dramatically", "silently"]
places = ["Paris", "Tokyo", "Mars", "New York", "Atlantis"]
names = ["Oliver", "Zara", "Max", "Luna", "Theo"]

def generate_random_story():
    return {
    "noun": random.choice(nouns),
    "verb": random.choice(verbs),
    "adjective": random.choice(adjectives),
    "adverb": random.choice(adverbs),
    "place": random.choice(places),
    "name": random.choice(names)
     }


#funciton to build the story
def build_story(choice, words):
    noun = words["noun"]
    verb = words["verb"]
    adjective = words["adjective"]
    adverb = words["adverb"]
    place = words["place"]
    name = words["name"]

    if choice == "1":
        story = f"""
------------------------------------------------
 Adventure Story
------------------------------------------------
In the magical land of {place}, a {adjective} {noun} named {name}
decided to {verb} {adverb}.

Suddenly, the ground started shaking!
But {name} bravely continued to {verb} and saved the day.

The people of {place} will never forget the heroic {noun}.
------------------------------------------------
"""

    elif choice == "2":
        story = f"""
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
"""

    elif choice == "3":
        story = f"""
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
    else:
        story = "Invalid choice."

    return story


play_again = "yes"
while play_again.lower() == "yes":

    # start of the program
    show_welcome()

    # story type selection 
    print()
    print("Choose a story type:")
    print("1. Adventure")
    print("2. Funny")
    print("3. Spooky")

    choice = input("Enter 1, 2, or 3: ")
    while choice not in ["1", "2", "3"]:
        choice = input("Please enter 1, 2, or 3: ")
    
    # mode selection user input or random
    print("Choose mode:")
    print("1. Enter your own words")
    print("2. Random words")

    # picking the mode for the story

    mode = input("Enter 1 or 2: ")
    while mode not in ["1", "2"]:
        mode = input("Please enter 1 or 2: ")

    if mode == "1":
        noun, verb, adjective, adverb, place, name = collect_user_input()#collect user input for the story
    else:
        noun, verb, adjective, adverb, place, name = generate_random_story() #generate random words for the story
        print("Random words selected!")

    
        
    print("Here is your Mad Libs story:")

    
    story = build_story(choice, noun, verb, adjective, adverb, place, name)    
    print(story)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    while play_again not in ["yes", "no", "y", "n"]:
     play_again = input("Please enter 'yes' or 'no': ").lower()
print("Thanks for playing the Mad Libs Story Generator! Goodbye!")
