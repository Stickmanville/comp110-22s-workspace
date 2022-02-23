"""Wordle puzzle game."""

__author__ = "730332997"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(searched_word: str, letter: str) -> bool:
    """Searches whether character is in word."""
    assert len(letter) == 1
    i: int = 0
    while i < len(searched_word):  # iterates to test if word contains same letter
        if letter == searched_word[i]:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Concatenates boxes."""
    assert len(guess) == len(secret)
    index: int = 0
    emoji: str = ""
    if guess == secret:  # tests if guess matches secret word
        while index < len(secret):  # iterates to create the string of green boxes
            emoji += GREEN_BOX
            index += 1
        return f"{emoji}"
    else:  # if word does not match program then must choose yellow or white box
        alt_index = 0
        while index < len(secret):  # iterates to create string of colored boxes
            if guess[alt_index] == secret[index]:
                emoji += GREEN_BOX 
                alt_index += 1
            else:
                alt_index += 1
                if contains_char(secret, guess[index]) is True:
                    emoji += YELLOW_BOX
                else:
                    emoji += WHITE_BOX
            index += 1
        return f"{emoji}"


def input_guess(expected_length: int) -> str:
    """Tests if guess matches secret word length."""
    word: str = input(f"Enter a {expected_length} character word: ")
    while len(word) != expected_length:
        word = input(f"That wasn\'t {expected_length} chars! Try again: ")
    return word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 0
    while turns < 6:
        turns += 1
        print(f"=== Turn {turns}/6 ===")
        input: str = input_guess(len(secret_word))
        print(emojified(input, secret_word))
        if input == secret_word:
            print(f"You won in {turns}/6 turns!")
            return
    print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main()