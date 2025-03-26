from wonderland import rabbit
import re

# This function repeats the input phrase with a comma in between
def repeat_with_comma(phrase: str):
    phrase1, phrase2 = phrase, phrase
    return phrase1 + ", " + phrase2

# This function prepares the phrase and calls rabbit()
def the(phrase: str):
    new_phrase = repeat_with_comma(phrase)
    rabbit(new_phrase)

# This function searches for the word "late" and prints a message if found
def down():
    phrase = "I'm late"
    match = re.search("late", phrase)
    if match:
        print("Found late!")  # Can be skipped using debugger
    the(phrase)

# Starts the program
def main():
    down()

if __name__ == "__main__":
    main()