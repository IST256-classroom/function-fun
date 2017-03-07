'''
We are going to write an advanced game of guess the word to demonstrate how we use funtions
Below are 7 functions that are used for the main program. Each Group needs to define their function
with the right inputs and it needs to return the proper value. The function name is given along with what inputs
it needs and what it should return.
'''

# Import statements are always at the top
import random

random_words = [
    "milanese"
    "roscius"
    "broch"
    "postseason"
    "imbuing"
    "razorfish"
    "elasticity"
    "universalizer"
    "sedged"
    "spiegel"
]

# Todos
# Retrieve a random word from the provided list of words
# Ask the user for a letter
# Increment the try count
# If the word is longer that 1 letter, see if the guess is correct
# If the user already guessed the letter, let them know and start over
# If equal to 1 letter Check to see if the letter exists in the word
# replace the space in the word with the guessed character
# add letter to guessed letters
# rinse repeat

'''
Group 1:
Write a function named get_random_word, It does not take an input
and returns a random word from the list provided (random_words)
You will need to use indexing to get the word
'''
# Group 1 Function Here
import random

random_words= [
        "milanese",
        "roscius",
        "broch",
        "postseason",
        "imbuing",
        "razorfish",
        "elasticity",
        "universalizer",
        "sedged",
        "spiegel",
    ]


def get_random_word():
    random_number = random.randint(0, len(random_words))
    print(random_number)
    return random_words[random_number]


'''
Group 2:
Write a function named check_guessed_word, It should take 2 str inputs and compare
them to see if they are equal. Return True if the are, False if they aren't
'''
# Group 2 Function Here

def check_guessed_word(word_compare, compared_to):
    if word_compare == compared_to:
        return True
    else:
        return False


'''
Group 3:
Write a function named check_character_in_word, It should take 2 str and return true if
str_1 is in str_2, or return false if its not
'''
# Group 3 Function Here
def check_character_in_word(str_1, str_2):
    for c in str_2:
        if c == str_1:
            return True
    return False


'''
Group 4:
Write a function named replace_letters_in_word, it should take 3 strings, and replace all
occurances of str_1 in str_2 and replace them by index in str_3 and return the str_3
There are a couple of ways to do this
'''
# Group 4 Function Here
def replace_letters_in_word(char, str_2, str_3):
    split_str3 = list(str_3)
    index = -1
    for c in str_2:
        index = index + 1
        if c == char:
            split_str3[index] = char
    return "".join(split_str3)


'''
Group 5:
Write a function named generate_blanks, it should take a str as an input and return
a string with the same amount of _ as the original string: Ex: take example return "_______"
'''
# Group 5 Function Here

def generate_blanks(string1):
    num_blanks = '_' * len(string1)
    return num_blanks

'''
Group 6:
Write a function named save_guess, This should take 2 str arguments and add str 2 to str 1,
and return the new string.
'''
# Group 6 Function Here

def save_guess(str_1, str_2):
    new_str = (str_2 + str_1)
    return(new_str)


'''
Group 7:
Write a function named main, it takes no input but uses the functions above to create the program:
I started it for you
'''
def main():
    random_word = get_random_word()
    guessed_word = generate_blanks(random_word)
    trys = 0
    letters_guessed = ""

    print("Welcome to the Word Guesser!")
    print(random_word)
    while True:
        print(guessed_word)
        '''
        Finish the loop here. Use the functions available to you, your know the names
        inputs and outputs
        '''
        guess = input("Please guess the word, or guess a letter: ")
        trys = trys + 1
        if len(guess) > 1:
            if check_guessed_word(random_word, guess):
                break
            else:
                print("Wrong! Please try again")
        else:
            if guess in letters_guessed:
                print("Your already chose that letter")
            else:
                if check_character_in_word(guess, random_word):
                    guessed_word = replace_letters_in_word(guess, random_word, guessed_word)
                else:
                    print("Wrong!, Please choose another letter")
                if not "_" in guessed_word:
                    break
    
    print("Nice Work!")
    print("You guessed the word: {} in {} trys".format(random_word, trys))
    # Group 7 do this too!


# Call the main function to start the program
main()



