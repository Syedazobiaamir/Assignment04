# Sentence starter
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

# Ask the user for inputs
adjective = input("Please type an adjective and press enter: ")
noun = input("Please type a noun and press enter: ")
verb = input("Please type a verb and press enter: ")

# Construct the final sentence
final_sentence = f"{SENTENCE_START} {adjective} {noun} {verb}!"

# Print the fun story
print("\n" + final_sentence)
