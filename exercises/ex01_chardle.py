"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730332997"

characterlimit: int = 5
letterlimit: int = 1
word: str = input("Enter a 5-character word: ")
wordlength: int = len(word)
wordcount: int = 0

if wordlength == characterlimit:
    letter: str = input("Enter a single character: ")
    letterlength: int = len(letter)
  
    if letterlength == letterlimit:
        print("Searching for " + letter + " in " + word)
        
        if word[0] == letter:
            print(letter + " found at index 0")
            wordcount = wordcount + 1
        else:
            wordcount = wordcount
       
        if word[1] == letter:
            print(letter + " found at index 1")
            wordcount = wordcount + 1
        else:
            wordcount = wordcount

        if word[2] == letter:
            print(letter + " found at index 2")
            wordcount = wordcount + 1
        else:
            wordcount = wordcount
        
        if word[3] == letter:
            print(letter + " found at index 3")
            wordcount = wordcount + 1
        else:
            wordcount = wordcount

        if word[4] == letter:
            print(letter + " found at index 4")
            wordcount = wordcount + 1
        else:
            wordcount = wordcount
  
        if wordcount == 0:
            print("no instances of " + letter + " found in " + word)
        else:
            if wordcount == 1:
                print("1 instance of " + letter + " found in " + word)
            else:
                print(str(wordcount) + " instances of " + letter + " found in " + word)

    else:
        exit("Error: Character must be a single character.")

else: 
    exit("Error: Word must contain 5 characters")