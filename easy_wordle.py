from display_utility import green
from display_utility import grey
from display_utility import yellow

from words import words
import random


                    

def check_clues(clue1,clue2):
    """Takes two clues and returns if they have the same colors for each character
    in the clue."""
    for color in range(5):
        if clue1[color] != clue2[color]:
            return False
    return True
               
    
def easy_check_word(secret,guess):
    "Takes in a guess and returns the output clue"
    colors = ["","","","",""]

    """Assigning green hints"""
    for char in range(len(secret)):
        if guess[char] == secret[char]:
            colors[char] = "green"
        
    """Assigning yellow hints"""
    for char in range(len(secret)):
        if colors[char] != "green":
            for check_indices in range(len(secret)):
                if guess[check_indices] == secret[char] and colors[check_indices]!= "green":
                    colors[check_indices] = "yellow"

    """Assigning grey hints"""
    for char in range(len(secret)):
        if colors[char] == "":
            colors[char] = "grey"
    return colors
   

def filter_word_list(words, clues):
    """Filters and return list with words that can be hints based upon if they work for every single clue"""
    num_cases_right = 0
    all_hints = []
    #Adds all instances clues match and if instances fo match, it is added to all_hints and returne
    for word in words:
            for clue in clues:
                if clue[1] == easy_check_word(word.lower(), clue[0].lower()):
                    num_cases_right +=1
            if num_cases_right == len(clues):
                    all_hints.append(word)
            num_cases_right = 0

    return all_hints
    
"""clues = [
    ("TUNES", ["yellow", "green", "green", "grey", "green"]),
    ("ALPHA", ["green", "grey", "grey", "grey", "grey"]),
    ("MONTH", ["grey", "grey", "green", "green", "grey"]),
    ("DUMMY", ["grey", "green", "grey", "grey", "grey"]),
]
print(filter_word_list(words, clues))  # ['aunts']"""

    
def easy_game(secret):
    """Runs the game using different functions for only 6 guesses and prints the Answer at the end"""
    guess_count=0
    clues = []
    num_possible = 0
    all_words_clues = []
    all_words = words
    
    """Runs rounds with 6 rounds and if correct, guess count set to 6 to ensure loop doesnt continue""" 
    while guess_count<6:
        if easy_play_round(secret, clues, num_possible,all_words, all_words_clues):
            guess_count=6
        guess_count+=1
        
    print ("Answer: " + secret )
            



def easy_is_Valid(guess):
    """
    Determines if guess is valid (valid word and equal to length 5)"""
    if len(guess)==5:
        for word in words:
            if word == guess:
                return True
    return False





def easy_play_round(secret, clues, num_possible, all_words, all_words_clues):
    """Runs each round of gameplay in which it takes guess and updates clues, all_words, num_possible
    and many other fucntions. It also runs the easy_print_round function that prints the round for the
    user to look at."""
    guess = input("> ").strip().lower()

    while easy_is_Valid(guess) == False:
        guess = easy_try_again()

    #Assigns all values for clue, clues, all_words_clues, and num_possible with easy_check word
    # and filter_list
    guess = guess.upper()
    clue = easy_check_word(secret,guess)
    clues.append((guess,clue))
    all_words_clues = filter_word_list(all_words, clues)
    num_possible = len(all_words)
    easy_print_round(clues, num_possible, all_words_clues)
        
    if secret==guess:
        return True
    False

        





def easy_print_round(clues, num_possible, all_words_clues):
    """Prints the entire round when called by easy_play_round including the colored hint,
    nums possible, and 5 hints"""
    last_index = len(clues)-1
    print_word = ""
    """Prints each clue with the color formatting """
    for clue in clues:
        for chars in range(5):
            if clue[1][chars] == "green":
                green(clue[0][chars])
            if clue[1][chars] == "yellow":
                yellow(clue [0][chars])
            if clue [1][chars] == "grey":
                grey(clue [0][chars])
        print()
    num_possible = len(all_words_clues)
    """Prints words possible and up to 5 possible words"""
    print(str(num_possible) + " words possible: ")
    if (len(all_words_clues))<=5:
        for word in all_words_clues:
            print(word)   
    else:
        print_words = random.shuffle(all_words_clues)
        print_words = all_words_clues[:5]
        for word in print_words:
            print(word)


                


def easy_try_again():
    """If guess is not valid, ths code is ran to get a new input"""
    print("Not a word. Try again")
    return input("> ").strip().lower()




if __name__ == "__main__":
    rand = random.randint(0, len(words) - 1)
    easy_game(words[rand])         

"""for rep in range(len(all_words_clues)):
                    if print_word == all_words_clues[rep-1]:
                        all_words_clues.remove(print_word)"""