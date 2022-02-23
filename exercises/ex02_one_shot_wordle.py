"""EX02 - One Shot Wordle - Fun with words!"""

__author__ = "730332997"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index: int = 0
emoji: str = ""
secret_word: str = "python"
word_limit: int = len(secret_word)

word: str = input(f"What is your {word_limit}-letter guess? ")
word_length: int = len(word)

while word_length != word_limit:
    word = input(f"That was not {word_limit} letters! Try again: ")
    word_length = len(word)

if secret_word == word:  # tests if guess matches secret word
    while index < word_limit:  # iterates to create the string of green boxes
        emoji = emoji + GREEN_BOX 
        index = index + 1
    print(f"{emoji}")
    print("Woo! You got it!")
else:  # if word does not match program then must choose yellow or white box
    while index < word_limit:  # iterates to create string of colored boxes
        if word[index] == secret_word[index]:
            emoji = emoji + GREEN_BOX 
            index = index + 1
        else:
            anywhere: bool = False
            alt_index = 0
            while anywhere is False and alt_index < word_limit:  # iterates to test if word contains same letter
                if word[index] == secret_word[alt_index]:
                    anywhere = True
                else:
                    alt_index = alt_index + 1
            if anywhere is False:
                emoji = emoji + WHITE_BOX
            else:
                emoji = emoji + YELLOW_BOX
            index = index + 1

    print(f"{emoji}")
    print("Not quite. Play again soon!")