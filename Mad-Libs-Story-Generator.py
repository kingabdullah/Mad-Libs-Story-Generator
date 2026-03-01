# start of the program
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

# collect user input
noun = input("Enter a noun (person/place/thing): ")
verb = input("Enter a verb (action word): ")
adjective = input("Enter an adjective (describing word): ")
adverb = input("Enter an adverb (how something is done): ")
place = input("Enter a place: ").title()
name = input("Enter a name: ").title()


# generate and print story
print()
print("Here is your Mad Libs story:")
print("-" * 64)
print(f"Once upon a time, in a {adjective} {place}, there lived a {noun} named {name}.")
print(f"Every day, {name} would {verb} {adverb}.")
print("-" * 64)

