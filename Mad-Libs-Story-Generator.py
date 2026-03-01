
#introduction function 
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
    print()
    
#function to collect user input
def collect_user_input():
    noun = input("Enter a noun (person/place/thing): ")
    verb = input("Enter a verb (action word): ")
    adjective = input("Enter an adjective (describing word): ")
    adverb = input("Enter an adverb (how something is done): ")
    place = input("Enter a place: ").title()
    name = input("Enter a name: ").title()
    return noun, verb, adjective, adverb, place, name

#funciton to build the story
def build_story(noun, verb, adjective, adverb, place, name):
    story = f"""
Here is your Mad Libs story:
------------------------------------------------
Once upon a time, in a {adjective} {place}, there lived a {noun} named {name}.
Every day, {name} would {verb} {adverb}.
------------------------------------------------
"""
    return story


play_again = "yes"
while play_again.lower() == "yes":

    # start of the program
    show_welcome()

    # collect user input
    noun, verb, adjective, adverb, place, name = collect_user_input()

    # generate and print story
    print()
    print("Here is your Mad Libs story:")
    story = build_story(noun, verb, adjective, adverb, place, name)
    print(story)

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != "yes" and play_again != "no":
        print("Invalid input. Exiting the game.")
        play_again = "no"
