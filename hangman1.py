
from words import choose_word
from images import IMAGES
 
def is_word_guessed(secret_word, letters_guessed):
    if secret_word == get_guessed_word(secret_word, letters_guessed):
        return True
def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word
def get_available_letters(letters_guessed):
    import string
    letters_left = string.ascii_lowercase
    for i in letters_guessed:
        letters_left =letters_left.replace(i,"")
    return letters_left
def get_hint(secret_word, letters_guessed):
    import random
    letters_not_guessed = []
    
    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)
        index += 1
    return random.choice(letters_not_guessed)    
def ifValid(user_input):
    if len(user_input) != 1:
        return False

    if not user_input.isalpha():
        return False
    return True


def hangman(secret_word):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("")
    j=0
    while j<1:
        level=input("enter the level which you want to play""\n""a for easy""\n""b for medium""\n""c for hard")
        if  level=="a" or level not in ["a","b","c"]:
            print("your choice in valied""\n" "game is starting in easy level")
            total_lives=remaining_lives=8
            images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]
            j+=1
        elif level=="b":
            total_lives=remaining_lives=6
            images_selection_list_indices=[0,2,3,5,6,7]
         
            j+=1
        elif level=="c":
            total_lives=remaining_lives=4
            images_selection_list_indices=[1,3,5,7]
            
            j+=1
        else:
            continue
    letters_guessed = []
    c=0
    while remaining_lives>0:
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " + available_letters)

        guess = input("Please guess a letter: ")
        letter = guess.lower()
        if letter=="hint":
            if c==0:
                print("your hint for secret word is"+get_hint(secret_word,letters_guessed))
                c+=1
            else:
                print("you have already used") 
                print("guess a letter again:-")
        
        if (not ifValid(letter)) :
            continue 
        if letter in secret_word:
            letters_guessed.append(letter)
            print(letters_guessed)
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print("")

            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ")
                print("")
        else:
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            letters_guessed.append(letter)
            print (IMAGES[images_selection_list_indices[total_lives-remaining_lives]])
            remaining_lives-=1
            print(remaining_lives)
            print("")
    else:
        print("sorry you loss the game the word was-"+secret_word)
secret_word = choose_word()
hangman(secret_word)