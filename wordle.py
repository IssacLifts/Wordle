from random import choice
from words import words
from colorama import Fore, init
from sys import exit
from time import sleep
from os import system
init(autoreset=True)

global tries
global i
global codes
tries: list = list()
i: int = 0
codes: dict = {"SUCCESS": Fore.LIGHTMAGENTA_EX,
            "CORRECT": Fore.LIGHTGREEN_EX,
             "CLOSE": Fore.LIGHTYELLOW_EX,
             "INCORRECT": Fore.RED,
             "ERROR": Fore.LIGHTRED_EX
             }


# Chooses random english word \
    # That is 5 letters long and has only letters
pick_word = lambda: choice([word.upper() for word in words if len(word)==5 and word.isalpha()])


def checkColorDict(letter:str, colordict:dict, code:str) -> bool:
    """Adds a number to the end of duplicate keys

    Args:
        letter (str): letter that's being checked
        colordict (dict): dictionary of colored letters
        code (str): the color code that's being used

    Returns:
        bool: False if colorDict was incorrect \
            True if the colorDict was correct
            
    Example:
        The program tries to add the letter 'A' to the dictionary but the letter 'A' already exists\
            Therefore, this fuction adds a number to the end of that letter to not make it a duplicate.
    """
    global i
    for key in colordict.keys():
        if letter == key:
            letter += str(i)
            colordict[letter] = codes.get(code)
            i += 1
            return False
    return True

def isvalidword(guess:str, word: str) -> bool:
    """Checks if the word is valid & if the player has won

    Args:
        guess (str): The word the player guessed
        word (str): The correct word

    Returns:
        bool: True if the guessed correctly
    """
    # Check if player won
    if guess == word:
        return True
    
    try:
        assert guess.isalpha(), print(f"{codes['ERROR']}You must enter letters only.")
        assert len(guess)==5, print(f"{codes.get('ERROR')}Your word must be 5 letters long.")
    except AssertionError:
        wordle(word)
        
    # If all of the checks passed, the game is still ongoing/ user has entered correct input \
        # So continue
    
    # Returns the boolean value that's returned from the colorWords() function
    return colorWords(guess, word, colordict={})
    
def colorWords(guess:str, word:str, colordict:dict) -> bool:
    """Colors all the letters in the guess

    Args:
        guess (str): word the player guessed
        word (str): the actual word
        colordict (dict): dictionary to store letters tied to a color-code

    Returns:
        bool: False because if this function was called, the game is still ongoing
    """
    try:  
        for index, letter in enumerate(guess):
            if letter == word[index]:
                if checkColorDict(letter, colordict, "CORRECT"):
                    colordict[letter] = codes['CORRECT']
                    continue
                continue
                                           
            elif index != 0 and letter == word[index-1] or letter == word[index+1]:
                if checkColorDict(letter, colordict, "CLOSE"):
                    colordict[letter] = codes['CLOSE']
                    continue
                continue
                
            else:
                if checkColorDict(letter, colordict, "INCORRECT"):
                    colordict[letter] = codes['INCORRECT']
                    continue
                continue
                    
    except IndexError:
        if checkColorDict(letter, colordict, "INCORRECT"):
            colordict[letter] = codes['INCORRECT']
                    
    # Append the color-coded word to list
    tries.append(colordict)
    
    # return False because the game is still ongoing
    return False

            
def wordle(word:str) -> None:
    """Plays Wordle!

    Args:
        word (str): The correct word
    """
    colored_string = ""
    colored_words = []
    
    if len(tries) != 0: 
        for color in tries:
            # Creating the colored-coded string
            for key, value in color.items():
                colored_string += value + key[0]
            colored_words.append(colored_string)
            colored_string = ""
        
        for index, value in enumerate(colored_words):
            print(f"{Fore.CYAN}TRY {index+1}: {value}")
    

    guess = isvalidword(input(f"\n{Fore.LIGHTMAGENTA_EX}ATTEMPT {len(tries)+1}: ").upper(), word)
     
    # If guess is true it means the player guessed the correct word
    if guess:
        playerWon(word)
         
    wordle(word)
    
def playerWon(word:str) -> None:
    while True:
        print(f"{codes['SUCCESS']}You won! the word was: {codes['CORRECT']}{word.capitalize()}\nWould you like to play again? (y/n)")
        play_again = input(Fore.RED).lower()
        if play_again == "y":
            print("Restarting game...")
            sleep(2)
            restart_game()
        
        elif play_again == "n":
            print(f"{Fore.LIGHTMAGENTA_EX}Closing game...")
            sleep(2)
            exit()

def printColorCodes() -> None:
    print(f"{Fore.GREEN}GREEN- You have guessed the correct letter\n{Fore.YELLOW}YELLOW- You are 1 letter away (left or right) from the correct letter\n{Fore.RED}RED- Incorrect Letter")
        
def restart_game() -> None:
    global tries, i
    tries, i = [], 0
    system('cls')
    printColorCodes()
    wordle(pick_word())

if __name__ == "__main__":
    system('cls')
    printColorCodes()
    wordle(pick_word())