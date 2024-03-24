from display_utility import green
from display_utility import yellow
from display_utility import grey
from words import words
import random




def check_word(secret,guess):
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
                        for yellow_characters in range(len(guess)):
                             if colors[yellow_characters] =="yellow" and yellow_characters!= check_indices and guess[check_indices] == guess[yellow_characters]:
                                colors[check_indices] = ""
                        

        """Assigning gray hints"""
        for char in range(len(secret)):
            if colors[char] == "":
                colors[char] = "grey"

        return colors




def known_word(clues):
        """
        Returns the known string from a list recording guesses taken
        and clues received.
        """
        word = "_____"
        for i in range(len(clues)):
            for char in range (5):
                if clues[i][1][char] == "green":
                    old_word = word
                    word = old_word[:(char)]
                    word += clues[i][0][char]
                    word += old_word[(char+1):]
        return word  



def no_letters(clues):
        """
        Returns string of letters that are not in thr word
        from a list that recorded guesses taken
        and clues received.
        """
        word_list = []
        for i in range(len(clues)):
            """Iterates thtrough the list of tuples/clues"""
            for c in range(5):
                """Iterates through the guess colors list and guess char"""
                if (clues[i][1][c] == "grey"):
                    grey_char = clues[i][0][c]
                    should_add = True
                    for letters in word_list:
                        """Checks if letter is already in return string"""
                        if letters == grey_char:
                            should_add = False
                    for chars in range(5):
                        """Checks if letters repeats in word and is not grey"""
                        if grey_char == clues[i][0][chars] and clues[i][1][chars] != "grey":
                            should_add = False
                    if should_add:
                        word_list.append(clues[i][0][c])
        word_list.sort()
        grey_letters = ""
        for letters in word_list:
            grey_letters += letters
        return grey_letters


def yes_letters(clues):
        """
        Returns string of letters that are not in thr word
        from a list that recorded guesses taken
        and clues received.
        """
        word_list = []
        for i in range(len(clues)):
            """Iterates thtrough the list of tuples/clues"""
            for c in range(5):
                """Iterates through the guess colors list and guess char"""
                if (clues[i][1][c] != "grey"):
                    non_grey_char = clues[i][0][c]
                    should_add = True
                    for letters in word_list:
                        """Checks if letter is already in return string"""
                        if letters == non_grey_char:
                            should_add = False
                    for chars in range(5):
                        """Checks if letters repeats in word and is grey"""
                    if should_add:
                        word_list.append(clues[i][0][c])
        word_list.sort()
        grey_letters = ""
        for letters in word_list:
            grey_letters += letters
        return grey_letters 




def game(secret):
        """Runs the game using different functions for only 6 guesses and prints the Answer at the end"""
        guess_count=0
        clues = []
        non_grey_letters = ""
        grey_letters = ""
        known_letters = "_____"
        
        print("Known : " + known_letters)
        print("Green/Yellow Letters: " + non_grey_letters)
        print("Grey Letters: " + grey_letters)
       
        """Runs rounds with 6 rounds and if correct, guess count set to 6 to ensure loop doesnt continue""" 
        while guess_count<6:
            if (play_round(secret,clues, non_grey_letters, grey_letters, known_letters, guess_count)):
                guess_count=6
            guess_count+=1
        
        print ("Answer: " + secret )
            



def is_Valid(guess):
        """
        Determines if guess is valid (valid word and equal to length 5)"""
        if len(guess)==5:
            for word in words:
                if word == guess:
                    return True
        return False



def play_round(secret, clues, non_grey_letters, grey_letters, known_letters,guess_count):
        """Runs each round of gameplay in which it takes guess and updates clues, non_grey_ltters, grey_letters,
     known_letters. It also runs the print_round function that prints the round for the
    user to look at."""
        guess = input("> ").strip().lower()
        while is_Valid(guess) == False:#validates that guess is valid
            guess = try_again(secret, clues) 
        if is_Valid(guess):
            guess = guess.upper()
            clue = check_word(secret.upper(),guess.upper())
            clues.append((guess,clue))
        else:
            guess = try_again(secret, clues)

        """Assigns values with the resulting functions"""
        grey_letters = no_letters(clues)
        non_grey_letters = yes_letters(clues)
        known_letters = known_word(clues)

        if guess!= secret:
            print_round(clues, non_grey_letters, grey_letters, known_letters) #prints for non-correct guesses
        else: #prints for correct guesses
            for clue in clues:
                for chars in range(5):
                    if clue[1][chars] == "green":
                        green(clue[0][chars])
                    if clue[1][chars] == "yellow":
                        yellow(clue [0][chars])
                    if clue [1][chars] == "grey":
                        grey(clue [0][chars])
                print() 
             
        
        if secret==guess:
                return True
        False

        





def print_round(clues, non_grey_letters, grey_letters, known_letters):
    """Prints the entire round when called by play_round including 
    the non_grey_letters, grey_letters, known_letters"""
    
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
    
    print("Known : " + known_letters)
    print("Green/Yellow Letters: " + non_grey_letters)
    print("Grey Letters: " + grey_letters)
    


def try_again(secret, clues):
    """If guess is not valid, ths code is ran to get a new input"""
    print("Not a word. Try again")
    return input("> ").strip().lower()




if __name__ == "__main__":
    rand = random.randint(0, len(words) - 1)
    game(words[rand])




"""
def known_word(clues):
        num_clues_index = len(clues)-1
        return_word = "_____"
        while num_clues_index>=0:
            char = 0
            while char<5:
                if clues[num_clues_index][1][char] == "green":
                    return_word+= clues[num_clues_index][0][char]
        return return_word


        



    def no_letters(clues):

        Returns string of letters that are not in thr word
        from a list that recorded guesses taken
        and clues received.
        

        word = ""
        for i in range(len(clues)):
            Iterates thtrough the list of tuples/clues

            for c in range(5):
                Iterates through the guess colors list and guess char
                
                if (clues[i][1][c] == "grey"):
                    If the color at the ist element of clues and 
                    c elemnt of the clue is grey 

                    count = 0
                    for nums in range(len(word)):
                    Iterates through the guess and clue once again

                        if word[nums] == clues[i][0][c]:  
                            if character at word equals the grey indexx
                            count+=1
                        if count==0:
                            for doubles in word:
                                if doubles == clues[i][0][c]:
                                    print("")
                    if count ==0:
                        word+= clues[i][0][c]
        return word





        
    if (clues[i][1][c] == "grey"):
                    grey_char = clues[i][0][c]
                    If the color at the ist element of clues and 
                    c elemnt of the clue is grey 
                    count = 0
                    for nums in range(len(word)):
                        Iterates through the guess and clue once again
                        new_char = clues[i][0][nums]
                        if grey_char == new_char and c!=nums: 
                            print(" There is a duplicate letter at : " + clues[i][0][c] + " At index of clues at " + str(i))
                            if clues[i][1][nums] != "grey":
                                print("This letter is in word: clues[i][0][c]")
                                count+=1
                    if count ==0:
                        word+= clues[i][0][c]



        



    def is_char_known(guess, clue, index):
        for char in guess:

 """    